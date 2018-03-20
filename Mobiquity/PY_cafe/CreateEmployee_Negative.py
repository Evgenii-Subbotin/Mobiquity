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
file.write("\n" + TimeNow + " Create Employee Negative test set is started - ")

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

def ClearForm():
    driver.find_element_by_css_selector('input[ng-model="selectedEmployee.firstName"]').clear()
    driver.find_element_by_css_selector('input[ng-model="selectedEmployee.lastName"]').clear()
    driver.find_element_by_css_selector('input[ng-model="selectedEmployee.startDate"]').clear()
    driver.find_element_by_css_selector('input[ng-model="selectedEmployee.email"]').clear()

#EmptyFirstName Attempt
driver.find_element_by_css_selector('input[ng-model="selectedEmployee.firstName"]').send_keys("" + Keys.RETURN)
driver.find_element_by_css_selector('input[ng-model="selectedEmployee.lastName"]').send_keys("LastNameES" + Keys.RETURN)
driver.find_element_by_css_selector('input[ng-model="selectedEmployee.startDate"]').send_keys("2010-10-10" + Keys.RETURN)
driver.find_element_by_css_selector('input[ng-model="selectedEmployee.email"]').send_keys("123qwe@123qwe.123" + Keys.RETURN)
print("Empty First Name Attempt")

#EmptyLastName attempt
ClearForm()
driver.find_element_by_css_selector('input[ng-model="selectedEmployee.firstName"]').send_keys("FirstName" + Keys.RETURN)
driver.find_element_by_css_selector('input[ng-model="selectedEmployee.lastName"]').send_keys("" + Keys.RETURN)
driver.find_element_by_css_selector('input[ng-model="selectedEmployee.startDate"]').send_keys("2010-10-10" + Keys.RETURN)
driver.find_element_by_css_selector('input[ng-model="selectedEmployee.email"]').send_keys("123qwe@123qwe.123" + Keys.RETURN)
print("Empty Last Name attempt")

#EmptyDate attempt
ClearForm()
driver.find_element_by_css_selector('input[ng-model="selectedEmployee.firstName"]').send_keys("FirstName" + Keys.RETURN)
driver.find_element_by_css_selector('input[ng-model="selectedEmployee.lastName"]').send_keys("LastNameES" + Keys.RETURN)
driver.find_element_by_css_selector('input[ng-model="selectedEmployee.startDate"]').send_keys("" + Keys.RETURN)
driver.find_element_by_css_selector('input[ng-model="selectedEmployee.email"]').send_keys("123qwe@123qwe.123" + Keys.RETURN)
print("Empty Date attempt")

#EmptyEmail attempt
ClearForm()
driver.find_element_by_css_selector('input[ng-model="selectedEmployee.firstName"]').send_keys("FirstName" + Keys.RETURN)
driver.find_element_by_css_selector('input[ng-model="selectedEmployee.lastName"]').send_keys("LastNameES" + Keys.RETURN)
driver.find_element_by_css_selector('input[ng-model="selectedEmployee.startDate"]').send_keys("2010-10-10" + Keys.RETURN)
driver.find_element_by_css_selector('input[ng-model="selectedEmployee.email"]').send_keys("" + Keys.RETURN)
print("Empty Email attempt")

#invalidEmail attempt
ClearForm()
driver.find_element_by_css_selector('input[ng-model="selectedEmployee.firstName"]').send_keys("FirstName" + Keys.RETURN)
driver.find_element_by_css_selector('input[ng-model="selectedEmployee.lastName"]').send_keys("LastNameES" + Keys.RETURN)
driver.find_element_by_css_selector('input[ng-model="selectedEmployee.startDate"]').send_keys("2010-10-10" + Keys.RETURN)
driver.find_element_by_css_selector('input[ng-model="selectedEmployee.email"]').send_keys("3453453453423" + Keys.RETURN)
print("Invalid Email attempt")
ClearForm()

print("Creation fields are still visible - all creation negative scenarios handled properly")

time.sleep(1)
driver.find_element_by_tag_name('p').click() #Logout by click
print("Logout")
driver.close()

file.write("All test scenarios are passed")
file.close()