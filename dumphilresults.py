import requests
from bs4 import BeautifulSoup as bs
import MySQLdb
db=MySQLdb.connect("localhost","root","icancode23","dufeed")
cursor2=db.cursor()
#cursor3=db.cursor()
cmd="""select * from api_mphilcounters"""
cursor2.execute(cmd)
alt=cursor2.fetchone()
db.commit()
titlef=alt[1]
src=requests.get("http://exam.du.ac.in/Mphil-result.html").text
soup=bs(src,"html.parser")
soup1=soup.find_all('article',id="contents")[0]        
soup2=soup1.find_all('a') 
file1=open('mphilresults.txt','w+')
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
         continue;
     #print "1"
     if title == alt[1]:
        cursor2.execute("""update api_mphilcounters set mphiltitle=%s""",(titlef,))
        break
     titlef=title
     m.append(link)
     k.append(title)
if myalt == alt[1]:
     condi=1;
while len(m) !=0:
     r=m.pop()
     p=k.pop()
     sql="""insert into api_mphilresults(id,title,linkf) values(NULL,'%s','%s')"""%(p,r)
     cursor2.execute(sql)
     if condi == 1:     
         cursor2.execute("""update api_mphilcounters set mphiltitle=%s""",(p,))
     #print "3"
     
file1.close()
db.commit()
cursor2.close()
#cursor3.close()
db.close()
