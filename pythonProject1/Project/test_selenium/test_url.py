from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
import json

f = open('testdata.json')
data = json.load(f)
f.close()

add = []
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(data['url'])
# driver.implicitly_wait(10)


def test_lnk():
    driver.find_element(By.XPATH, "//*[@class='menu']").click()
    time.sleep(3)
    links = driver.find_elements(By.XPATH, "(//*[@class='social so-slide']//*[@target='_blank'])")
    for link in links:
        add.append(link.get_attribute('href'))
    print(add)


def test_new_window():
    driver.switch_to.new_window()
    time.sleep(2)
    for i in range(3):
        try:
            driver.get(add[i])
            driver.switch_to.new_window()
            time.sleep(2)
            print("click in successfully", add[i])

        except:
            driver.get_screenshot_as_file("screenshot/screen3.png")
            print("An exception error occurred ", add[i])




