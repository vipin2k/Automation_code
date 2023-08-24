from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver import ActionChains
import time
import json
import selenium


f = open("test_drop.json")
data = json.load(f)
f.close()
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(data["url"])
driver.implicitly_wait(15)


def test_try():
    action = ActionChains(driver)
    driver.switch_to.frame(driver.find_element(By.XPATH, '//iframe[@class="demo-frame"]'))
    source_element = driver.find_element(By.XPATH, "//*[@id='draggable']")
    time.sleep(2)
    target_element = driver.find_element(By.XPATH, "//*[@id='droppable']")
    time.sleep(1)
    color1 = target_element.value_of_css_property("color")
    print("color", color1)
    action.drag_and_drop(source_element, target_element).perform()
    time.sleep(2)
    color2 = target_element.value_of_css_property("color")
    print("color", color2)
    driver.close()
    driver.quit()
    print("dragged successfully")
    # action.move_to_element(source).click_and_hold().move_to_element(target).release().perform()






