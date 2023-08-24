from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import pytest
import unittest

add = []
add1 = []
listssss = []

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.gcitsolutions.com/gold-coast-it-solutions/")
        self.driver.implicitly_wait(10)

    def test_try(self):
        self.driver.find_element(By.XPATH, "//*[@class='menu']").click()
        time.sleep(2)
        lists = self.driver.find_elements(By.XPATH, "//*[@class='menu-list']")
        for i in lists:
            add.append(i.text)
        a = add[0].split("\n")
        print(type(a))
        print("Test 1 pass")


    def test_login(self):
        global b
        self.driver.find_element(By.XPATH, "//*[@class='menu']").click()
        time.sleep(3)
        store = self.driver.find_elements(By.XPATH, "//*[@class='menu-list']")
        for j in store:
            add1.append(j.text)
        b = add1[0].split("\n")
        print(type(b))
        print("Test 2 pass")


    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("logout successfully")
