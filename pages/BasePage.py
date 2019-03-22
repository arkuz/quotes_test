from selenium import webdriver


class BasePage(object):
    driver: webdriver
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, by, locator):
        return self.driver.find_element(by, locator)

    def find_elements(self, by, locator):
        return self.driver.find_elements(by, locator)

    def click(self):
        self.driver.click()

    def send_keys(self, value):
        self.driver.send_keys(value)

    def clear(self):
        self.driver.clear()




