import requests
from bs4 import BeautifulSoup as bs
import MySQLdb
db=MySQLdb.connect("localhost","root","plutonian","test1")
cursor2=db.cursor()
#cursor3=db.cursor()
cmd="""select * from undergradcounters"""
cursor2.execute(cmd)
alt=cursor2.fetchone()
db.commit()
titlef=alt[1]
src=requests.get("http://exam.du.ac.in/UG-result.html").text
soup=bs(src,"html.parser")
soup1=soup.find_all('div',id="Wrapper3")[0]          
soup2=soup1.find_all('a') 
file1=open('undergradresults.txt','w+')
counter=alt[0]
#print "0"
v=0;
m=[]
k=[]
myalt=alt[1]
condi=0;
for i in soup2:
     v=v+1;
     link=i["href"]
     if v<4:
         continue
     title="".join([str(j) for j in i.contents])
     
     if title == alt[1]:
         cursor2.execute("""update undergradcounters set undergradtitle=%s""",(titlef,))
         break 
     m.append(link)
     k.append(title)
     titlef=title
if myalt == alt[1]:
     condi=1;
while len(m) !=0:
     r=m.pop()
     p=k.pop()
     sql="""insert into undergradresults(id,title,linkf) values(NULL,'%s','%s')"""%(p,r)
     cursor2.execute(sql)
     if condi == 1:
         cursor2.execute("""update undergradcounters set undergradtitle=%s""",(p,))
     counter=counter+1
     
file1.close()
db.commit()
cursor2.close()
#cursor3.close()
db.close()
