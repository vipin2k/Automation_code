import time
import json
import os
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest



def login(driver, data):
    driver.find_element(By.XPATH, "//input[@placeholder='Email']").send_keys(data["Username"])
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='password']").send_keys(data["Password"])
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@type='submit']").click()
    time.sleep(5)
    print("Login successfully")