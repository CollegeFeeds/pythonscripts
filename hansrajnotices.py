import requests
from bs4 import BeautifulSoup as bs
import MySQLdb
db=MySQLdb.connect("localhost","root","plutonian","test1")
cursor2=db.cursor()
#cursor3=db.cursor()
cmd="""select * from hansrajcounter"""
cursor2.execute(cmd)
alt=cursor2.fetchone()
db.commit()
titlef=alt[1]
src=requests.get("http://www.hansrajcollege.co.in/news.php").text
soup=bs(src,"html.parser")
soup1=soup.find_all('div',class_="urbanmenu")[0]          
soup2=soup1.find_all('a') 
file1=open('hansrajnotices.txt','w+')
counter=alt[0]
#print "0"
for i in soup2:
     link=i["href"]
     #title=i["title"]
     #print "1"
     if title==alt[1]:
         cursor2.execute("""update hansrajcounter set hansrajtitle=%s""",(titlef,))
         cursor2.execute("""update hansrajcounter set hansrajid=%d""",(counter))
         break
     titlef=title
     sql="""insert into hansrajnotices(id,title,linkf) values(NULL,'%s','%s')"""%(title,link)
     cursor2.execute(sql)
     file1.write('\n%s'%link)
     #print "3"
     counter=counter+1
     
file1.close()
db.commit()
cursor2.close()
#cursor3.close()
db.close()
