import requests
from bs4 import BeautifulSoup as bs
import MySQLdb
db=MySQLdb.connect("localhost","root","plutonian","test1")
cursor2=db.cursor()
#cursor3=db.cursor()
cmd="""select * from phdcounters"""
cursor2.execute(cmd)
alt=cursor2.fetchone()
db.commit()
titlef=alt[1]
src=requests.get("http://www.du.ac.in/du/index.php?mact=News,cntnt01,detail,0&cntnt01articleid=8016&cntnt01showall=1&cntnt01returnid=83").text
soup=bs(src,"html.parser")
soup1=soup.find_all('div',class_="content-inner.grid_12")[1]          
soup2=soup1.find_all('a') 
file1=open('phdresults.txt','w+')
counter=alt[0]
#print "0"
for i in soup2:
     link=i["href"]
     #title=i["title"]
     #print "1"
     if title == alt[1]:
        cursor2.execute("""update phdcounter set phdtitle=%s""",(titlef,))
        cursor2.execute("""update phdcounter set phdid=%d""",(counter))
        break
     if link==soup2[-1]:
        cursor2.execute("""update phdcounter set phdtitle=%s""",(titlef,))
        cursor2.execute("""update phdcounter set phdid=%d""",(counter))
        break
     titlef=title
     sql="""insert into phdresults(id,title,linkf) values(NULL,'%s','%s')"""%(title,link)
     cursor2.execute(sql)
     file1.write('\n%s'%link)
     #print "3"
     counter=counter+1
     
file1.close()
db.commit()
cursor2.close()
#cursor3.close()
db.close()
