from selenium import webdriver
from selenium.webdriver.common.by import By


class MemberPage:
    textbox_username_xpath = "//*[@name='loginForm:userName']"
    # textbox_password_xpath = "//*[@name='loginForm:password']"
    textbox_password_xpath = "//*[@type='password']"
    button_login_xpath = "//span[text()='Log in']"
    button_search_id = "//*[@id='commandBarForm:searchButton']"
    button_member_xpath = "//*[@class='ui-menuitem-text' and text() = 'Members']"
    button_create_new_member_xpath = "//*[@class='ui-button-text ui-c' and text() = 'New Member']"
    textbox_first_name_name = "//*[@name='memberDetailIdentificationForm:firstname']"
    textbox_last_name_name = "//*[@name='memberDetailIdentificationForm:lastName']"
    textbox_create_member_id_name = "//*[@name='memberDetailIdentificationForm:memberId']"
    textbox_create_DOB_name = "//*[@name='memberDetailIdentificationForm:birthDate_input']"
    button_Gender_xpath = "(//*[@class='ui-radiobutton-icon ui-icon ui-icon-blank ui-c'])[1]"


    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickSearch(self):
        self.driver.find_element(By.XPATH, self.button_search_id).click()

    def clickMember(self):
        self.driver.find_element(By.XPATH, self.button_member_xpath).click()

    def clickNewMember(self):
        self.driver.find_element(By.XPATH, self.button_create_new_member_xpath).click()

    def setFirstName(self, firstname):
        self.driver.find_element(By.XPATH, self.textbox_first_name_name).send_keys(firstname)

    def setLastName(self, lastname):
        self.driver.find_element(By.XPATH, self.textbox_last_name_name).send_keys(lastname)

    def setMemberId(self, member_id):
        self.driver.find_element(By.XPATH, self.textbox_create_member_id_name).send_keys(member_id)

    def setDob(self, DOB):
        self.driver.find_element(By.XPATH, self.textbox_create_DOB_name).send_keys(DOB)

    def clickGender(self):
        self.driver.find_element(By.XPATH, self.button_Gender_xpath).click()


    # def clickSaveandExit(self):
    #     self.driver.find_element(By.XPATH, self.button_Save_Exit_xpath).click()

