######################### This scraper is expected to run once a day#############
import requests
from bs4 import BeautifulSoup as bs
import MySQLdb
db=MySQLdb.connect("localhost","root","icancode23","dufeed",use_unicode=True, charset="utf8")
cursor=db.cursor()
db.set_character_set('utf8')
cursor.execute('SET NAMES utf8;')
cursor.execute('SET CHARACTER SET utf8;')
cursor.execute('SET character_set_connection=utf8;')
sql_query="""DELETE FROM api_headlines WHERE 1=1"""
cursor.execute(sql_query)
db.commit()
url="http://dubeat.com"
try:
	src=requests.get(url).text
except Exception as e:
	print "There was an error fetching Html from url"
soup=bs(src,"html.parser")
soup1=soup.find_all('ul',class_="feature-post-list")[0]
soup2=soup1.find_all('a',class_="feature-image-link")
###################### soup2 contains all the anchor tags that contain the main headline"###################
for headline in soup2:
	# print "The title for the headline is: ",headline['title']
	# print "The link is ",headline['href']
	try:
		sql_query="""INSERT INTO api_headlines(id,title,linkf) VALUES(NULL,'%s','%s')"""%(headline['title'].encode('utf-8'),headline['href'].encode('utf-8'))
		#print sql_query
		cursor.execute(sql_query)

	except Exception as e:
		print "Database Exception :",e


db.commit()
db.close()


