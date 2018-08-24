from selenium import webdriver


class Browser(object):

    base_url = 'http://localhost:8000'
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option("detach", True)
    driver = webdriver.Chrome('./chromedriver', chrome_options=opts)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def quit(self):
        self.driver.quit()

    def visit(self, location=''):
        url = self.base_url + location
        self.driver.get(url)