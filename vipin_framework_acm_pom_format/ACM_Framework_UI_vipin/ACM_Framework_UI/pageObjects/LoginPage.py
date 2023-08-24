from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    textbox_username_xpath = "//*[@name='loginForm:userName']"
    textbox_password_xpath = "//*[@name='loginForm:password']"
    button_login_xpath = "//span[text()='Log in']"
    button_welcome_id = "commandBarForm:masterCommandMenuButton"
    button_logout_xpath = "//span[text()='Log Out']"

    def __init__(self, driver):
        self.driver = driver


    def setUserName(self, username):
        # self.driver.find_element(By.XPATH, self.textbox_username_xpath).clear
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(username)

    def setPassword(self, password):
        # self.driver.find_element(By.XPATH, self.textbox_password_xpath).clear
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickWelcome(self):
        self.driver.find_element(By.ID, self.button_welcome_id).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.button_logout_xpath).click()







