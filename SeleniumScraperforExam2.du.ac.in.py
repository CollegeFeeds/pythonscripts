from selenium import webdriver as wb
import time
pathtochromedriver = '/Users/nipunarora/Desktop/django/webscraper&djangostart/seleniumscraper/chromedriver'
driver = wb.Chrome(executable_path=pathtochromedriver)  
driver.get('http://duexam2.du.ac.in/RSLT_ND2016/Students/List_Of_Declared_Results.aspx')
a=driver.find_element_by_id("gvshow_ata_glance_ctl05_btn_show_details")
a.click()
time.sleep(20)
current_page_source=open("Pagesource.html","a+")
current_page_source.write(driver.page_source.encode('utf-8'))
current_page_source.close()
print "Completed Successfully"