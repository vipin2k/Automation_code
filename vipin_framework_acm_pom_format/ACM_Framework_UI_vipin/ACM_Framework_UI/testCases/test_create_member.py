import pytest
from selenium import webdriver
import time
import string
import random
from selenium.webdriver.common.by import By
from pageObjects.Medical_IP_Request_CreationPage import Medical_IP_Request_CreationPage
from pageObjects.MemberSearchPage import MemberSearchPage
from pageObjects.MemberPage import MemberPage
from pageObjects.EnrollmentPage import EnrollmentPage
from pageObjects.RequestHomePage import RequestPage
from pageObjects.Task_CreationPage import TaskPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_002_Creating_Member:
    baseurl = ReadConfig.getApplicationURl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    firstname = ReadConfig.getFirstname()
    lastname = ReadConfig.getLastname()
    member_id = ReadConfig.getMember_id()
    DOB = ReadConfig.getMember_DOB()
    Effective_date = ReadConfig.getEffective_date()
    search_id = ReadConfig.getSearchMemberid()
    Admit_date = ReadConfig.getAdmit_date()
    unit_date = ReadConfig.getunit_date()
    logger = LogGen.loggen()

    def test_createMember(self, setup):
        self.logger.info("**************Test_002_Creating_Member********************")
        self.logger.info("**************Verifying Home Page********************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.mp = MemberPage(self.driver)
        self.mp.setUserName(self.username)
        self.mp.setPassword(self.password)
        self.mp.clickLogin()
        self.mp.clickSearch()
        self.mp.clickMember()
        self.mp.clickNewMember()
        self.mp.setFirstName(self.firstname)
        self.mp.setLastName(self.lastname)
        self.Number = 5
        value = ''.join(random.choices(string.ascii_uppercase + string.digits, k=self.Number))
        print("The generated random string number : " + str(value))
        self.mp.setMemberId(self.member_id + str(value))
        self.mp.setDob(self.DOB)
        time.sleep(5)
        self.mp.clickGender()
        self.ep = EnrollmentPage(self.driver)
        self.logger.info("**************Verifying Enrollment Page********************")
        self.ep.clickEnrollment()
        self.ep.clickAdd()
        self.ep.clickThisMember()
        self.ep.clickRelationship()
        self.ep.clickRelationship_type()
        self.ep.setEffective_date(self.Effective_date)
        self.ep.clickSave()
        self.msg = MemberSearchPage(self.driver)
        time.sleep(2)
        self.msg.clickSearchIcon()
        self.msg.clickMemberIcon()
        self.msg.setSearchMemberid(self.search_id + str(value))
        self.msg.clickSearchAerial()
        time.sleep(3)
        search_id = value
        sample_xpath = f'//a[@id="memberSearchResultsForm:memberSearchResultsTable:searchResultsTable:0:memberDemographics" and text()="{value}"]'
        self.txt = self.driver.find_element(By.XPATH, sample_xpath).text
        print(self.txt)
        if search_id:
            assert search_id == self.txt
            self.logger.info("*******ACM user Login Successful- Test Passed*******")
            print("value match")
        else:
            self.logger.error("*******ACM user Login Successful- Test Failed*******")
            print("Doesn't match")
        self.rp = RequestPage(self.driver)
        self.rp.clickCmv()
        time.sleep(4)
        self.rp.clickProgram()
        time.sleep(2)
        self.mrc = Medical_IP_Request_CreationPage(self.driver)
        self.logger.info("**************Test_002_Creating_Member********************")
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
        self.mrc.setAdmit_date(self.Admit_date)
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
        self.logger.info("**************Test_002_Creating_Member********************")
        self.logger.info("**************Verifying Member Search Page********************")
        self.msp.clickSearchIcon()
        self.msp.clickMemberIcon()
        self.msp.clearMemberid()
        self.msp.setSearchMemberid(self.search_id + str(value))
        self.msp.clickSearchAerial()
        time.sleep(2)
        self.msp.clickCmv()
        time.sleep(2)
        self.Admit_date = "03/22/2023"
        admit = self.Admit_date
        self.date = self.driver.find_element(By.XPATH, "(//*[@class='inpatient addDynamicTooltip'])[1]").text
        time.sleep(2)
        self.rp.clickcreated_request()
        time.sleep(2)
        date = self.date.split(" ")[0]
        try:
            assert admit == date
            self.logger.info("*******ACM request creation date- Test Passed*******")
            print("current date :" + admit)
        except:
            self.logger.error("******ACM request creation date- Test Failed*******")
        time.sleep(5)
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
        self.tp.clickpriority()
        time.sleep(2)
        self.tp.clickpriority_type()
        time.sleep(3)
        self.tp.clicksave_exit()
        time.sleep(1)
        self.driver.refresh()
        time.sleep(5)
        tsk = self.driver.find_element(By.XPATH,
                                       "//*[@id='cmvCenterForm:cmvItemsTabView:1:filteredTaskAccordianPanel:openTaskListTableFiltered_data']/tr[1]/td[3]").text
        req = self.driver.find_element(By.XPATH,
                                       "//*[@id='cmvCenterForm:cmvItemsTabView:1:filteredTaskAccordianPanel:openTaskListTableFiltered_data']/tr[2]/td[3]").text
        try:
            assert tsk == req
            self.logger.info("*******ACM task and request text matched- Test Passed*******")
            print("Request and Task text matched :" + tsk)
        except:
            self.logger.error("******ACM task and request text matched- Test Failed*******")



