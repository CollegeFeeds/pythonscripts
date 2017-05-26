import time
from selenium import webdriver
import requests
from bs4 import BeautifulSoup as bs
driver = webdriver.Chrome('/home/harsh/Desktop/chromedriver')
driver.get('http://duexam2.du.ac.in/RSLT_ND2016/Students/List_Of_Declared_Results.aspx')
cbcs1 = driver.find_element_by_xpath('//*[@id="gvshow_ata_glance_ctl02_btn_show_details"]')
cbcs1.click()
time.sleep(100)
driver.quit()