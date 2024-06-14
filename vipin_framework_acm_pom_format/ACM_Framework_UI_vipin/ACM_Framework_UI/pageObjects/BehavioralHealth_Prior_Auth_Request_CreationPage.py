from selenium import webdriver
from selenium.webdriver.common.by import By


class BehavioralHealth_Prior_Auth:
    button_BHPA_text = "//span[@class='ui-menuitem-text' and text() = 'Behavioral Health Prior Auth']"
    button_BHPA_Urgency_id = "//label[@id='requestForm:urgency_label']"
    button_BHPA_Urgency_type_xpath = "//*[@data-label='Emergency']"
    button_Providers_tab_xpath = "(//span[@class='ui-menuitem-text' and text() = 'Providers'])[1]"
    button_providers_Last_name_xpath = "//*[@id='providersAccordion:providerMultiSearchForm:providerSearchTabView:providerNameSearchView:practitionerLastName']"
    button_search_aerial_xpath = "(//span[@class='ui-button-text ui-c' and text() = 'Search Aerial'])"
    button_add_facility_xpath = "//*[@id='providersAccordion:providerSearchResultsForm:providerSearchResultsTable:searchResultsTable:3:selectProvider']"
    button_select_Servicing_Provider_xpath = "//*[@id='providersAccordion:providersForm:requestProviders:providersDataTable:0:providerRoleListEven']/tbody/tr[2]/td[2]/div/div[2]/span"
    button_Diagnoses_Description_xpath = "//*[@id='diagnosesForm:requestBHDiagnoses:diagnosisSearchDescription']"
    button_Diagnoses_tab_xpath = "//span[@class='ui-menuitem-text' and text()='Diagnoses']"
    button_Diagnoses_dropdown_xpath  = "//*[@id='diagnosesForm:requestBHDiagnoses:diagnosisQuickList']/div[3]"
    button_Diagnoses_dropdown_value_xpath = "//*[@id='diagnosesForm:requestBHDiagnoses:diagnosisQuickList_2']"
    button_search_diagnoses_xpath = "//*[@id='diagnosesForm:requestBHDiagnoses:searchDiagnosesButton']/span"
    button_diagnoses_checkbox_xpath = "//*[@id='diagnosesForm:requestBHDiagnoses:axisIVProblems']/tbody/tr[1]/td[1]/div/div[2]/span"
    button_diagnoses_add_xpath = "//*[@id='diagnosesForm:requestBHDiagnoses:diagnosisSearchResultsTable:0:addDiagnosisLink']/span[2]"
    button_diagnoses_score_xpath = "//*[@id='diagnosesForm:requestBHDiagnoses:axisVScore']"
    button_diagnoses_scorevalue_add_xpath = "//span[@class='ui-button-text ui-c' and text()='Add']"
    button_select_services_tab_xpath = "//span[@class='ui-menuitem-text' and text()='Services']"
    button_service_dropdown_xpath = "//*[@id='requestProcedureSearch:procedureSearchForm:procedureQuickList_label']"
    button_service_dropdown_value_xpath = "//*[@id='requestProcedureSearch:procedureSearchForm:procedureQuickList_1']"
    button_select_service_add_xpath = "//span[@class='ui-button-text ui-c' and text()='Add']"
    button_service_tab_xpath = "//*[@id='menuForm:requestSectionMenu']/ul/li[6]"
    button_Treatment_type_xpath = "//*[@id='serviceDetailsForm:treatmentType_label']"
    button_Treatment_type_dropdown_xpath = "//*[@id='serviceDetailsForm:treatmentType_2']"
    button_startdate_xpath = "//*[@id='serviceDetailsForm:startDate_input']"
    button_request_units_xpath = "//*[@id='serviceDetailsForm:requestedUnits']"
    button_Review_tab_xpath = "(//*[@class='ui-menuitem-link ui-corner-all'])[3]"
    button_mcg_page_xpath = "//*[@id='MainContent_cgxGuidelineSearchCriteria_rsltsGrid_rptSearchRelated_rptSearchRows_0_rptSearchCells_0_lblData_19']"
    button_mcg_episode_page_xpath = "//*[@id='MainContent_cgxEpisodeOverview_btnExitEpisode']"
    textbox_review_To_Date = "//*[@id='reviewAccordion:newOutcomeForm:newOutcomeAccordion:serviceReviewOutcomeEntry:toDate_input']"
    button_review_status_dropdown = "//*[@id='reviewAccordion:newOutcomeForm:newOutcomeAccordion:serviceReviewOutcomeEntry:outcomeStatus_label']"
    button_status_dropdown_value = "//*[@data-label='Approve']"
    button_click_Add_outcome = "//*[@class='ui-button-text ui-c' and text()= 'Add Outcome']"
    button_save_exit_OP_req_text = "//*[@class='ui-button-text ui-c' and text() ='Save & Exit']"
    button_title_home_xpath = "//a[@title='Home']"
    button_BHPA_save_exit_text = "//*[@class='ui-button-text ui-c' and text() ='Save & Exit']"

    def __init__(self, driver):
        self.driver = driver

    def click_Refferal_BH(self):
        self.driver.find_element(By.XPATH, self.button_BHPA_text).click()

    def clickBHPA_Urgency(self):
        self.driver.find_element(By.XPATH, self.button_BHPA_Urgency_id).click()

    def clickBHPA_Urgency_type(self):
        self.driver.find_element(By.XPATH, self.button_BHPA_Urgency_type_xpath).click()

    def click_Providers_tab(self):
        self.driver.find_element(By.XPATH, self.button_Providers_tab_xpath).click()

    def clickproviders_Last_name(self, facility):
        self.driver.find_element(By.XPATH, self.button_providers_Last_name_xpath).send_keys(facility)

    def click_search_aerial(self):
        self.driver.find_element(By.XPATH, self.button_search_aerial_xpath).click()

    def clickadd_facility(self):
        self.driver.find_element(By.XPATH, self.button_add_facility_xpath).click()

    def click_select_Servicing_Provider(self):
        self.driver.find_element(By.XPATH, self.button_select_Servicing_Provider_xpath).click()

    def click_Diagnoses_tab(self):
        self.driver.find_element(By.XPATH, self.button_Diagnoses_tab_xpath).click()

    def click_Diagnoses_Description_click(self):
        self.driver.find_element(By.XPATH, self.button_Diagnoses_Description_xpath).click()

    def click_Diagnoses_Description(self, Description):
        self.driver.find_element(By.XPATH, self.button_Diagnoses_Description_xpath).send_keys(Description)

    def click_Diagnoses_dropdown(self):
        self.driver.find_element(By.XPATH, self.button_Diagnoses_dropdown_xpath).click()

    def click_Diagnoses_dropdown_value(self):
        self.driver.find_element(By.XPATH, self.button_Diagnoses_dropdown_value_xpath).click()

    def click_search_diagnoses(self):
        self.driver.find_element(By.XPATH, self.button_search_diagnoses_xpath).click()

    def clickdiagnoses_checkbox(self):
        self.driver.find_element(By.XPATH, self.button_diagnoses_checkbox_xpath).click()

    def clickdiagnoses_add(self):
        self.driver.find_element(By.XPATH, self.button_diagnoses_add_xpath).click()

    def clickdiagnoses_score(self):
        self.driver.find_element(By.XPATH, self.button_diagnoses_score_xpath).click()

    def get_diagnoses_scorevalue(self, diagnoses_score):
        self.driver.find_element(By.XPATH, self.button_diagnoses_score_xpath).send_keys(diagnoses_score)

    def get_diagnoses_scorevalue_add(self):
        self.driver.find_element(By.XPATH, self.button_diagnoses_scorevalue_add_xpath).click()

    def clickselect_services_tab(self):
        self.driver.find_element(By.XPATH, self.button_select_services_tab_xpath).click()

    def clickservice_dropdown(self):
        self.driver.find_element(By.XPATH, self.button_service_dropdown_xpath).click()

    def click_service_dropdown_value(self):
        self.driver.find_element(By.XPATH, self.button_service_dropdown_value_xpath).click()

    def click_select_service_add(self):
        self.driver.find_element(By.XPATH, self.button_select_service_add_xpath).click()

    def click_service_tab(self):
        self.driver.find_element(By.XPATH, self.button_service_tab_xpath).click()

    def click_Treatment_setting_service(self):
        self.driver.find_element(By.XPATH, self.button_Treatment_type_xpath).click()

    def click_Treatment_setting_dropdown(self):
        self.driver.find_element(By.XPATH, self.button_Treatment_type_dropdown_xpath).click()

    def click_startdate(self, start_date):
        self.driver.find_element(By.XPATH, self.button_startdate_xpath).send_keys(start_date)

    def click_request_units(self):
        self.driver.find_element(By.XPATH, self.button_request_units_xpath).click()

    def set_request_units_service(self, requested_units):
        self.driver.find_element(By.XPATH, self.button_request_units_xpath).send_keys(requested_units)

    def clickReview_tab(self):
        self.driver.find_element(By.XPATH, self.button_Review_tab_xpath).click()

    def clickmcg_page(self):
        self.driver.find_element(By.XPATH, self.button_mcg_page_xpath).click()

    def clickmcg_episode_page(self):
        self.driver.find_element(By.XPATH, self.button_mcg_episode_page_xpath).click()

    def set_review_To_Date(self, To_Date):
        self.driver.find_element(By.XPATH, self.textbox_review_To_Date).send_keys(To_Date)

    def clickreview_status_dropdown(self):
        self.driver.find_element(By.XPATH, self.button_review_status_dropdown).click()

    def click_dropdown_value(self):
        self.driver.find_element(By.XPATH, self.button_status_dropdown_value).click()

    def clickAdd_outcome(self):
        self.driver.find_element(By.XPATH, self.button_click_Add_outcome).click()

    def clicksave(self):
        self.driver.find_element(By.XPATH, self.button_save_exit_OP_req_text).click()

    def clicktitle_home(self):
        self.driver.find_element(By.XPATH, self.button_title_home_xpath).click()

    def clickBHPA_save_exit(self):
        self.driver.find_element(By.XPATH, self.button_BHPA_save_exit_text).click()