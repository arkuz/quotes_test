from selenium import webdriver


class MainPage(object):
    driver: webdriver
    driver = None

    def __init__(self, driver):
        self.driver = driver
        self.driver.get('http://tereshkova.test.kavichki.com')

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




