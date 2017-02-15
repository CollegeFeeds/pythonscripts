import requests
from bs4 import BeautifulSoup as bs
import MySQLdb
db=MySQLdb.connect("localhost","root","icancode23","dufeed")
cursor2=db.cursor()
#cursor3=db.cursor()
cmd="""select * from api_diplomacounters"""
cursor2.execute(cmd)
alt=cursor2.fetchone()
db.commit()
titlef=alt[1]
counter=alt[0]
src=requests.get("http://exam.du.ac.in/certificate-result.html").text
soup=bs(src,"html.parser")
soup1=soup.find_all('article',id="contents")[0]        
soup2=soup1.find_all('a') 
file1=open('diplomaresults.txt','w+')
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
        cursor2.execute("""update api_diplomacounters set diplomatitle=%s""",(titlef,))
        break
     titlef=title
     m.append(link)
     k.append(title)
if myalt == alt[1]:
     condi=1;
while len(m) !=0:
     r=m.pop()
     p=k.pop()
     sql="""insert into api_diplomaresults(id,title,linkf) values(NULL,'%s','%s')"""%(p,r)
     counter=counter+1
     cursor2.execute(sql)
     if condi == 1:     
         cursor2.execute("""update api_diplomacounters set diplomatitle=%s""",(p,))
     cursor2.execute("""update api_diplomacounters set diplomaid=%ld""",(counter,))
     cursor2.execute()
file1.close()
db.commit()
cursor2.close()
#cursor3.close()
db.close()
