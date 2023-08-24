from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
import selenium
import pytest

value = 12
lst1 = []
lst2 = []
f = open("test_mailcount.json")
data = json.load(f)
f.close()
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(data["url"])
# driver.implicitly_wait(15)


def test_try():
    driver.find_element(By.XPATH, "//*[@id='identifierId']").send_keys(data['name'])
    time.sleep(2)
    driver.find_element(By.XPATH, "(//*[@class='VfPpkd-vQzf8d' and text() = 'Next'])").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//*[@type='password']").send_keys(data['password'])
    time.sleep(3)
    driver.find_element(By.XPATH, "(//*[@class='VfPpkd-vQzf8d' and text() = 'Next'])").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//*[@class='by7 T-I']").click()
    time.sleep(2)
    print("Logged In Successfully")


def test_cnt():
    counts = driver.find_elements(By.XPATH, "//*[@class='ts']")
    for count in counts:
        lst1.append(count.text)
    print("Total number of counts :", lst1[2])


def test_ts():
    # driver.find_element(By.XPATH, "//*[@class='T-I J-J5-Ji amD T-I-awG T-I-ax7 T-I-Js-Gs L3']").click()
    # time.sleep(5)
    names = driver.find_elements(By.XPATH, "//*[@class='bA4']")
    for name in names:
        lst2.append(name.text)
    while ("" in lst2):
        lst2.remove("")
    var1 = lst2[value]
    add = []
    subject = driver.find_elements(By.XPATH, "//*[@class ='bog']")
    for sub in subject:
        add.append(sub.text)
    var2 = add[value]
    print("The values of ", value, "The To name is ", var1, " & The Subject :  ", var2)
    driver.close()
    driver.quit()