from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
import selenium
import pytest

f = open("test_fb.json")
data = json.load(f)
f.close()
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(data["fb_url"])
driver.implicitly_wait(5)


def test_try():
    browser = driver.current_url
    print(browser)

    if browser == data["facebook_url"]:
        print("redirect")
    else:
        print("no redirect")


def test_fb():
    driver.find_element(By.XPATH, "//*[@class='_42ft _4jy0 _6lti _4jy6 _4jy2 selected _51sy']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@name='firstname']").send_keys("santha")
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@name='lastname']").send_keys("kumar")
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@name='reg_email__']").send_keys("6369953431")
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@name='reg_passwd__']").send_keys("123456789")
    time.sleep(2)
    driver.find_element(By.XPATH, "//option[text()='12']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//option[text()='Dec']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//option[text()='2000']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@class='_58mt' and text()='Male']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@name='websubmit']").click()
    print("fb login successfully ")
    driver.close()
    driver.quit()