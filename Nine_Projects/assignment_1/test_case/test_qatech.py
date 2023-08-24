import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import selenium
import pytest


f = open("test_qa.json")
data = json.load(f)
f.close()
driver = webdriver.Firefox()
driver.maximize_window()
driver.get(data["qa_url"])
# driver.implicitly_wait(5)


def test_qa():
    a = driver.title
    time.sleep(2)
    print(a)
    if a == "QA Automation Tools Trainings and Tutorials | QA Tech Hub":
        print("Same")
    else:
        print("Not same")


def test_facebook():
    driver.get(data["fb_url"])
    print(driver.title)
    time.sleep(2)
    driver.back()
    driver.forward()
    time.sleep(1)
    driver.refresh()
    time.sleep(1)
    print("Test completed")
    driver.close()
    driver.quit()

