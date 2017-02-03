import requests
from bs4 import BeautifulSoup as bs
import MySQLdb
db=MySQLdb.connect("localhost","root","plutonian","test1")
cursor2=db.cursor()
#cursor3=db.cursor()
cmd="""select * from postgradcounters"""
cursor2.execute(cmd)
alt=cursor2.fetchone()
db.commit()
titlef=alt[1]
src=requests.get("http://exam.du.ac.in/PG-result.html").text
soup=bs(src,"html.parser")
soup1=soup.find_all('article',id="contents")[0]          
soup2=soup1.find_all('a') 
file1=open('postgradresults.txt','w+')
counter=alt[0]
v=0
k=[]
m=[]
myalt=alt[1]
condi=0;
for i in soup2:
     v=v+1
     if v<2:
         continue; 
     link=i["href"]
     title="".join([str(j) for j in i.contents]) 
     #print "1"
     if title == alt[1]:
        cursor2.execute("""update postgradcounters set postgradtitle=%s""",(titlef,))
        break
     titlef=title
     m.append(link)
     k.append(title)
if myalt == alt[1]:
     condi=1;
while len(m) !=0:
     r=m.pop()
     p=k.pop()
     sql="""insert into postgradresults(id,title,linkf) values(NULL,'%s','%s')"""%(p,r)
     cursor2.execute(sql)
     if condi == 1:     
         cursor2.execute("""update postgradcounters set postgradtitle=%s""",(p,))
     #print "3"
     counter=counter+1
     
file1.close()
db.commit()
cursor2.close()
#cursor3.close()
db.close()
