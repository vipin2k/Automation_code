import time
from selenium.webdriver.common.by import By
# from CommonClass.web_utils.CommonActions import Request
from CommonClass.web_utils.CommonActions import click, send_keys


class Request():
    def __init__(self, uiTestData):
        self.uiTestData = uiTestData
        # self.driver = driver
        # self.uiTestData = uiTestData
        # print(self.driver)


    def create_Request(self):
        click(self.uiTestData['locators']['member_search_id'])
        time.sleep(2)
        click(self.uiTestData['locators']['member_xpath'])
        time.sleep(2)
        send_keys(self.uiTestData['locators']['enrollment_member_search_id'], self.uiTestData['member']['search_Member_ID'])
        click(self.uiTestData['locators']['enrollment_member_search_button'])
        time.sleep(2)
        click(self.uiTestData['locators']['member_search_button_xpath'])
        time.sleep(5)
        print("Given Member Id search successfully : ", self.uiTestData['member']['search_Member_ID'])
        click(self.uiTestData['locators']['create_new_request_xpath'])
        time.sleep(1)
        click(self.uiTestData['locators']['request_medical_inpatient_xpath'])
        time.sleep(1)
        click(self.uiTestData['locators']['request_treatment_setting_xpath'])
        time.sleep(2)
        click(self.uiTestData['locators']['request_treatment_inpatient_xpath'])
        time.sleep(1)
        click(self.uiTestData['locators']['request_treatment_type_xpath'])
        time.sleep(2)
        click(self.uiTestData['locators']['request_treatment_type_medical_xpath'])
        time.sleep(2)
        click(self.uiTestData['locators']['request_review_type_xpath'])
        time.sleep(3)
        # click(self.uiTestData['locators']['request_days_xpath'])
        # time.sleep(2)
        click(self.uiTestData['locators']['request_days_xpath_6'])
        time.sleep(2)
        send_keys(self.uiTestData['locators']['request_admit_date_xpath'], self.uiTestData['request']['Request_date'])
        time.sleep(2)
        click(self.uiTestData['locators']['click_request_unit_xpath'])
        time.sleep(1)
        send_keys(self.uiTestData['locators']['enter_request_unit_xpath'], self.uiTestData['request']['Request_units'])
        time.sleep(2)
        click(self.uiTestData['locators']['click_request_urgency_xpath'])
        time.sleep(2)
        click(self.uiTestData['locators']['enter_request_emergency_xpath'])
        time.sleep(2)
        click(self.uiTestData['locators']['click_save_exit_xpath'])
        time.sleep(3)
        click(self.uiTestData['locators']['click_aerial_xpath'])
        time.sleep(1)
        click(self.uiTestData['locators']['member_search_id'])
        time.sleep(1)
        click(self.uiTestData['locators']['member_xpath'])
        time.sleep(1)
        click(self.uiTestData['locators']['enrollment_member_search_button'])
        time.sleep(1)
        click(self.uiTestData['locators']['member_search_button_xpath'])
        time.sleep(2)
        print("Request created successfully ")
        print("Request Was Created by Given Member ID : ", self.uiTestData['member']['search_Member_ID'])

