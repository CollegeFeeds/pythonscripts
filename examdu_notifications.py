import requests
from bs4 import BeautifulSoup as bs
import MySQLdb
#db=MySQLdb.connect("localhost","root","icancode23","dufeed")
#cursor2=db.cursor()
src=requests.get("http://exam.du.ac.in/notifications.html").text
soup=bs(src,"html.parser")     
soup1=soup.find_all('a')[72] 
print soup1