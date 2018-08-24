import time
from selenium import webdriver

driver = webdriver.Chrome('/Users/t33kt33k/Downloads/chromedriver')
driver.get('https://www.seleniumhq.org')

print(driver.title)

time.sleep(20)
driver.quit()
