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
sql_query="""ALTER TABLE api_headlines AUTO_INCREMENT = 1"""
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
headline_links=[]
image_links=[]
###################### soup2 contains all the anchor tags that contain the main headline"###################
for headline in soup2:
	# print "The title for the headline is: ",headline['title']
	# print "The link is ",headline['href']
	try:
		print headline['title']
		headline_links.append(headline['href'].encode('utf-8'))
		sql_query="""INSERT INTO api_headlines(id,title,linkf,imagelink) VALUES(NULL,'%s','%s','null')"""%(headline['title'].encode('utf-8'),headline['href'].encode('utf-8'))
		#print sql_query
		cursor.execute(sql_query)

	except Exception as e:
		print "Database Exception :",e
i=0
for link in headline_links:
	a=requests.get(link)
	soupa=bs(a.text,"html.parser")
	imgsrc=soupa.find_all('div',class_="single_post_format_image")[0].find_all('img')[0]['src'].encode('utf-8')
	image_links.append(imgsrc)
	sql_query="""UPDATE api_headlines SET imagelink='%s' WHERE linkf='%s' """%(imgsrc,link)
	print sql_query
	cursor.execute(sql_query)
	db.commit()
	i=i+1
	print i

print image_links



db.commit()
db.close()


