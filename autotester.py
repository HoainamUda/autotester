from lib2to3.pgen2 import driver
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.set_window_size(1080, 1080)
driver.get('https://my.uda.edu.vn/sv/svlogin')

driver.find_element_by_id("User").send_keys("47077") #Id của bạn
driver.save_screenshot('nhapid.png')

time.sleep(2)

driver.find_element_by_id("Password").send_keys("25/06/2001") #Password
driver.save_screenshot('passw.png')

time.sleep(2)

driver.find_element_by_id("Lnew1").click()
driver.save_screenshot('login.png')

time.sleep(2)

driver.find_element_by_class_name("dropdown-toggle").click()
driver.save_screenshot('tkb.png')

time.sleep(2)

driver.execute_async_script('document.querySelector("#form1 > div.navbar.navbar-inverse.navbar-fixed-top > div > div.navbar-collapse.collapse > ul > li.dropdown.open > ul > li:nth-child(2) > a").click()')
driver.save_screenshot('done.png')
