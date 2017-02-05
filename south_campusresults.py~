import requests
from bs4 import BeautifulSoup as bs
import MySQLdb
db=MySQLdb.connect("localhost","root","plutonian","test1")
cursor2=db.cursor()
cmd="""select * from api_south_campuscounters"""
cursor2.execute(cmd)
alt=cursor2.fetchone()
db.commit()
src=requests.get("http://exam.du.ac.in/south_results.html").text
soup=bs(src,"html.parser")
soup1=soup.find_all('article',id="contents")[0]          
soup2=soup1.find_all('a') 
file1=open('south_campusresults.txt','w+')
counter=1
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
     title=link //smjh nahi aaya bc 
     #print "1"
     if title == alt[1]:
        cursor2.execute("""update api_south_campuscounters set south_campustitle=%s""",(titlef,))
        break
     titlef=title
     m.append(link)
     k.append(title)
if myalt == alt[1]:
     condi=1;
while len(m) !=0:
     r=m.pop()
     p=k.pop()
     sql="""insert into api_south_campusresults(id,title,linkf) values(NULL,'%s','%s')"""%(p,r)
     cursor2.execute(sql)
     if condi == 1:     
         cursor2.execute("""update api_south_campuscounters set south_campustitle=%s""",(p,))
     #print "3"
     counter=counter+1
     
file1.close()
db.commit()
cursor2.close()
#cursor3.close()
db.close()
