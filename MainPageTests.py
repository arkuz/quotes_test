import unittest
from selenium import webdriver
from MainPage import MainPage
from locators import MainPageLocators


class MainPageTests(unittest.TestCase):
    driver: webdriver
    driver = None
    MAIN_PAGE = None

    def setUp(self):
        self.driver = webdriver.Chrome()
        print('Browser started')
        self.driver.maximize_window()
        self.MAIN_PAGE = MainPage(self.driver)

    def tearDown(self):
        self.driver.close()
        print('Browser closed')

    def test_compare_tables_data(self):
        print('hello')
        print(MainPageLocators.LABEL)
        print(type(MainPageLocators.LABEL))
        elem = self.MAIN_PAGE.find_element(MainPageLocators.TABLE)
        print(type(elem))
        print(elem.text)


if __name__ == '__main__':
    unittest.main()