from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LABEL = (By.ID, 'header')
    TABLE = (By.XPATH, '//table')
    TR = (By.XPATH, '//table/tbody/tr')
    TD = (By.XPATH, 'td')
    ADD_LINK = (By.ID, 'open')
    NAME_EDIT = (By.ID, 'name')
    COUNT_EDIT = (By.ID, 'count')
    COST_EDIT = (By.ID, 'price')
    ADD_BUTTON = (By.ID, 'add')
    DELETE_LINK = (By.XPATH, "//table//a[@class='delete']")
    RESET_LINK = (By.XPATH, "//a[text()='Сбросить']")






