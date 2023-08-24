from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
import selenium
import pytest


add = []
f = open("test_ebay.json")
data = json.load(f)
f.close()
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(data["url"])
driver.implicitly_wait(15)


def test_try():
    driver.find_element(By.XPATH, "//*[@type='text']").click()
    driver.find_element(By.XPATH, "//*[@type='text']").send_keys("Apple Watches")
    driver.find_element(By.XPATH, "//*[@type='submit']").click()
    driver.find_element(By.XPATH, "//*[@class='gh-sb ']").click()
    driver.find_element(By.XPATH, "//option[text() = ' Consumer Electronics']").click()
    driver.find_element(By.XPATH, "//*[@type='submit']").click()
    print("Electronics click successfully")


def test_lst():
    products = driver.find_elements(By.XPATH, "//*[@class='s-item__title']")

    for product in products:
        add.append(product.text)
    print(add)


def test_separated():
    print("separated the product : ", add[10])