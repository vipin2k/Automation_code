from selenium import webdriver
from selenium.webdriver.common.by import By


class RequestPage:
    button_cmv_id = "memberSearchResultsForm:memberSearchResultsTable:searchResultsTable:0:memberSearchGotoCMV"
    button_New_Program_text = "//*[@class='ui-menuitem-text' and text() = 'New Program/Request']"
    button_created_request_xpath = "//*[@id='cmvCenterForm:requestsAndProgramsAccordionPanel:requestTable_data']/tr/td"
    button_task_new_item_xpath = "//*[@class='ui-button-text ui-c' and text() = 'Add New Item']"
    button_task_xpath = "//*[@class='ui-menuitem-text' and text() ='Task']"



    def __init__(self, driver):
        self.driver = driver

    def clickCmv(self):
        self.driver.find_element(By.ID, self.button_cmv_id).click()

    def clickProgram(self):
        self.driver.find_element(By.XPATH, self.button_New_Program_text).click()

    def clickcreated_request(self):
        self.driver.find_element(By.XPATH, self.button_created_request_xpath).click()

    def clicknew_item(self):
        self.driver.find_element(By.XPATH, self.button_task_new_item_xpath).click()

    def clicktask(self):
        self.driver.find_element(By.XPATH, self.button_task_xpath).click()