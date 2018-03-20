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
file.write("\n" + TimeNow + " Login-Logout test set is started - ")

#open test page
driver.get("http://cafetownsend-angular-rails.herokuapp.com")
print("Page is found")

#credential at login form
Username = "Luke"
driver.find_element_by_xpath('id("login-form")/fieldset[1]/label[1]/input[@class="ng-pristine ng-invalid ng-invalid-required"]').send_keys(Username + Keys.RETURN)
driver.find_element_by_xpath('id("login-form")/fieldset[1]/label[2]/input[@class="ng-pristine ng-invalid ng-invalid-required"]').send_keys("Skywalker" + Keys.RETURN)
print(Username + " Skywalker is used as login credentials")

#Verify that user in hello<user> is equal to currentuser
if (driver.find_element_by_id('greetings').text == "Hello " + Username):
    print("Login is successfull, greetings equal to Username")
else:
    print("Login is failed")

#Logout by click
time.sleep(2)
driver.find_element_by_tag_name('p').click()
print("Logout")
driver.close()

file.write("All test scenarios are passed")
file.close()