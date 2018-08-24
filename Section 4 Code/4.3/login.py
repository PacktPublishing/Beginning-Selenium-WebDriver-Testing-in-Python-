from selenium import webdriver
from locators import *
import time


driver = webdriver.Chrome('./chromedriver')

# Happy Path - Login Success
driver.get('http://localhost:8000')
username = driver.find_element(*LoginPage.username_field)
password = driver.find_element(*LoginPage.password_field)
submit = driver.find_element(*LoginPage.submit_btn)

username.send_keys('registeredUser')
password.send_keys('1234')
submit.click()

time.sleep(2)

welcome_message = driver.find_element(*LoginPage.message)
print(welcome_message.text)

# Sad Path - Login Fail
driver.get('http://localhost:8000')
username = driver.find_element(*LoginPage.username_field)
password = driver.find_element(*LoginPage.password_field)
submit = driver.find_element(*LoginPage.submit_btn)

username.send_keys('otherUser')
password.send_keys('asdf')
submit.click()

time.sleep(2)

message = driver.find_element(*LoginPage.message)
print(message.text)

create_account_link = driver.find_element(*LoginPage.create_account_link)
create_account_link.click()

time.sleep(2)

header = driver.find_element(*CreateAccountPage.header)
print(header.text)

driver.quit()
