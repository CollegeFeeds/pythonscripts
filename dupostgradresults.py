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
soup1=soup.find_all('article',id="contents")[2]          
soup2=soup1.find_all('a') 
file1=open('postgradresults.txt','w+')
counter=alt[0]
#print "0"
for i in soup2:
     link=i["href"]
     title=i["title"]
     #print "1"
     if title == alt[1]:
        cursor2.execute("""update postgradcounter set postgradtitle=%s""",(titlef,))
        cursor2.execute("""update postgradcounter set postgradid=%d""",(counter))
        break
     titlef=title
     #print "2"
     src2=requests.get(link).text
     soup3=bs(src2,"html.parser")
     soup4=soup3.find_all("div",class_="content-inner grid_12")[1].find_all("a")[0]
     linkf=soup4["href"]
     sql="""insert into postgradresults(id,title,linkf) values(NULL,'%s','%s')"""%(title,linkf)
     cursor2.execute(sql)
     file1.write('\nhttp://www.du.ac.in/du/%s'%linkf)
     #print "3"
     counter=counter+1
     
file1.close()
db.commit()
cursor2.close()
#cursor3.close()
db.close()
