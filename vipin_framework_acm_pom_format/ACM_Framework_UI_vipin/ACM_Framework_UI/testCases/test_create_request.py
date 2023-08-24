import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
from pageObjects.Medical_IP_Request_CreationPage import Medical_IP_Request_CreationPage
from pageObjects.MemberSearchPage import MemberSearchPage
from pageObjects.MemberPage import MemberPage
from pageObjects.RequestHomePage import RequestPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_003_Creating_Request:
    baseurl = ReadConfig.getApplicationURl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    search_id = ReadConfig.getSearchMemberid()
    existing_member_id = ReadConfig.getexisting_member_id()
    Admit_date = ReadConfig.getAdmit_date()
    unit_date = ReadConfig.getunit_date()
    logger = LogGen.loggen()

    def test_create_request_existing_member(self, setup):
        self.logger.info("**************Test_002_Creating_Member********************")
        self.logger.info("**************Verifying Home Page********************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.mp = MemberPage(self.driver)
        self.mp.setUserName(self.username)
        self.mp.setPassword(self.password)
        self.mp.clickLogin()
        self.msg = MemberSearchPage(self.driver)
        time.sleep(2)
        self.msg.clickSearchIcon()
        self.msg.clickMemberIcon()
        self.msg.setexisting_member_id(self.existing_member_id)
        self.msg.clickSearchAerial()
        time.sleep(3)
        self.rp = RequestPage(self.driver)
        # self.msg.setSearchMemberid(self.search_id)
        self.msg.clickSearchAerial()
        time.sleep(3)
        self.rp = RequestPage(self.driver)
        self.rp.clickCmv()
        time.sleep(4)
        self.rp.clickProgram()
        time.sleep(2)
        self.mrc = Medical_IP_Request_CreationPage(self.driver)
        self.logger.info("**************Verifying Request Creation Page********************")
        time.sleep(2)
        self.mrc.clickMedical()
        time.sleep(2)
        self.mrc.clickTreatment()
        time.sleep(1)
        self.mrc.clickTreatmentsetting()
        time.sleep(1)
        self.mrc.clickTreatment_type()
        time.sleep(1)
        self.mrc.clickRequest_treatment_type()
        time.sleep(1)
        s = '05/14/2023'
        date = datetime.strptime(s, "%m/%d/%Y")
        modified_date = date + timedelta(days=1)
        v = datetime.strftime(modified_date, "%m/%d/%Y")
        self.mrc.setAdmit_date(self.Admit_date + v)
        time.sleep(1)
        self.mrc.clickrequest_units()
        time.sleep(2)
        self.mrc.setUnits(self.unit_date)
        self.mrc.clickurgency()
        time.sleep(1)
        self.mrc.clickurgency_type()
        self.mrc.clicksave()
        self.mrc.clicktitle_home()
        self.msp = MemberSearchPage(self.driver)
        self.logger.info("**************Verifying Member Search Page********************")
        self.msp.clickSearchIcon()
        self.msp.clickMemberIcon()
        self.msp.clearMemberid()
        self.msp.setSearchMemberid(self.search_id)
        self.msp.clickSearchAerial()
        time.sleep(2)
        self.msp.clickCmv()
        time.sleep(2)
        self.rp.clickcreated_request()
