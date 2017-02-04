import requests
from bs4 import BeautifulSoup as bs
import MySQLdb
db=MySQLdb.connect("localhost","root","plutonian","test1")
cursor2=db.cursor()
#cursor3=db.cursor()
cmd="""select * from api_srcccounters"""
cursor2.execute(cmd)
alt=cursor2.fetchone()
db.commit()
titlef=alt[1]
src=requests.get("http://www.srcc.edu/announcements").text
soup=bs(src,"html.parser")
soup1=soup.find_all('div',class_="year")[0]          
soup2=soup1.find_all('a') 
file1=open('srccnotices.txt','w+')
k=[]
m=[]
myalt=alt[1]
condi=0;
#print "0"
for i in soup2:
     link=i["href"]
     title=link
     #print "1"
     #print link
     #print " "
     if title==alt[1]:
         cursor2.execute("""update api_srcccounters set srcctitle=%s""",(titlef,))
         break
     titlef=title
     m.append(link)
     k.append(title)
if myalt == alt[1]:
     condi=1;
while len(m) !=0:
     r=m.pop()
     p=k.pop()
     sql="""insert into api_srccnotices(id,title,linkf) values(NULL,'%s','%s')"""%(p,r)
     cursor2.execute(sql)
     #file1.write('\n%s'%link)
     if condi == 1:     
         cursor2.execute("""update api_srcccounters set srcctitle=%s""",(p,))
     #counter=counter+1
     
file1.close()
db.commit()
cursor2.close()
#cursor3.close()
db.close()
