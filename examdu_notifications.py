import requests
from bs4 import BeautifulSoup as bs
import MySQLdb
#db=MySQLdb.connect("localhost","root","icancode23","dufeed")
#cursor2=db.cursor()
last_notification="Notification dated 13.03.2012 regarding the charges for issue of transcript of marks &amp; various other certificates"
src=requests.get("http://exam.du.ac.in/notifications.html").text
soup=bs(src,"html.parser")
j=15     
soup1=soup.find_all('a')
soup2=soup1[15]
updated_new_last_notification=soup2
print soup2
print len(soup1)
while soup2!=last_notification and j<len(soup1):
	link=soup2["href"]
	name=soup2.decode_contents(formatter="html")
	print name
	print "\n"
	j=j+1
	soup2=soup1[j]