import time
import ast
import pytest
from CommonClass.web_utils.CommonActions import get
from CommonClass.web_utils.pages.create_member import Create_Member
from CommonClass.web_utils.pages.loginPage import LoginPage
from CommonClass.web_utils.CommonActions import *
from CommonClass.web_utils.pages.locators import Locators
from CommonClass.web_utils.pages.member import Member
from CommonClass.web_utils.pages.request import Request


@pytest.mark.usefixtures("test_setup")
class TestSample1():
    def test_sample_ui_test_case(self,uiTestData, configLogger):
        get(uiTestData["url_6"])
        time.sleep(5)
        login = LoginPage(uiTestData)
        login.enter_username_6()
        time.sleep(2)
        login.enter_password_6()
        time.sleep(5)
        login.click_login()
        time.sleep(5)

    # def test_member_sample(self, uiTestData, configLogger):
    #     mem = Member(uiTestData)
    #     mem.create_Member()

    def test_create_member_sample(self, uiTestData, configLogger):
        create = Create_Member(uiTestData)
        create.create_Member_id()

    # def test_request_sample(self,uiTestData, configLogger):
    #     req = Request(uiTestData)
    #     req.create_Request()