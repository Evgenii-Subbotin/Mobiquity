import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime

driver = webdriver.Chrome("D:\Mobiquity\chromedriver.exe")

#Define in-test waits
driver.implicitly_wait(10)
driver.set_page_load_timeout(10)
file = open("Report.txt","a")
TimeNow = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
file.write("\n" + TimeNow + " Login Negative test set is started - ")

#open test page
driver.get("http://cafetownsend-angular-rails.herokuapp.com")
print("Page is found")

#credential at login form
driver.find_element_by_xpath('id("login-form")/fieldset[1]/label[1]/input[@class="ng-pristine ng-invalid ng-invalid-required"]').send_keys("Anakin" + Keys.RETURN)
driver.find_element_by_xpath('id("login-form")/fieldset[1]/label[2]/input[@class="ng-pristine ng-invalid ng-invalid-required"]').send_keys("Skywalker" + Keys.RETURN)
print("Anakin Skywalker is used as wrong login credentials")

time.sleep(0.2)
driver.refresh()
driver.find_element_by_xpath('id("login-form")/fieldset[1]/label[1]/input[@class="ng-pristine ng-invalid ng-invalid-required"]').send_keys("Luke" + Keys.RETURN)
driver.find_element_by_xpath('id("login-form")/fieldset[1]/label[2]/input[@class="ng-pristine ng-invalid ng-invalid-required"]').send_keys("Vader" + Keys.RETURN)
print("Luke Vader is used as Wrong login credentials")

time.sleep(0.2)
#Verify that Login button is still visible, means both negative scenarions are handled
if (driver.find_element_by_css_selector('button[type="submit"]').text == "Login"):
     print("Both negative scenarions are handled")

time.sleep(0.2)
driver.close()

file.write("All test scenarios are passed")
file.close()