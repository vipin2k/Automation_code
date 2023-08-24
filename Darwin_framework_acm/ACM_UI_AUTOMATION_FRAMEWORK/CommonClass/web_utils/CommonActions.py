from selenium.webdriver.common.by import By
from selenium import webdriver



driver = webdriver.Chrome(executable_path="D:/Users/pvelu/Documents/ACM_UI_Automation/chromedriver_win32/chromedriver.exe")
driver.maximize_window()


def click(xpath):
    return driver.find_element(By.XPATH, xpath).click()


def get(url):
    return driver.get(url)


def maximize_window():
    return driver.maximize_window()


def clear(xpath):
    return driver.find_element(By.XPATH, xpath).clear


def send_keys(xpath, keys):
    return driver.find_element(By.XPATH, xpath).send_keys(keys)
