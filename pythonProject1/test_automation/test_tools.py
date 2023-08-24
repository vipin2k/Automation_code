from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import time
import pytest

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/")


def test_forms():
    driver.find_element(By.XPATH, "//*[@class='card mt-4 top-card'][2]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//span[text()='Practice Form']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='firstName']").send_keys("santha")
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='lastName']").send_keys("kumar")
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='userEmail']").send_keys("santhakumar08@gmail.com")
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[text()='Male']").click()
    driver.find_element(By.XPATH, "//*[@id='userNumber']").send_keys("6564158154")
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='dateOfBirthInput']").click()
    driver.find_element(By.XPATH, "//option[text()='August']/../option[8]").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//option[text()='2000']/../option[101]").click()
    time.sleep(2)
    driver.find_element(By.XPATH,
                        "//*[@class='react-datepicker__day react-datepicker__day--008']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@class='custom-control-label' and text() = 'Music']").click()
    driver.find_element(By.XPATH, "//*[@id='currentAddress']").send_keys("no:14/50 bharathi nagar 3rd opp sharma nagar vyasarpadi")
    time.sleep(2)
