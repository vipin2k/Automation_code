import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta

from pageObjects.Discharge_Request import DischargePage
from pageObjects.Medical_IP_Request_CreationPage import Medical_IP_Request_CreationPage
from pageObjects.MemberSearchPage import MemberSearchPage
from pageObjects.MemberPage import MemberPage
from pageObjects.RequestHomePage import RequestPage
from pageObjects.Task_CreationPage import TaskPage
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
    discharge_date = ReadConfig.getdischarge_date()
    logger = LogGen.loggen()

    def test_create_request_existing_member(self, setup):
        self.logger.info("**************Test_003_Creating_Member********************")
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
        time.sleep(1)
        # self.msg.setSearchMemberid(self.search_id)
        self.msg.setexisting_member_id(self.existing_member_id)
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
        # s = '03/14/2023'
        # date = datetime.strptime(s, "%m/%d/%Y")
        # modified_date = date + timedelta(days=1)
        # v = datetime.strftime(modified_date, "%m/%d/%Y")
        # self.mrc.setAdmit_date(self.Admit_date + v)
        # time.sleep(1)
        self.mrc.setAdmit_date(self.Admit_date)
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
        self.msp.setexisting_member_id(self.existing_member_id)
        self.msp.clickSearchAerial()
        time.sleep(2)
        self.msp.clickCmv()
        time.sleep(2)
        self.rp.clickcreated_request()
        request_id = self.driver.find_element(By.XPATH, '(//*[@class="ui-panelgrid-cell"])[30]').text
        # print(request_id)
        print(request_id.split(" ")[0])
        self.rp = RequestPage(self.driver)
        time.sleep(2)
        self.rp.clicknew_item()
        time.sleep(2)
        self.rp.clicktask()
        time.sleep(2)
        self.tp = TaskPage(self.driver)
        time.sleep(3)
        self.tp.clicktask_id()
        time.sleep(1)
        self.tp.clicktask_type()
        time.sleep(2)
        self.tp.clicktask_reason()
        time.sleep(2)
        self.tp.clickreason()
        time.sleep(2)
        # self.tp.clickpriority()
        # time.sleep(2)
        # self.tp.clickpriority_type()
        # time.sleep(3)
        self.tp.clicksave_exit()
        self.Dp = DischargePage(self.driver)
        time.sleep(2)
        self.Dp.click_discharge_button()
        time.sleep(2)
        self.Dp.set_discharge_date(self.discharge_date)
        time.sleep(2)
        self.Dp.click_disposition_button()
        self.Dp.click_disposition_button()
        time.sleep(2)
        self.Dp.click_disposition_type()
        time.sleep(2)
        self.Dp.click_discharge()
        time.sleep(2)
        self.Dp.click_discharge_Task()
        time.sleep(2)
        # task_closed = self.driver.find_element(By.XPATH,
        #                                        "//*[@id='cmvCenterForm:cmvItemsTabView:1:filteredTaskAccordianPanel:closedTaskListTableFiltered_data']/tr[1]/td[3]").text
        # request_closed = self.driver.find_element(By.XPATH,
        #                                           "//*[@id='cmvCenterForm:cmvItemsTabView:1:filteredTaskAccordianPanel:closedTaskListTableFiltered_data']/tr[2]/td[3]").text
        # try:
        #     assert task_closed == request_closed
        #     self.logger.info("*******ACM task and request Discharge successfully - Test Passed*******")
        #     print("Request and Task discharge text matched :" + task_closed)
        # except:
        #     self.logger.error("******ACM task and request Discharge fail- Test Failed*******")
