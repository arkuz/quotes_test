from selenium import webdriver
from selenium.webdriver.common.by import By


class MainPage(object):
    driver: webdriver
    driver = None

    def __init__(self, driver):
        self.driver = driver
        self.driver.get('http://tereshkova.test.kavichki.com')
        print('Home page opened')

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_element(*locator)

