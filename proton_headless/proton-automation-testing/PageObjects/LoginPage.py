from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    textbox_username_id = "//*[@placeholder='Email']"
    textbox_password_id = "//*[@id='password']"
    button_login_id = "//*[@type='submit']"
    button_click = "//*[@class='dropdown-toggle nav-link ng-star-inserted']"
    button_logout_id = "//*[@class='feather feather-log-out icon-dual icon-xs mr-2']"
    button_click_date_in_overview = "(//*[@aria-haspopup='listbox'])[2]"
    button_click_today_date_in_overview = "//*[@aria-label='Today']"
    button_click_score_card_page = "//span[text()='Score Card']"
    button_click_screencast_page = "//span[text()='Screen Cast']"
    button_click_Reports_page = "//span[text()='Reports']"
    button_click_Activity_summary_page = "//*[@id='dropOpen']/li[2]/a/div"
    button_click_Timeline_page = "//*[@id='dropOpen']/li[3]/a/div"
    button_click_Attendances_page = "//*[@id='dropOpen']/li[4]/a/div"
    button_click_Apps_and_Webs_page = "//*[@id='dropOpen']/li[5]/a/div"

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        self.driver.find_element(By.XPATH, self.textbox_username_id).clear()
        self.driver.find_element(By.XPATH, self.textbox_username_id).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_id).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.button_login_id).click()

    def click_date_in_overview(self):
        self.driver.find_element(By.XPATH, self.button_click_date_in_overview).click()

    def click_Today_date_in_overview(self):
        self.driver.find_element(By.XPATH, self.button_click_today_date_in_overview).click()

    def click_userprofile(self):
        self.driver.find_element(By.XPATH, self.button_click).click()

    def click_score_card_page(self):
        self.driver.find_element(By.XPATH, self.button_click_score_card_page).click()

    def click_screencast_page(self):
        self.driver.find_element(By.XPATH, self.button_click_screencast_page).click()

    def click_Reports_page(self):
        self.driver.find_element(By.XPATH, self.button_click_Reports_page).click()

    def click_Activity_summary_page(self):
        self.driver.find_element(By.XPATH, self.button_click_Activity_summary_page).click()

    def click_Timeline_page(self):
        self.driver.find_element(By.XPATH, self.button_click_Timeline_page).click()

    def click_Attendances_page(self):
        self.driver.find_element(By.XPATH, self.button_click_Attendances_page).click()

    def click_Apps_and_Webs_page(self):
        self.driver.find_element(By.XPATH, self.button_click_Apps_and_Webs_page).click()

    # def click_Activity_summary_page(self):
    #     self.driver.find_element(By.XPATH, self.button_click_Activity_summary_page).click()
    #
    # def click_Activity_summary_page(self):
    #     self.driver.find_element(By.XPATH, self.button_click_Activity_summary_page).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.button_logout_id).click()
