from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pytest
import allure
# import moment
# from pages.loginPage import LoginPage
from CommonClass.web_utils.pages.loginPage import LoginPage
# from pages.homePage import HomePage
import os
from CommonClass.web_utils.pages.member import Member
from CommonClass.web_utils.pages.request import Request
from CommonClass.web_utils.pages.task import Task


def login(uiTestData):
    driver=os.getenv("driver")
    driver.get(uiTestData["url"])
    time.sleep(5)
    login = LoginPage(driver)
    login.enter_username(uiTestData["username"])
    login.enter_password(uiTestData["password"])
    # screenshot_name=f'{utils.whoami()}_{moment.now().strftime("%y-%m-%d_%H-%M-%S")}'
    # allure.attach(driver.get_screenshot_as_png(),name=screenshot_name,attachment_type=allure.attachment_type.PNG)
    # driver.get_screenshot_as_file('D:/web_automation/sample_automation_test/screenshots/'+screenshot_name+'.png')
    time.sleep(5)
    login.click_login()
    time.sleep(5)
# def notification():
#     driver=os.getenv("driver")
#     home=HomePage(driver)
#     home.click_notification()
#     time.sleep(3)

# def logout():
#     driver=os.getenv("driver")
#     home=HomePage(driver)
#     home.click_logout
#     # screenshot_name=f'{utils.whoami()}_{moment.now().strftime("%y-%m-%d_%H-%M-%S")}'
#     # allure.attach(driver.get_screenshot_as_png(),name=screenshot_name,attachment_type=allure.attachment_type.PNG)
#     # driver.get_screenshot_as_file('D:/web_automation/sample_automation_test/screenshots/'+screenshot_name+'.png')

def login_web(uiTestData, driver):
    mem = Member(driver)
    print(driver)
    print(uiTestData)
    Member.create_Member(driver)


def login_request(uiTestData, driver):
    req = Request(driver)
    # print(driver)
    # print(uiTestData)
    Request.create_Request(driver)


def login_task(uiTestData, driver):
    new_task = Task(driver)
    Task.create_Task(driver)

