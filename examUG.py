import requests
from bs4 import BeautifulSoup as bs
import MySQLdb
db=MySQLdb.connect("localhost","root","plutonian","dufeed")
cursor2=db.cursor()
#cursor3=db.cursor()
cmd="""select * from api_UGexamcounter"""
cursor2.execute(cmd)
alt=cursor2.fetchone()
db.commit()
titlef=alt[1]
src=requests.get("http://exam.du.ac.in/UG-exam.html").text
soup=bs(src,"html.parser")
soup1=soup.find_all('div',id="Wrapper3")[0]          
soup2=soup1.find_all('a') 
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
        cursor2.execute("""update api_UGexamcounter set title=%s""",(titlef,))
        break
     titlef=title
     m.append(link)
     k.append(title)
if myalt == alt[1]:
     condi=1;
while len(m) !=0:
     r=m.pop()
     p=k.pop()
     sql="""insert into api_UGexamschedule(id,title,linkf) values('%ld','%s','%s')"""%(counter,p,r)
     cursor2.execute(sql)
     if condi == 1:     
         cursor2.execute("""update api_UGexamcounter set title=%s""",(p,))
     #print "3"
     counter=counter+1
counter=counter-1
sql="""update api_UGexamcounter set counter='%ld' """%(counter)  
cursor2.execute(sql) 
db.commit()
cursor2.close()
#cursor3.close()
db.close()