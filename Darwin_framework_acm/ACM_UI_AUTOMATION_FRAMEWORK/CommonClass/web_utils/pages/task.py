from selenium.webdriver.common.by import By
import time,os
import allure
import moment
from utils import utils as utils

class HomePage():
    def __init__(self,driver):
        self.driver = driver

        self.notification_link_xpath = '//div[@class="image-gt-icon-notification h-2x w-2x"]'
        self.notification_close_xpath = '//*[@class="icon-gt-close text-2 text-regular"]'
        self.logout_xpath ='//*[@class="image-gt-icon-logout w-2x h-2x"]'

    def click_notification(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.notification_link_xpath).clear
        self.driver.find_element(By.XPATH,self.notification_link_xpath).click()
        screenshot_name=f'{utils.whoami()}_{moment.now().strftime("%y-%m-%d_%H-%M-%S")}'
        allure.attach(self.driver.get_screenshot_as_png(),name=screenshot_name,attachment_type=allure.attachment_type.PNG)
        self.driver.get_screenshot_as_file('D:/web_automation/sample_automation_test/screenshots/'+screenshot_name+'.png')
        time.sleep(5)
        self.driver.find_element(By.XPATH,self.notification_close_xpath).clear
        self.driver.find_element(By.XPATH,self.notification_close_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH,self.logout_xpath).clear
        self.driver.find_element(By.XPATH,self.logout_xpath).click()