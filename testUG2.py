import requests
from bs4 import BeautifulSoup as bs
import MySQLdb
db=MySQLdb.connect("localhost","root","plutonian","test1")
cursor2=db.cursor()
#cursor3=db.cursor()
cmd="""select * from undergradcounters"""
cursor2.execute(cmd)
print "rundi"
alt=cursor2.fetchone()
db.commit()
titlef=alt[1]
k=[]
m=[]
src=requests.get("http://192.168.1.3:80/test.htm").text
print "hai"
soup=bs(src,"html.parser")
soup1=soup.find_all('div',class_="block")[1]          
soup2=soup1.find_all('a') 
file1=open('undergradresults.txt','w+')
counter=alt[0]
r=0
wpow=0
print "mera"
for i in soup2:
     link=i["href"]
     title=i["title"]
     print "1"
     if r==0:
        r=r+1
        titleff=title
     if title == alt[1]:
        break
     titlef=title
     print "pc"
     k.append(title)
     m.append(link)
     print wpow
     wpow=wpow+1
cursor2.execute("""update undergradcounters set undergradtitle=%s""",(titleff,))
while len(m) !=0:
     a=m.pop()
     print a
     src2=requests.get(a).text
     soup3=bs(src2,"html.parser")
     soup4=soup3.find_all("div",class_="content-inner grid_12")[1].find_all("a")[0]
     linkf=soup4["href"]
     sql="""insert into undergradresults(id,title,linkf) values(NULL,'%s','%s')"""%(k.pop(),linkf)
     cursor2.execute(sql)
     print "Done"
     #file1.write('\nhttp://www.du.ac.in/du/%s'%linkf)
     #print "3"
     counter=counter+1
     
file1.close()
db.commit()
cursor2.close()
#cursor3.close()
db.close()
