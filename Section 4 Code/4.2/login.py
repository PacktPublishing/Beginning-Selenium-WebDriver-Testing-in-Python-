from selenium import webdriver
import time


driver = webdriver.Chrome('./chromedriver')

# Happy Path - Login Success
driver.get('http://localhost:8000')
username = driver.find_element('username')
password = driver.find_element('password')
submit = driver.find_element('submit')

username.send_keys('registeredUser')
password.send_keys('1234')
submit.click()

time.sleep(2)

welcome_message = driver.find_element('welcome_message')
print(welcome_message)

# Sad Path - Login Fail
driver.get('http://localhost:8000')
username = driver.find_element('username')
password = driver.find_element('password')
submit = driver.find_element('submit')

username.send_keys('otherUser')
password.send_keys('asdf')
submit.click()

time.sleep(2)

message = driver.find_element('welcome_message')
print(welcome_message)

create_account_link = driver.find('create_account')
create_account_link.click()

time.sleep(2)

header = driver.find_element('header')
print(header)

