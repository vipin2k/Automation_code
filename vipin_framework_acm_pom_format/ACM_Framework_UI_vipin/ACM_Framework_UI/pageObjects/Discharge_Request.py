from selenium import webdriver
from selenium.webdriver.common.by import By


class DischargePage:
    textbox_discharge_button_text = "(//span[@class='ui-button-text ui-c' and text()= 'Discharge Request'])[1]"
    textbox_discharge_date_button_id = "//input[@id='dischargeRequestForm:dischargeDate_input']"
    textbox_disposition_id = "//*[@id='dischargeRequestForm:disposition_label']"
    button_disposition_type_xpath = "//*[@data-label='Home']"
    button_discharge_button_text = "(//span[@class='ui-button-text ui-c' and text()='Discharge Request'])[2]"
    button_Task_id = "//*[@id='cmvCenterForm:cmvItemsTabView']/div[3]/span"
    button_task_close_xpath = "(//*[@class='ui-button-text ui-c' and text()='Close'])[1]"
    dropdown_close_task_outcome_xpath = "//*[@id='closeTaskForm:taskOutcome']/div[3]/span"
    select_dropdown_close_task_outcome_xpath = "//*[@id='closeTaskForm:taskOutcome_14']"
    button_single_close_task_xpath = "//*[@id='closeTaskForm:closeTaskCommandButton']/span"
    click_reopen_discharge = "//*[@class='ui-button-text ui-c' and text() = 'Re-Open Request']"
    textbox_discharge_date_button_id = "//input[@id='dischargeRequestForm:dischargeDate_input']"

    def __init__(self, driver):
        self.driver = driver

    def click_discharge_button(self):
        self.driver.find_element(By.XPATH, self.textbox_discharge_button_text).click()

    def click_discharge_date(self):
        self.driver.find_element(By.XPATH, self.textbox_discharge_date_button_id).clear()

    def set_discharge_date(self, discharge_date):
        self.driver.find_element(By.XPATH, self.textbox_discharge_date_button_id).send_keys(discharge_date)

    def click_disposition_button(self):
        self.driver.find_element(By.XPATH, self.textbox_disposition_id).click()

    def click_disposition_type(self):
        self.driver.find_element(By.XPATH, self.button_disposition_type_xpath).click()

    def click_discharge(self):
        self.driver.find_element(By.XPATH, self.button_discharge_button_text).click()

    def click_discharge_Task(self):
        self.driver.find_element(By.XPATH, self.button_Task_id).click()

    def click_close_task(self):
        self.driver.find_element(By.XPATH, self.button_task_close_xpath).click()

    def click_close_task_dropdown(self):
        self.driver.find_element(By.XPATH, self.dropdown_close_task_outcome_xpath).click()

    def click_dropdown_close(self):
        self.driver.find_element(By.XPATH, self.select_dropdown_close_task_outcome_xpath).click()

    def click_close_wizard(self):
        self.driver.find_element(By.XPATH, self.button_single_close_task_xpath).click()

    def set_discharge_date_clear(self):
        self.driver.find_element(By.XPATH, self.textbox_discharge_date_button_id).clear()

    def click_reopen_discharge_Task(self):
        self.driver.find_element(By.XPATH, self.click_reopen_discharge).click()