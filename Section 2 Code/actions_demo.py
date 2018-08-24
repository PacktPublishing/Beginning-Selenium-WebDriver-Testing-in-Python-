from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome('./chromedriver')
driver.get('https://google.com')

# locate the search box element
search_box = driver.find_element_by_name('q')
import time
time.sleep(5)

# type in our search query into the search box
search_box.send_keys('seleniumhq' + Keys.RETURN)

time.sleep(10)
print(driver.title)

driver.quit()
