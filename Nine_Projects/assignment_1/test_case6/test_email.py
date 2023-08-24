from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
import selenium
import pytest


f = open("test_mail.json")
data = json.load(f)
f.close()
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(data["url"])
driver.implicitly_wait(15)


def test_try():
    driver.find_element(By.XPATH, "//*[@id='identifierId']").send_keys(data['name'])
    time.sleep(2)
    driver.find_element(By.XPATH, "(//*[@class='VfPpkd-vQzf8d' and text() = 'Next'])").click()
    time.sleep(6)
    driver.find_element(By.XPATH, "//*[@type='password']").send_keys(data['password'])
    time.sleep(2)
    driver.find_element(By.XPATH, "(//*[@class='VfPpkd-vQzf8d' and text() = 'Next'])").click()
    time.sleep(5)
    print("Logged In Successfully")
    driver.find_element(By.XPATH, "//*[@class='by7 T-I']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//*[@class='T-I T-I-KE L3']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@class='agP aFw']").send_keys(data["To"])
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@name='subjectbox']").send_keys(data["subject"])
    time.sleep(3)
    driver.find_element(By.XPATH, "//*[@class='Am Al editable LW-avf tS-tW']").send_keys(data["content"])
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@class='T-I J-J5-Ji aoO v7 T-I-atl L3']").click()
    print("Mail sent successfully")