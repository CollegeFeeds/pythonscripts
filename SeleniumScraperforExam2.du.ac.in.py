from pyvirtualdisplay import Display
from selenium import webdriver as wb
import time
#pathtochromedriver = '/Users/nipunarora/Desktop/django/webscraper&djangostart/seleniumscraper/chromedriver'### path to chromedriver Nipuns laptop
pathtochromedriver='/usr/local/share/chromedriver' ##ubuntu chromedriver path
################## A Virtual Display for VPS #########################
display = Display(visible=0, size=(800, 600))
display.start()
driver = wb.Chrome(executable_path=pathtochromedriver)  
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