import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time



add1 = []
add2 = []
combine = []


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.gcitsolutions.com/gold-coast-it-solutions/")
        self.driver.implicitly_wait(10)

    def test_click_menu1(self):
        global var1
        self.driver.find_element(By.XPATH, "//*[@class='menu']").click()
        time.sleep(2)
        variables = self.driver.find_elements(By.XPATH, "//*[@class='menu-list']")
        for variable in variables:
            add1.append(variable.text)
        var1 = (add1[0].split("\n"))
        print(var1)
        print("Test 1 is passed")

    def test_click_menu2(self):
        self.driver.find_element(By.XPATH, "//*[@class='menu']").click()
        time.sleep(2)
        variables_list = self.driver.find_elements(By.XPATH, "//*[@class='menu-list']")
        for variable in variables_list:
            add2.append(variable.text)
        var2 = (add2[0].split("\n"))
        print(var2)
        print("Test 2 is passed")

        combine = var1 + var2
        print(combine)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Logout Completed")




