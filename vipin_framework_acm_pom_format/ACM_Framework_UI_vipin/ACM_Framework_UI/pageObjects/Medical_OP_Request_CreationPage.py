from selenium import webdriver
from selenium.webdriver.common.by import By

class Medical_OP_Request_CreationPage:
    button_Medical_Outpatient_id = "//*[@id='cmvCenterForm:medicalOPMenuItem']"
    button_treatment_setting_id = "//*[@id='requestForm:treatmentSetting_label']"
    button_treatment_setting_type_text = "//*[@data-label='Outpatient']"
    button_treatment_urgency_id = "//*[@id='requestForm:urgency_label']"
    button_treatment_urgency_type_id = "//*[@data-label='Emergency']"
    button_providers_text = "(//span[@class='ui-menuitem-text' and text()='Providers'])[1]"
    textbox_facility_name = "//*[@id='providersAccordion:providerMultiSearchForm:providerSearchTabView:providerNameSearchView:practitionerLastName']"
    button_search_aerial_xpath = "//*[@class='ui-button-text ui-c' and text()= 'Search Aerial']"
    button_add_facility_xpath = "(//*[@class='ui-button-text ui-c' and text()= 'Add'])[6]"
    button_select_facility_xpath = "//*[@id='providersAccordion:providersForm:requestProviders:providersDataTable:0:providerRoleListEven']/tbody/tr[2]/td[2]/div/div[2]"
    button_select_diagnoses_xpath = "//*[@class='ui-menuitem-text' and text()= 'Diagnoses']"
    button_diagnoses_dropdown = "//*[@class='ui-selectonemenu-trigger ui-state-default ui-corner-right']"
    button_select_diagnoses_dropdown = "(//*[@class='ui-selectonemenu-item ui-selectonemenu-list-item ui-corner-all'])[3]"
    button_select_diagnosis_add = "(//*[@class='ui-button-text ui-c' and text()='Add'])[1]"
    button_social_problem_select = "(//*[@class='ui-chkbox-box ui-widget ui-corner-all ui-state-default'])[2]"
    textbox_GAF_score_xpath = "//*[@id='diagnosesForm:requestBHDiagnoses:axisVScore']"
    button_select_GAF_diagnosis_add = "(//*[@class='ui-button-text ui-c' and text()='Add'])[2]"
    button_select_services_xpath = "//*[@class='ui-menuitem-text' and text()= 'Services']"
    button_click_service_dropdown = "//*[@class='ui-icon ui-icon-triangle-1-s ui-c']"
    button_select_service_dropdown = "(//*[@class='ui-selectonemenu-item ui-selectonemenu-list-item ui-corner-all'])[3]"
    button_select_service_add = "//*[@class='ui-button-text ui-c' and text() = 'Add']"
    button_select_service_scheme = "//*[@class='ui-menuitem-link ui-corner-all requestNavigationMenuItem requestNavigationIconNone requestNavigationMenuItemService']"
    button_service_treatment_dropdown = "//*[@id='serviceDetailsForm:treatmentType_label']"
    select_service_treatment_type_dropdown_value = "//*[@data-label='Chiropractic Care']"
    button_service_start_date_xpath = "//*[@id='serviceDetailsForm:startDate_input']"
    textbox_request_units_name = "//*[@id='serviceDetailsForm:requestedUnits']"
    button_review_tab_xpath = "//*[@id='serviceMenuForm:reviewMenuItem']"
    button_select_mcg_page_xpath = "//*[@id='MainContent_cgxGuidelineSearchCriteria_rsltsGrid_rptSearchRelated_rptSearchRows_0_rptSearchCells_0_lblData_19']/a"
    button_mcg_episode_page = "//*[@id='MainContent_cgxEpisodeOverview_btnExitEpisode']"
    button_review_TODATE_xpath = "//*[@id='reviewAccordion:newOutcomeForm:newOutcomeAccordion:serviceReviewOutcomeEntry:toDate_input']"
    button_review_status_dropdown = "(//*[@class='ui-selectonemenu-trigger ui-state-default ui-corner-right'])[1]"
    button_review_status_dropdown_value_type = "//*[@data-label='Approve']"
    button_click_Add_outcome = "//*[@class='ui-button-text ui-c' and text()= 'Add Outcome']"
    button_save_text = "//*[@class='ui-button-text ui-c' and text() ='Save & Exit']"
    button_extend_xpath = "//*[@class='ui-button-text ui-c' and text()= 'Extend']"
    select_services_edit_request_xpath = "//*[@class='ui-button-text ui-c' and text()= 'Edit Request']"
    button_title_home_xpath = "//a[@title='Home']"


    def __init__(self, driver):
        self.driver = driver

    def click_Medical_OP(self):
        self.driver.find_element(By.XPATH, self.button_Medical_Outpatient_id).click()

    def click_Treatment_setting(self):
        self.driver.find_element(By.XPATH, self.button_treatment_setting_id).click()

    def click_Treatment_setting_type(self):
        self.driver.find_element(By.XPATH, self.button_treatment_setting_type_text).click()

    def clickurgency(self):
        self.driver.find_element(By.XPATH, self.button_treatment_urgency_id).click()

    def click_emergency(self):
        self.driver.find_element(By.XPATH, self.button_treatment_urgency_type_id).click()

    def clickproviders_type(self):
        self.driver.find_element(By.XPATH, self.button_providers_text).click()

    def click_facility(self):
        self.driver.find_element(By.XPATH, self.textbox_facility_name).click()

    def setfacility(self, facility):
        self.driver.find_element(By.XPATH, self.textbox_facility_name).send_keys(facility)

    def clicksearch_aerial(self):
        self.driver.find_element(By.XPATH, self.button_search_aerial_xpath).click()

    def clickadd_facility(self):
        self.driver.find_element(By.XPATH, self.button_add_facility_xpath).click()

    def click_select_facility(self):
        self.driver.find_element(By.XPATH, self.button_select_facility_xpath).click()

    def click_select_diagnoses(self):
        self.driver.find_element(By.XPATH, self.button_select_diagnoses_xpath).click()

    def clickdiagnoses_dropdown(self):
        self.driver.find_element(By.XPATH, self.button_diagnoses_dropdown).click()

    def click_select_diagnoses_dropdown(self):
        self.driver.find_element(By.XPATH, self.button_select_diagnoses_dropdown).click()

    def click_select_diagnosis_add(self):
        self.driver.find_element(By.XPATH, self.button_select_diagnosis_add).click()

    def clickselect_services(self):
        self.driver.find_element(By.XPATH, self.button_select_services_xpath).click()

    def clickservice_dropdown(self):
        self.driver.find_element(By.XPATH, self.button_click_service_dropdown).click()

    def click_select_service_dropdown(self):
        self.driver.find_element(By.XPATH, self.button_select_service_dropdown).click()

    def click_select_service_add(self):
        self.driver.find_element(By.XPATH, self.button_select_service_add).click()

    def click_select_service_scheme(self):
        self.driver.find_element(By.XPATH, self.button_select_service_scheme).click()

    def click_service_treatment_dropdown(self):
        self.driver.find_element(By.XPATH, self.button_service_treatment_dropdown).click()

    def click_service_treatment_type_dropdown_value(self):
        self.driver.find_element(By.XPATH, self.select_service_treatment_type_dropdown_value).click()

    def set_service_start_date(self, start_date):
        self.driver.find_element(By.XPATH, self.button_service_start_date_xpath).send_keys(start_date)

    def clickrequest_units(self):
        self.driver.find_element(By.XPATH, self.textbox_request_units_name).click()

    def setUnits(self, unit_date):
        self.driver.find_element(By.XPATH, self.textbox_request_units_name).send_keys(unit_date)

    def clickreview_tab(self):
        self.driver.find_element(By.XPATH, self.button_review_tab_xpath).click()

    def clickselect_mcg_page(self):
        self.driver.find_element(By.XPATH, self.button_select_mcg_page_xpath).click()

    def click_mcg_episode_page(self):
        self.driver.find_element(By.XPATH, self.button_mcg_episode_page).click()

    def set_review_TODATE(self, To_date):
        self.driver.find_element(By.XPATH, self.button_review_TODATE_xpath).send_keys(To_date)

    def clickreview_status_dropdown(self):
        self.driver.find_element(By.XPATH, self.button_review_status_dropdown).click()

    def click_status_dropdown_value(self):
        self.driver.find_element(By.XPATH, self.button_review_status_dropdown_value_type).click()

    def click_Add_outcome(self):
        self.driver.find_element(By.XPATH, self.button_click_Add_outcome).click()

        # def clickreason_dropdown_value(self):
        #     self.driver.find_element(By.XPATH, self.button_status_reason_dropdown_value).click()

    def clicksave(self):
        self.driver.find_element(By.XPATH, self.button_save_text).click()

    def clickextend(self):
        self.driver.find_element(By.XPATH, self.button_extend_xpath).click()

    def clicktitle_home(self):
        self.driver.find_element(By.XPATH, self.button_title_home_xpath).click()