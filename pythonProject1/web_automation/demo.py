from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.myntra.com/")
time.sleep(2)

def test_myntra():
    driver.find_element(By.XPATH,"(//*[@class='desktop-main'])[1]").click()
    time.sleep(3)