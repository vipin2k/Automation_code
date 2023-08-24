import time
import ast
import pytest
from CommonClass.web_utils.CommonActions import get
from CommonClass.web_utils.pages.loginPage import LoginPage
from CommonClass.web_utils.CommonActions import *
from CommonClass.web_utils.pages.member import (Member)


@pytest.mark.usefixtures("test_setup")
class TestSample1():
    def test_sample_ui_test_case(self,uiTestData, configLogger):
        get(uiTestData["url_11"])
        time.sleep(5)
        login = LoginPage(uiTestData)
        login.enter_username()
        time.sleep(2)
        login.enter_password()
        time.sleep(5)
        login.click_login()
        time.sleep(5)

    def test_member_sample(self, uiTestData, configLogger):
        mem = Member(uiTestData)
        mem.create_Member()
