from selenium import webdriver
from selenium.webdriver.common.by import By


class TaskPage:
    button_task_id = "addTask:taskForm:taskType_label"
    textbox_task_type_xpath = "//*[@data-label='Add Attachment']"
    button_task_reason_id = "addTask:taskForm:taskReason_label"
    textbox_reason_xpath = "//*[@data-label='Add Attachment in iExchange']"
    button_close_task_xpath = "//*[@id='cmvCenterForm:cmvItemsTabView:1:filteredTaskAccordianPanel:openTaskListTableFiltered:0:closeTask']/span"
    button_close_task_2_xpath ="//*[@id='cmvCenterForm:cmvItemsTabView:1:filteredTaskAccordianPanel:openTaskListTableFiltered:0:closeTask']/span"
    button_close_task_wizard_xpath = "//*[@id='closeTaskForm:closeTaskCommandButton']/span"
    button_save_exit_xpath = "(//*[@class='ui-button-text ui-c' and text() ='Save & Exit'])[2]"
    button_priority_xpath = "addTask:taskForm:priority_label"
    textbox_priority_type_xpath = "//*[@data-label='Critical']"
    button_open_xpath = "(//*[@class='ui-accordion-header ui-helper-reset ui-state-default ui-corner-all'])[6]"

    def __init__(self, driver):
        self.driver = driver

    def clicktask_id(self):
        self.driver.find_element(By.ID, self.button_task_id).click()

    def clicktask_type(self):
        self.driver.find_element(By.XPATH, self.textbox_task_type_xpath).click()

    def clicktask_reason(self):
        self.driver.find_element(By.ID, self.button_task_reason_id).click()

    def clickreason(self):
        self.driver.find_element(By.XPATH, self.textbox_reason_xpath).click()

    def close_task_1(self):
        self.driver.find_element(By.XPATH, self.button_close_task_xpath).click()

    def close_task_wizard_button(self):
        self.driver.find_element(By.XPATH, self.button_close_task_wizard_xpath).click()

    def close_task_2(self):
        self.driver.find_element(By.XPATH, self.button_close_task_2_xpath).click()

    def clickpriority(self):
        self.driver.find_element(By.ID, self.button_priority_xpath).click()

    def clickpriority_type(self):
        self.driver.find_element(By.XPATH, self.textbox_priority_type_xpath).click()

    def clicksave_exit(self):
        self.driver.find_element(By.XPATH, self.button_save_exit_xpath).click()

    def click_open(self):
        self.driver.find_element(By.XPATH, self.button_open_xpath).click()