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
file.write("\n" + TimeNow + " Create Employee test set is started - ")

#open test page
driver.get("http://cafetownsend-angular-rails.herokuapp.com")
print("Page is found")

#credential at login form
Username = "Luke"
driver.find_element_by_xpath('id("login-form")/fieldset[1]/label[1]/input[@class="ng-pristine ng-invalid ng-invalid-required"]').send_keys(Username + Keys.RETURN)
driver.find_element_by_xpath('id("login-form")/fieldset[1]/label[2]/input[@class="ng-pristine ng-invalid ng-invalid-required"]').send_keys("Skywalker" + Keys.RETURN)
print(Username + " Skywalker is used as login credentials")

#add user
driver.find_element_by_id('bAdd').click()
print("Add Form is shown")
time.sleep(1)
driver.find_element_by_css_selector( 'input[ng-model="selectedEmployee.firstName"]').send_keys("FirstNameES" + Keys.RETURN)
print("FirstName = FirstNameES")
driver.find_element_by_css_selector( 'input[ng-model="selectedEmployee.lastName"]').send_keys("LastNameES" + Keys.RETURN)
print("LastName = LastNameES")
driver.find_element_by_css_selector( 'input[ng-model="selectedEmployee.startDate"]').send_keys("2010-10-10" + Keys.RETURN)
print("Date = 2010-10-10")
driver.find_element_by_css_selector( 'input[ng-model="selectedEmployee.email"]').send_keys("123qwe@123qwe.123" + Keys.RETURN)
print("Email = 123qwe@123qwe.123")

time.sleep(1)
driver.find_element_by_tag_name('p').click() #Logout by click
print("Logout")
driver.close()

file.write("All test scenarios are passed")
file.close()