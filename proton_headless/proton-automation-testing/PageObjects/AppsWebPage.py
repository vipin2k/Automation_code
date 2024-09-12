from selenium import webdriver
from selenium.webdriver.common.by import By


class Apps_and_webs_page:
    button_click_apps_page = "//*[@class='mx-2 btn btn-primary' and text()='Apps']"
    button_click_webs_page = "//*[@class='mx-2 btn btn-primary' and text()='Website']"

    def __init__(self, driver):
        self.driver = driver

    def click_apps_page(self):
        self.driver.find_element(By.XPATH, self.button_click_apps_page).click()

    def click_webs_page(self):
        self.driver.find_element(By.XPATH, self.button_click_webs_page).click()
