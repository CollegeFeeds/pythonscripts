import requests
from bs4 import BeautifulSoup as bs
import MySQLdb
db=MySQLdb.connect("localhost","root","plutonian","test1")
cursor2=db.cursor()
#cursor3=db.cursor()
cmd="""select * from srcccounter"""
cursor2.execute(cmd)
alt=cursor2.fetchone()
db.commit()
titlef=alt[1]
src=requests.get("http://www.srcc.edu/announcements").text
soup=bs(src,"html.parser")
soup1=soup.find_all('div',class_="year")[0]          
soup2=soup1.find_all('a') 
file1=open('srccnotices.txt','w+')
counter=alt[0]
#print "0"
for i in soup2:
     link=i["href"]
     #title=i["title"]
     #print "1"
     if title==alt[1]:
         cursor2.execute("""update srcccounter set srcctitle=%s""",(titlef,))
         cursor2.execute("""update srcccounter set srccid=%d""",(counter))
         break
     titlef=title
     sql="""insert into srccnotices(id,title,linkf) values(NULL,'%s','%s')"""%(title,link)
     cursor2.execute(sql)
     file1.write('\n%s'%link)
     #print "3"
     counter=counter+1
     
file1.close()
db.commit()
cursor2.close()
#cursor3.close()
db.close()
