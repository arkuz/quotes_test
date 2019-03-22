import unittest
from unittest import TestCase as asserts
from selenium import webdriver
from pages.MainPage import MainPage
from locators.MainPageLocators import MainPageLocators
from helpers import DB


class MainPageTests(unittest.TestCase):
    maxDiff = None
    driver: webdriver
    driver = None
    con = None
    MAIN_PAGE = None
    url = 'http://tereshkova.test.kavichki.com'

    @classmethod
    def setUpClass(self):
        self.con = DB.init_connection()
        print('Database connected')
        DB.delete_all_from_db(self.con)
        print('Clear table')
        self.driver = webdriver.Chrome()
        print('Browser started')
        self.driver.maximize_window()
        self.MAIN_PAGE = MainPage(self.driver)
        self.MAIN_PAGE.open_url(self.url)

    @classmethod
    def tearDownClass(self):
        self.driver.close()
        print('Browser closed')
        DB.close_connection(self.con)
        print('Database disconnected')

    def test_add_new_row(self): # тест корректен, ошибка в функционале сайта
        # test data set
        goods = 'Ангельская пыль'
        count = '5'
        cost = '20000'
        action = 'Удалить'
        added_row_expected = (goods, count, cost, action)
        # test
        self.fill_form(cost, count, goods)
        self.MAIN_PAGE.find_element(*MainPageLocators.ADD_BUTTON).click()
        added_row_actual = self.get_table_data()[-1]
        asserts().assertTupleEqual(added_row_expected, added_row_actual,
                                   'Error: expected and actual row is not equals')

    def test_delete_last_added_row(self): # тест корректен, ошибка в функционале сайта
        # precondition
        goods = 'Крошки Зевса'
        count = '3'
        cost = '5500'
        action = 'Удалить'
        self.fill_form(cost, count, goods)
        self.MAIN_PAGE.find_element(*MainPageLocators.ADD_BUTTON).click()
        # test
        absent_row = self.get_table_data()[-1]
        current_element = self.MAIN_PAGE.find_elements(*MainPageLocators.DELETE_LINK)[-1]
        current_element.click()
        rows = self.get_table_data()
        asserts().assertNotIn(absent_row, rows, 'Error: deleted row is present in table')

    def test_delete_first_row(self): # тест корректен, ошибка в функционале сайта
        # test
        absent_row = self.get_table_data()[0]
        current_element = self.MAIN_PAGE.find_elements(*MainPageLocators.DELETE_LINK)[0]
        current_element.click()
        rows = self.get_table_data()
        asserts().assertNotIn(absent_row, rows, 'Error: deleted row is present in table')

    def test_reset_form(self): # тест корректен, ошибка в функционале сайта
        expected = {
            'name': '',
            'count': '',
            'cost': ''
        }
        params = ['100500', '78', 'hello']
        self.fill_form(*params)
        self.MAIN_PAGE.find_element(*MainPageLocators.RESET_LINK).click()
        name = self.MAIN_PAGE.find_element(*MainPageLocators.NAME_EDIT).get_attribute('value')
        count = self.MAIN_PAGE.find_element(*MainPageLocators.COUNT_EDIT).get_attribute('value')
        cost = self.MAIN_PAGE.find_element(*MainPageLocators.COST_EDIT).get_attribute('value')
        actual = {
            'name': name,
            'count': count,
            'cost': cost
        }
        asserts().assertDictEqual(expected, actual,
                                  'Error: name, count, cost edits is not empty')

    def test_compare_tables_data(self):
        # copy all records in DB
        rows = self.get_table_data()
        DB.copy_all_in_table(self.con, rows)
        # add new rows in table on GUI
        attempts = 3
        i = 1
        while i <= attempts:
            goods = 'bla-bla-bla ' + str(i)
            count = '5' + str(i)
            cost = '20' + str(i)
            self.fill_form(cost, count, goods)
            self.MAIN_PAGE.find_element(*MainPageLocators.ADD_BUTTON).click()
            i = i + 1
        rows_db = DB.select_all_from_db(self.con)
        rows_table = self.get_table_data()
        asserts().assertGreater(len(rows_table), len(rows_db), 'Error: count rows in DB > count rows in table')
        set_db = set(rows_db)
        set_table = set(rows_table)
        set_total = set_table - set_db
        print('\nDifferent rows:')
        for row in set_total:
            print(row)

    def fill_form(self, cost, count, goods):
        self.MAIN_PAGE.find_element(*MainPageLocators.ADD_LINK).click()
        self.MAIN_PAGE.find_element(*MainPageLocators.NAME_EDIT).clear()
        self.MAIN_PAGE.find_element(*MainPageLocators.NAME_EDIT).send_keys(goods)
        self.MAIN_PAGE.find_element(*MainPageLocators.COUNT_EDIT).clear()
        self.MAIN_PAGE.find_element(*MainPageLocators.COUNT_EDIT).send_keys(count)
        self.MAIN_PAGE.find_element(*MainPageLocators.COST_EDIT).clear()
        self.MAIN_PAGE.find_element(*MainPageLocators.COST_EDIT).send_keys(cost)

    def get_table_data(self):
        table_data_list = []
        rows = self.MAIN_PAGE.find_elements(*MainPageLocators.TR)
        for row in rows:
            cols = row.find_elements(*MainPageLocators.TD)
            goods = cols[0].text
            count = cols[1].text
            cost = cols[2].text
            action = cols[3].text
            table_data_list.append((goods, count, cost, action))
        return table_data_list

if __name__ == '__main__':
    unittest.main()