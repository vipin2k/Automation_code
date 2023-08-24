# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager

from CommonClass.web_utils.CommonActions import send_keys, click


class LoginPage():
    def __init__(self, uiTestData):
        self.uiTestData = uiTestData
        self.user_name_text_box_xpath = '//*[@name="loginForm:userName"]'
        self.password_text_box_xpath = "//*[@name='loginForm:clientSecret']"



        self.user_name_text_box_xpath_6 = "//input[@name='loginForm:userName']"
        self.password_text_box_xpath_6 = "//input[@type='password']"
        self.submit_button_xpath = "//*[@class='ui-button-text ui-c']"

    def enter_username(self):
        # self.driver.find_element(By.XPATH, self.user_name_text_box_xpath).clear
        send_keys(self.user_name_text_box_xpath, self.uiTestData["username"])

    def enter_password(self):
        # self.driver.find_element(By.XPATH, self.password_text_box_xpath).clear
        send_keys(self.password_text_box_xpath, self.uiTestData["password"])


    def enter_username_6(self):
        # self.driver.find_element(By.XPATH, self.user_name_text_box_xpath).clear
        send_keys(self.user_name_text_box_xpath_6, self.uiTestData["username_6"])


    def enter_password_6(self):
        # self.driver.find_element(By.XPATH, self.password_text_box_xpath).clear
        send_keys(self.password_text_box_xpath_6, self.uiTestData["password_6"])

    def click_login(self):
        click(self.submit_button_xpath)




