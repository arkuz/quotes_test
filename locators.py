from selenium.webdriver.common.by import By


class MainPageLocators(object):

    LABEL = (By.ID, 'header')
    TABLE = (By.XPATH, '//table')
    TR = (By.XPATH, '//table/tbody/tr')
    TD = (By.XPATH, '//table/tbody/tr/td')



