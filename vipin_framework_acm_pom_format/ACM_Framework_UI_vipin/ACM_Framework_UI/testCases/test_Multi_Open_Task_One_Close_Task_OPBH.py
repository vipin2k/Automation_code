import pytest
from selenium import webdriver
import time
import string
import random
from selenium.webdriver.common.by import By
from pageObjects.Discharge_Request import DischargePage
from pageObjects.Medical_IPBH_Request_CreationPage import Medical_IPBH_Request_CreationPage
from pageObjects.Medical_IP_Request_CreationPage import Medical_IP_Request_CreationPage
from pageObjects.Medical_OPBH_Request_CreationPage import Medical_OPBH_Request_CreationPage
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
    discharge_date = ReadConfig.getdischarge_date()
    unit_date = ReadConfig.getunit_date()
    owner = ReadConfig.getowner()
    facility = ReadConfig.getfacility()
    logger = LogGen.loggen()
    # @pytest.mark.sanity
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

    # def test_Enrollment(self, setup):
        self.ep.clickEnrollment()
        self.ep.clickAdd()
        self.ep.clickThisMember()
        self.ep.clickRelationship()
        time.sleep(2)
        self.ep.clickRelationship_type()
        time.sleep(1)
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
        self.MOPBH = Medical_OPBH_Request_CreationPage(self.driver)
        self.logger.info("**************Test_002_Creating_Member********************")
        self.logger.info("**************Verifying Request Creation Page********************")
        time.sleep(2)
        self.MOPBH.click_Medical_OPBH()
        time.sleep(2)
        self.MOPBH.click_Treatment_setting()
        time.sleep(1)
        self.MOPBH.click_Treatment_setting_type()
        time.sleep(1)
        self.MOPBH.clickurgency()
        time.sleep(1)
        self.MOPBH.click_emergency()
        time.sleep(1)
        self.MOPBH.clickproviders_type()
        time.sleep(1)
        self.MOPBH.click_facility()
        time.sleep(1)
        self.MOPBH.setfacility(self.facility)
        time.sleep(1)
        self.MOPBH.clicksearch_aerial()
        time.sleep(1)
        self.MOPBH.clickadd_facility()
        time.sleep(1)
        self.MOPBH.click_select_facility()
        time.sleep(1)
        self.MOPBH.click_select_diagnoses()
        time.sleep(1)
        self.MOPBH.clickdiagnoses_dropdown()
        time.sleep(2)
        self.MOPBH.click_select_diagnoses_dropdown()
        time.sleep(2)
        self.MOPBH.click_select_diagnosis_add()
        time.sleep(2)
        self.MOPBH.clickselect_services()
        time.sleep(1)
        self.MOPBH.clickservice_dropdown()
        time.sleep(1)
        self.MOPBH.click_select_service_dropdown()
        time.sleep(1)
        self.MOPBH.click_select_service_add()
        time.sleep(1)
        self.MOPBH.clickReview_tab()
        time.sleep(1)
        self.MOPBH.clickreview_status_dropdown()
        time.sleep(1)
        self.MOPBH.click_dropdown_value()
        time.sleep(1)
        self.MOPBH.click_reason_dropdown_id()
        time.sleep(1)
        self.MOPBH.clickreason_dropdown_value()
        time.sleep(1)
        self.MOPBH.clickAdd_outcome()
        time.sleep(1)
        self.MOPBH.clicksave()
        time.sleep(1)
        # self.MOPBH.clicktitle_home()
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
        # self.Admit_date = "03/22/2023"
        # admit = self.Admit_date
        # self.date = self.driver.find_element(By.XPATH, "//*[@class='ui-widget-content ui-datatable-even ui-datatable-selectable']").text
        # time.sleep(2)
        self.rp.clickcreated_request()
        # time.sleep(2)
        # date = self.date.split(" ")[0]
        # try:
        #     assert admit == date
        #     self.logger.info("*******ACM request creation date- Test Passed*******")
        #     print("current date :" + admit)
        # except:
        #     self.logger.error("******ACM request creation date- Test Failed*******")
        # time.sleep(5)
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
        # time.sleep(2)
        # self.tp.clickpriority()
        # time.sleep(2)
        # self.tp.clickpriority_type()
        time.sleep(3)
        self.tp.clicksave_exit()
        time.sleep(1)
        self.driver.refresh()
        time.sleep(5)
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
        time.sleep(3)
        self.tp.clicksave_exit()
        # tsk = self.driver.find_element(By.XPATH,
        #                                "//*[@id='cmvCenterForm:cmvItemsTabView:1:filteredTaskAccordianPanel:openTaskListTableFiltered_data']/tr[1]/td[3]").text
        # req = self.driver.find_element(By.XPATH,
        #                                "//*[@id='cmvCenterForm:cmvItemsTabView:1:filteredTaskAccordianPanel:openTaskListTableFiltered_data']/tr[2]/td[3]").text
        # try:
        #     assert tsk == req
        #     self.logger.info("*******ACM task and request text matched- Test Passed*******")
        #     print("Request and Task text matched :" + tsk)
        # except:
        #     self.logger.error("******ACM task and request text matched- Test Failed*******")
        # time.sleep(2)
        self.Dp = DischargePage(self.driver)
        time.sleep(2)
        # self.Dp.click_discharge_button()
        # time.sleep(2)
        # self.Dp.set_discharge_date(self.discharge_date)
        # time.sleep(2)
        # self.Dp.click_disposition_button()
        # self.Dp.click_disposition_button()
        # time.sleep(2)
        # self.Dp.click_disposition_type()
        # time.sleep(1)
        # self.Dp.click_discharge()
        # self.Dp.click_discharge()
        # time.sleep(2)
        # self.Dp.click_discharge_Task()
        # time.sleep(2)
        self.Dp.click_close_task()
        time.sleep(2)
        self.Dp.click_close_task_dropdown()
        time.sleep(2)
        self.Dp.click_dropdown_close()
        time.sleep(2)
        self.Dp.click_close_wizard()
        time.sleep(5)
        self.driver.refresh()
        self.Open_task = self.driver.find_element(By.XPATH,
                                             "//*[@id='cmvCenterForm:cmvItemsTabView:1:filteredTaskAccordianPanel']/div[1]").text
        time.sleep(2)
        print(self.Open_task)
        self.Closed_task = self.driver.find_element(By.XPATH,
                                               "//*[@id='cmvCenterForm:cmvItemsTabView:1:filteredTaskAccordianPanel']/div[3]").text
        time.sleep(2)
        print(self.Closed_task)
        # discharged = self.driver.find_element(By.XPATH,
        #                                       "//*[@class='ui-button-text ui-c' and text()='Re-Open Request']").text
        # print(discharged, "Successfully discharged")
        # time.sleep(5)
        # self.Dp.click_reopen_discharge_Task()
        # try:
        #     outcome = self.driver.find_element(By.XPATH, "(//span[text()='Outcome']//following::tr/td[3])[1]").text
        #     assert outcome == "Auto-closed"
        #     self.logger.info("*******Task Auto-Closed Successfully- Test Passed*******")
        #     print("value match - Config ON (APPL_CONFIG AutoCloseTasksOnRequestDischarge)")
        # except:
        #     pass
        #     # print("In AMDOQ6, the result value does not match, or an Exception occurred in this URL.")
        #     # self.logger.error("*******Task validation- Test Failed*******")
        # try:
        #     ownername = self.driver.find_element(By.XPATH, "(//span[text()='Owner']//following::tr/td[3])[1]").text
        #     assert ownername == owner
        #     self.logger.error("*******Task not Auto-Closed - Test Passed*******")
        #     print("value match - Config OFF (APPL_CONFIG AutoCloseTasksOnRequestDischarge)")
        # except:
        #     pass
        #     # print("In AMDOQ11, the result value does not match, or an Exception occurred in this URL.")
        #     # self.logger.error("*******Task validation- Test Failed*******")
        # try:
        #     outcome = self.driver.find_element(By.XPATH, "(//span[text()='Outcome']//following::tr/td[3])[1]").text
        #     ownername = self.driver.find_element(By.XPATH, "(//span[text()='Owner']//following::tr/td[3])[1]").text
        #     self.logger.error("*******Task validation- Test Failed*******")
        # except:
        #     print("In AMDOQ6 or AMDOQ11, the result value does not match, or an Exception occurred in this URL , Something else went wrong....")
        #
