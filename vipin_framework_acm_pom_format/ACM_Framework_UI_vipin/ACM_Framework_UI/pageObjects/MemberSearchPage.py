from selenium import webdriver
from selenium.webdriver.common.by import By


class MemberSearchPage:
    button_search_member_text = "//*[@class='ui-button-text ui-c' and text()='Search']"
    button_member_xpath = "//*[@class='ui-menuitem-text' and text()='Members']"
    textbox_Search_member_id = "//*[@id='memberSearchTabView:memberIdSearchForm:memberId']"
    button_Search_id = "//*[@id='memberSearchTabView:memberIdSearchForm:memberIdSearchLocalButton']"
    button_cmv_id = "memberSearchResultsForm:memberSearchResultsTable:searchResultsTable:0:memberSearchGotoCMV"

    def __init__(self, driver):
        self.driver = driver

    def clickSearchIcon(self):
        self.driver.find_element(By.XPATH, self.button_search_member_text).click()

    def clickMemberIcon(self):
        self.driver.find_element(By.XPATH, self.button_member_xpath).click()

    def clearMemberid(self):
        self.driver.find_element(By.XPATH, self.textbox_Search_member_id).clear()

    def setSearchMemberid(self, search_id):
        self.driver.find_element(By.XPATH, self.textbox_Search_member_id).send_keys(search_id)

    def setexisting_member_id(self, existing_member_id):
        self.driver.find_element(By.XPATH, self.textbox_Search_member_id).send_keys(existing_member_id)

    def clickSearchAerial(self):
        self.driver.find_element(By.XPATH, self.button_Search_id).click()

    def clickCmv(self):
        self.driver.find_element(By.ID, self.button_cmv_id).click()