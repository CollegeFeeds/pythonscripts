import requests
from bs4 import BeautifulSoup as bs
import MySQLdb
db=MySQLdb.connect("localhost","root","plutonian","test1")
cursor2=db.cursor()
#cursor3=db.cursor()
cmd="""select * from hansrajcounters"""
cursor2.execute(cmd)
alt=cursor2.fetchone()
db.commit()
titlef=alt[1]
src=requests.get("http://www.hansrajcollege.co.in/news.php").text
soup=bs(src,"html.parser")
soup1=soup.find_all('div',class_="urbanmenu")[0]          
soup2=soup1.find_all('a') 
file1=open('hansrajnotices.txt','w+')
k=[]
m=[]
myalt=alt[1]
condi=0;
#print "0"
for i in soup2:
     try:
         link=i["href"]
         title="".join([str(j) for j in i.contents]) 
     except:
         continue
     #print "1"
     if title==alt[1]:
         cursor2.execute("""update hansrajcounters set hansrajtitle=%s""",(titlef,))
         #cursor2.execute("""update hansrajcounter set hansrajid=%d""",(counter))
         break
     titlef=title
     m.append(link)
     k.append(title)
if myalt == alt[1]:
     condi=1;
while len(m) !=0:
     r=m.pop()
     p=k.pop()
     sql="""insert into hansrajnotices(id,title,linkf) values(NULL,'%s','%s')"""%(p,r)
     cursor2.execute(sql)
     if condi == 1:     
         cursor2.execute("""update hansrajcounters set hansrajtitle=%s""",(p,))
     
file1.close()
db.commit()
cursor2.close()
#cursor3.close()
db.close()
