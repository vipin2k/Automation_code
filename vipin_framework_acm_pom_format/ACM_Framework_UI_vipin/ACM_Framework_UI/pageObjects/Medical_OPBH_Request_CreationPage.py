from selenium import webdriver
from selenium.webdriver.common.by import By

class Medical_OPBH_Request_CreationPage:
    click_button_Medical_OPBH_text = "//*[@class='ui-menuitem-text' and text()= 'Behavioral Health Outpatient']"
    button_treatment_setting_id = "//*[@id='requestForm:treatmentSetting_label']"
    button_treatment_setting_service = "//*[@id='serviceDetailsForm:treatmentType_label']"
    button_click_Treatment_setting_dropdown = "//*[@id='serviceDetailsForm:treatmentType_2']"
    button_startdate_XPATH = "//*[@id='serviceDetailsForm:startDate_input']"
    button_request_unit_xpath = "//*[@id='serviceDetailsForm:requestedUnits']"
    button_treatment_setting_type_text = "//*[@data-label='Outpatient']"
    button_treatment_urgency_id = "//*[@id='requestForm:urgency_label']"
    button_treatment_urgency_type_id = "//*[@data-label='Emergency']"
    button_providers_text = "(//span[@class='ui-menuitem-text' and text()='Providers'])[1]"
    textbox_facility_name = "//*[@id='providersAccordion:providerMultiSearchForm:providerSearchTabView:providerNameSearchView:practitionerLastName']"
    button_search_aerial_xpath = "//*[@class='ui-button-text ui-c' and text()= 'Search Aerial']"
    button_add_facility_xpath = "(//*[@class='ui-button-text ui-c' and text()= 'Add'])[6]"
    button_select_facility_xpath = "(//*[@class='ui-chkbox-icon ui-icon ui-icon-blank ui-c'])[4]"
    button_Diagnoses_xpath = "//*[@id='menuForm:requestSectionMenu']/ul/li[4]/a/span"
    button_Diagnoses_Description = "//*[@id='diagnosesForm:requestBHDiagnoses:diagnosisSearchDescription']"
    button_search_diagnoses_xpath = "//*[@id='diagnosesForm:requestBHDiagnoses:searchDiagnosesButton']/span"
    button_clickdiagnoses_add_xpath = "//*[@id='diagnosesForm:requestBHDiagnoses:diagnosisSearchResultsTable:0:addDiagnosisLink']/span[2]"
    button_select_diagnoses_xpath = "//*[@class='ui-menuitem-text' and text()= 'Diagnoses']"
    button_diagnoses_dropdown = "//*[@class='ui-selectonemenu-trigger ui-state-default ui-corner-right']"
    button_select_diagnoses_dropdown = "(//*[@class='ui-selectonemenu-item ui-selectonemenu-list-item ui-corner-all'])[2]"
    button_select_diagnosis_add = "(//*[@class='ui-button-text ui-c' and text()='Add'])[1]"
    button_social_problem_select = "(//*[@class='ui-chkbox-box ui-widget ui-corner-all ui-state-default'])[2]"
    textbox_GAF_score_xpath = "//*[@id='diagnosesForm:requestBHDiagnoses:axisVScore']"
    button_select_GAF_diagnosis_add = "(//*[@class='ui-button-text ui-c' and text()='Add'])[2]"
    button_select_services_xpath = "//*[@class='ui-menuitem-text' and text()= 'Services']"
    button_click_service_dropdown = "//*[@class='ui-icon ui-icon-triangle-1-s ui-c']"
    button_select_service_dropdown = "//*[@id='requestProcedureSearch:procedureSearchForm:procedureQuickList_1']"
    button_select_service_add = "//*[@class='ui-button-text ui-c' and text()='Add']"
    button_select_service_tab = "//*[@id='menuForm:requestSectionMenu']/ul/li[6]/a/span"
    button_select_service_add_tab = "//*[@class='ui-menuitem-link ui-corner-all requestNavigationMenuItem requestNavigationIconNone requestNavigationMenuItemService']"
    button_Review_tab_xpath = "(//*[@class='ui-menuitem-link ui-corner-all'])[3]"
    button_mcg_page_xpath = "//*[@id='MainContent_cgxGuidelineSearchCriteria_rsltsGrid_rptSearchRelated_rptSearchRows_0_rptSearchCells_0_lblData_19']"
    button_mcg_episode_page_xpath = "//*[@id='MainContent_cgxEpisodeOverview_btnExitEpisode']"
    button_review_status_dropdown = "//*[@id='reviewAccordion:newOutcomeForm:newOutcomeAccordion:serviceReviewOutcomeEntry:outcomeStatus_label']"
    button_status_dropdown_value = "//*[@data-label='Approve']"
    button_status_reason_dropdown_id = "reviewAccordion:newOutcomeForm:newOutcomeAccordion:statusReason_label"
    button_status_reason_dropdown_value = "//*[@data-label='Clinical Criteria Met']"
    button_click_Add_outcome = "//*[@class='ui-button-text ui-c' and text()= 'Add Outcome']"
    button_save_text = "//*[@class='ui-button-text ui-c' and text() ='Save & Exit']"
    button_title_home_xpath = "//a[@title='Home']"
    button_click_extend_outcome = "//*[@class='ui-button-text ui-c' and text()= 'Extend']"
    textbox_request_name = "//*[@id='serviceDetailsForm:requestedUnits']"
    textbox_request_units_name = "//*[@id='serviceDetailsForm:requestedUnits']"
    textbox_review_To_Date = "//*[@id='reviewAccordion:newOutcomeForm:newOutcomeAccordion:serviceReviewOutcomeEntry:toDate_input']"
    button_save_exit_OP_req_text = "//*[@class='ui-button-text ui-c' and text() ='Save & Exit']"
    # button_title_home_xpath = "(// a[@ title='Home'])[1]"

    def __init__(self, driver):
        self.driver = driver

    def click_Medical_OPBH(self):
        self.driver.find_element(By.XPATH, self.click_button_Medical_OPBH_text).click()

    def click_Treatment_setting(self):
        self.driver.find_element(By.XPATH, self.button_treatment_setting_id).click()

    def click_Treatment_setting_dropdown(self):
        self.driver.find_element(By.XPATH, self.button_click_Treatment_setting_dropdown).click()

    def click_startdate(self, startdate):
        self.driver.find_element(By.XPATH, self.button_startdate_XPATH).send_keys(startdate)

    def click_request_units_service(self):
        self.driver.find_element(By.XPATH, self.button_request_unit_xpath).click()

    def set_request_units_service(self, requested_units):
        self.driver.find_element(By.XPATH, self.button_request_unit_xpath).send_keys(requested_units)

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

    def click_Diagnoses(self):
        self.driver.find_element(By.XPATH, self.button_Diagnoses_xpath).click()

    # def click_diagnoses(self):
    #     self.driver.find_element(By.XPATH, self.button_diagnoses_xpath).click()

    def click_Diagnoses_Description(self, Description):
        self.driver.find_element(By.XPATH, self.button_Diagnoses_Description).send_keys(Description)

    def click_search_diagnoses(self):
        self.driver.find_element(By.XPATH, self.button_search_diagnoses_xpath).click()

    def clickdiagnoses_add(self):
        self.driver.find_element(By.XPATH, self.button_clickdiagnoses_add_xpath).click()

    def clickselect_services(self):
        self.driver.find_element(By.XPATH, self.button_select_services_xpath).click()

    def clickservice_dropdown(self):
        self.driver.find_element(By.XPATH, self.button_click_service_dropdown).click()

    def click_select_service_dropdown(self):
        self.driver.find_element(By.XPATH, self.button_select_service_dropdown).click()

    def click_select_service_add(self):
        self.driver.find_element(By.XPATH, self.button_select_service_add).click()

    def click_service_tab(self):
        self.driver.find_element(By.XPATH, self.button_select_service_tab).click()

    def click_Treatment_setting_service(self):
        self.driver.find_element(By.XPATH, self.button_treatment_setting_service).click()


    # def click_select_service_add_tab(self):
    #     self.driver.find_element(By.XPATH, self.button_select_service_add_tab).click()

    def clickReview_tab(self):
        self.driver.find_element(By.XPATH, self.button_Review_tab_xpath).click()

    def clickmcg_page(self):
        self.driver.find_element(By.XPATH, self.button_mcg_page_xpath).click()

    def clickmcg_episode_page(self):
        self.driver.find_element(By.XPATH, self.button_mcg_episode_page_xpath).click()

    def clickreview_status_dropdown(self):
        self.driver.find_element(By.XPATH, self.button_review_status_dropdown).click()

    def click_dropdown_value(self):
        self.driver.find_element(By.XPATH, self.button_status_dropdown_value).click()

    def click_reason_dropdown_id(self):
        self.driver.find_element(By.XPATH, self.button_status_reason_dropdown_id).click()

    def clickreason_dropdown_value(self):
        self.driver.find_element(By.XPATH, self.button_status_reason_dropdown_value).click()

    def clickAdd_outcome(self):
        self.driver.find_element(By.XPATH, self.button_click_Add_outcome).click()

    def clicksave(self):
        self.driver.find_element(By.XPATH, self.button_save_exit_OP_req_text).click()

    def clicktitle_home(self):
        self.driver.find_element(By.XPATH, self.button_title_home_xpath).click()

    def clickextend(self):
        self.driver.find_element(By.XPATH, self.button_click_extend_outcome).click()

    def set_review_To_Date(self, To_Date):
        self.driver.find_element(By.XPATH, self.textbox_review_To_Date).send_keys(To_Date)

    def set_request_units(self, requested_units):
        self.driver.find_element(By.XPATH, self.textbox_request_name).send_keys(requested_units)

    def setUnits(self, unit_date):
        self.driver.find_element(By.XPATH, self.textbox_request_units_name).send_keys(unit_date)