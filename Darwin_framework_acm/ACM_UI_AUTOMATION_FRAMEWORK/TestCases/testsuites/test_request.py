import time
import ast
from CommonClass.web_utils.pages.request import Request
import pytest
from CommonClass.api_utils.AuthToken import getCurrentSessionToken
from CommonClass.web_utils.CommonActions import *
# from CommonClass.web_utils.CommonActions import Request
from CommonClass.web_utils.pages.loginPage import LoginPage
from CommonClass.web_utils.pages.member import (Member)
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# @pytest.mark.usefixtures("test_setup")
class TestSample2():
    def test_sample_ui_test_case(self,uiTestData, configLogger):
        # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # driver.maximize_window()
        # driver = self.driver
        # driver.get(uiTestData["url_11"])
        get(uiTestData["url_11"])
        time.sleep(5)
        login = LoginPage(uiTestData)
        login.enter_username()
        time.sleep(2)
        login.enter_password()
        time.sleep(5)
        login.click_login()
        time.sleep(5)


    def test_sample_request(self,uiTestData, configLogger):
        # driver = self.driver
        req = Request(uiTestData)
        req.create_Request()
