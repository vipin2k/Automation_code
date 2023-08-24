from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

add = []
add1 = []
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
# driver.implicitly_wait(5)

def test_login():

    driver.find_element(By.XPATH, "//*[@type='text']").send_keys("standard_user")
    driver.find_element(By.XPATH, "//*[@type='password']").send_keys("secret_sauce")
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@type='submit']").click()
    driver.get_screenshot_as_file("screenshots/screen1.png")
    time.sleep(2)
    print("login done")

def test_logout():
    # driver.find_element(By.XPATH, "//*[@class='product_sort_container')]").click()
    # driver.find_element(By.XPATH, "//option[text()='Name (A to Z)']").click()
    time.sleep(1)
    shirts = driver.find_elements(By.XPATH, "//div[@class='inventory_item_name']")
    for shirt in shirts:
        if shirt.text.startswith("Te") == False:
            add.append(shirt.text)
            driver.find_element(By.XPATH, "//*[@class='btn btn_primary btn_small btn_inventory']").click()
            # driver.find_element(By.XPATH, "//*[@id='add-to-cart-test.allthethings()-t-shirt-(red)']").click()
            time.sleep(1)
    print(add)
    driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']").click()
    time.sleep(1)
    driver.execute_script("windows.scrollBy(0,500)")
    driver.find_element(By.XPATH, "//*[@id='react-burger-menu-btn']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='logout_sidebar_link']").click()
    time.sleep(2)
    driver.get_screenshot_as_file("screenshots/screen2.png")
    print("logout successfully")
