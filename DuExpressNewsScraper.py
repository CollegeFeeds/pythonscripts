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
previous_headlines=[]
# cmd="""select * from api_headlines"""
# cursor.execute(cmd)
# previous_data=cursor.fetchall()
# for headline in previous_data:
# 	previous_headlines.append(headline[1])
# sql_query="""DELETE FROM api_headlines WHERE 1=1"""
# cursor.execute(sql_query)
# db.commit()
# sql_query="""ALTER TABLE api_headlines AUTO_INCREMENT = 1"""
# cursor.execute(sql_query)
# db.commit()
url="http://duexpress.in/category/campus-ki-khabar/"
try:
	src=requests.get(url).text
except Exception as e:
	print "There was an error fetching Html from url"
soup=bs(src,"html.parser")
soup1=soup.find_all('div',class_="td-ss-main-content")[0]
soup2=soup1.find_all('a')
headline_links=[]
currentheadline_titles=[]
image_links=[]
###################### soup2 contains all the anchor tags that contain the main headline"###################
for headline in soup2[5:39:4]:
	# print "The title for the headline is: ",headline['title']
	# print "The link is ",headline['href']
	try:
		currentheadline_titles.append(headline['title'])
		print headline['title']
		headline_links.append(headline['href'].encode('utf-8'))
		#sql_query="""INSERT INTO api_headlines(id,title,linkf,imagelink) VALUES(NULL,'%s','%s','null')"""%(headline['title'].encode('utf-8'),headline['href'].encode('utf-8'))
		#print sql_query
		#cursor.execute(sql_query)

	except Exception as e:
		print "Database Exception :",e

i=0
for link in headline_links:
	i=i+1
	a=requests.get(link)
	soupa=bs(a.text,"html.parser")
	imgsrc=soupa.find_all('div',class_="td-post-featured-image")[0].find_all('img')[0]['src'].encode('utf-8')
	image_links.append(imgsrc)
	print i
# 	sql_query="""UPDATE api_headlines SET imagelink='%s' WHERE linkf='%s' """%(imgsrc,link)
# 	cursor.execute(sql_query)
# 	db.commit()
# ######################### DEBUG PRINTS #######################
# print "The previous headlines are",previous_headlines
# print "The current headlines are",currentheadline_titles
 ####################### Check Whether to update banners and then publish the status#######
# if set(previous_headlines).issubset(set(currentheadline_titles)):
# 	if set(previous_headlines)==set(currentheadline_titles):
#  		pass
#  	else:
#  		########## Notify all app users that there are some changes #######################
#  		pass
print image_links
print "the headline links are",headline_links
db.commit()
db.close()


