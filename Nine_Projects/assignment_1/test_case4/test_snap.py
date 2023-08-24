from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.common.action_chains import ActionChains
import time
import json
import selenium

f = open("test_snap.json")
data = json.load(f)
f.close()
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(data["url"])
driver.implicitly_wait(15)


def test_try():
    action = ActionChains(driver)
    menu = driver.find_element(By.XPATH, "//*[@class='accountInner']")
    action.click_and_hold(menu).perform()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@class='dropdownAccountNonLoggedIn']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//*[@id='userName']").send_keys(data["Email"])
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@class='btn col-xs-24 btn-large btn-skyblue continueBtn marT20 marB30']").click()
    driver.find_element(By.XPATH, "//*[@id='j_number']").send_keys(data["Mobile_num"])
    driver.find_element(By.XPATH, "//*[@name='j_name']").send_keys(data["Name"])
    driver.find_element(By.XPATH, "//*[@id='j_dob']").clear()
    driver.find_element(By.XPATH, "//*[@id='j_dob']").send_keys(data["DOB"])
    driver.find_element(By.XPATH, "//*[@id='j_password']").send_keys(data["Password"])
    driver.find_element(By.XPATH, "//*[@id='userSignup']").click()
    print("login successfully")
    driver.close()
    driver.quit()
