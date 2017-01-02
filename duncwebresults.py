import requests
from bs4 import BeautifulSoup as bs
import MySQLdb
db=MySQLdb.connect("localhost","root","plutonian","test1")
cursor2=db.cursor()
#cursor3=db.cursor()
cmd="""select * from ncwebcounters"""
cursor2.execute(cmd)
alt=cursor2.fetchone()
db.commit()
titlef=alt[1]
src=requests.get("http://www.du.ac.in/du/index.php?page=students-welfare").text
soup=bs(src,"html.parser")
soup1=soup.find_all('div',class_="block")[6]          
soup2=soup1.find_all('a') 
file1=open('ncwebresults.txt','w+')
counter=alt[0]
#print "0"
for i in soup2:
     link=i["href"]
     title=i["title"]
     #print "1"
     if title == alt[1]:
        cursor2.execute("""update ncwebcounter set ncwebtitle=%s""",(titlef,))
        cursor2.execute("""update ncwebcounter set ncwebid=%d""",(counter))
        break
     titlef=title
     #print "2"
     linkf=link
     sql="""insert into ncwebresults(id,title,linkf) values(NULL,'%s','%s')"""%(title,linkf)
     cursor2.execute(sql)
     file1.write('\nhttp://www.du.ac.in/du/%s'%linkf)
     #print "3"
     counter=counter+1
     
file1.close()
db.commit()
cursor2.close()
#cursor3.close()
db.close()
