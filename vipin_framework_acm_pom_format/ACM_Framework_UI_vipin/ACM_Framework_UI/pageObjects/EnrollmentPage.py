from selenium import webdriver
from selenium.webdriver.common.by import By


class EnrollmentPage:
    button_enrollment_xpath = "//*[@class='ui-menuitem-text' and text() = 'Enrollment']"
    button_Add_xpath = "//*[@class='ui-button-text ui-c' and text() = 'Add']"
    button_this_member_xpath = "(//*[@class='ui-radiobutton-icon ui-icon ui-icon-blank ui-c'])[1]"
    button_Relationship_id = "//*[@id='memberDetailEnrollmentForm:member_Relationship_label']"
    textbox_Relationship_type_text = "//*[@data-label='Cousin']"
    textbox_Effective_date_name = "//*[@name='memberDetailEnrollmentForm:effDate_input']"
    button_Save_xpath = "//*[@class='ui-button-text ui-c' and text() = 'Save & Exit']"

    def __init__(self, driver):
        self.driver = driver

    def clickEnrollment(self):
        self.driver.find_element(By.XPATH, self.button_enrollment_xpath).click()

    def clickAdd(self):
        self.driver.find_element(By.XPATH, self.button_Add_xpath).click()

    def clickThisMember(self):
        self.driver.find_element(By.XPATH, self.button_this_member_xpath).click()

    def clickRelationship(self):
        self.driver.find_element(By.XPATH, self.button_Relationship_id).click()

    def clickRelationship_type(self):
        self.driver.find_element(By.XPATH, self.textbox_Relationship_type_text).click()

    def setEffective_date(self, Effective_date):
        self.driver.find_element(By.XPATH, self.textbox_Effective_date_name).send_keys(Effective_date)

    def clickSave(self):
        self.driver.find_element(By.XPATH, self.button_Save_xpath).click()
