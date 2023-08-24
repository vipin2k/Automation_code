from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.common.action_chains import ActionChains
import time
import json
import selenium


f = open("test_flip.json")
data = json.load(f)
f.close()
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(data["url"])
time.sleep(6)
driver.implicitly_wait(10)


def test_log():
    # driver.find_element(By.XPATH, "//*[@class='_36HLxm col col-3-5']").click()
    # driver.find_element(By.XPATH, "//*[@class='_1_3w1N']").click()
    # time.sleep(5)
    driver.find_element(By.XPATH, "//*[@class='_2IX_2- VJZDxU']").send_keys(data["Email"])
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@type='password']").send_keys(data["Password"])
    time.sleep(2)
    driver.find_element(By.XPATH, "(//*[@type='submit'])[2]").click()
    print("login successfully")
