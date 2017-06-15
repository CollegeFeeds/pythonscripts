import requests
from bs4 import BeautifulSoup as bs
import MySQLdb
db=MySQLdb.connect("localhost","root","icancode23","dufeed")
cursor2=db.cursor()
cmd="""select * from api_notificationcounters"""
cursor2.execute(cmd)
alt=cursor2.fetchone()
db.commit()
last_notification=alt[1]
src=requests.get("http://exam.du.ac.in/notifications.html").text
soup=bs(src,"html.parser")
j=15     
soup1=soup.find_all('a')
soup2=soup1[15]
href=soup2
#print soup2
print type(soup1)
while soup2!=last_notification and j<67:
	link=soup2["href"]
	name=soup2.decode_contents(formatter="html")
	print name
	print "\n"
	j=j+1
	soup2=soup1[j]
    sql="""insert into api_notifications(id,link,title) values(NULL,'%s','%s')"""%(link,name)
    cursor2.execute(sql)
cursor2.execute("""update api_notificationcounters set link=%s""",(href,))
db.commit()
db.close()