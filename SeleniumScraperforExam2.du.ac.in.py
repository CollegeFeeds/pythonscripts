import os
from pyvirtualdisplay import Display
from selenium import webdriver as wb
import time
def create_ch_driver():
  chrome_options = wb.ChromeOptions()
  chrome_options.add_argument("--no-sandbox")
  return wb.Chrome("/usr/local/bin/chromedriver", chrome_options=chrome_options)
#pathtochromedriver = '/Users/nipunarora/Desktop/django/webscraper&djangostart/seleniumscraper/chromedriver'### path to chromedriver Nipuns laptop
 ##ubuntu chromedriver path
################## A Virtual Display for VPS #########################
display = Display(visible=0, size=(800, 600))
display.start()
print "Display Started"
driver =  create_ch_driver()
print "driver executed"
driver.get('http://duexam2.du.ac.in/RSLT_ND2016/Students/List_Of_Declared_Results.aspx')
a=driver.find_element_by_id("gvshow_ata_glance_ctl05_btn_show_details")
a.click()
print "Clicked"
time.sleep(20)
current_page_source=open("Pagesource1.html","a+")
current_page_source.write(driver.page_source.encode('utf-8'))
current_page_source.close()
print "Completed Successfully"
driver.quit()
display.stop()