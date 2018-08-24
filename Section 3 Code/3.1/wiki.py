from selenium import webdriver
from locators import WikipediaHomepage
import time

driver = webdriver.Chrome('./chromedriver')
driver.get('https://en.wikipedia.org')

random_link = driver.find_element(*WikipediaHomepage.Random_Link)
random_link.click()

time.sleep(5)

print(driver.title)

driver.quit()
