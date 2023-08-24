from selenium import webdriver
from selenium.webdriver.common.by import By

class Medical_IP_Request_CreationPage:
    button_Medical_Inpatient_text = "//*[@class='ui-menuitem-text' and text() = 'Medical Inpatient']"
    button_treatment_id = "//*[@id='requestForm:treatmentSetting_label']"
    button_treatment_setting_xpath = "//*[@data-label='Inpatient']"
    button_treatment_type_id = "requestForm:treatmentType_label"
    textbox_request_treatment_type_xpath = "//*[@data-label='Medical']"
    textbox_Admit_date_xpath = "(//*[@class='ui-inputfield ui-widget ui-state-default ui-corner-all hasDatepicker'])[1]"
    textbox_request_name = "//*[@name='requestForm:requestedUnits']"
    textbox_request_units_name = "//*[@name='requestForm:requestedUnits']"
    button_urgency_xpath = "(//*[@class='ui-icon ui-icon-triangle-1-s ui-c'])[5]"
    textbox_urgency_type_name = "//*[@data-label='Emergency']"
    button_providers_text = "(//span[@class='ui-menuitem-text' and text()='Providers'])[1]"
    textbox_facility_name = "//*[@id='providersAccordion:providerMultiSearchForm:providerSearchTabView:providerNameSearchView:facilityName']"
    button_search_aerial_xpath = "//*[@class='ui-button-text ui-c' and text()= 'Search Aerial']"
    button_add_facility_xpath = "(//*[@class='ui-button-text ui-c' and text()= 'Add'])[6]"
    button_select_facility_xpath = "(//*[@class='ui-chkbox-box ui-widget ui-corner-all ui-state-default'])[2]"
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
    button_servicing_provider_dropdown = "(//*[@class='ui-selectonemenu-trigger ui-state-default ui-corner-right'])[4]"
    select_servicing_provider_dropdown_value = "//*[@id='serviceDetailsForm:servicingProvider_1']"
    button_Review_tab_xpath = "(//*[@class='ui-menuitem-text' and text()='Review'])[1]"
    button_mcg_page_xpath = "//*[@id='MainContent_cgxGuidelineSearchCriteria_rsltsGrid_rptSearchRelated_rptSearchRows_0_rptSearchCells_0_lblData_19']"
    button_mcg_episode_page_xpath = "//*[@id='MainContent_cgxEpisodeOverview_btnExitEpisode']"
    button_review_status_dropdown = "//*[@id='reviewAccordion:newOutcomeForm:newOutcomeAccordion:outcomeStatus_label']"
    button_status_dropdown_value = "//*[@data-label='Approve']"
    button_status_reason_dropdown_id = "reviewAccordion:newOutcomeForm:newOutcomeAccordion:statusReason_label"
    button_status_reason_dropdown_value = "//*[@data-label='Clinical Criteria Met']"
    button_click_Add_outcome = "//*[@class='ui-button-text ui-c' and text()= 'Add Outcome']"
    button_extend_xpath = "//*[@class='ui-button-text ui-c' and text()= 'Extend']"
    button_save_text = "//*[@class='ui-button-text ui-c' and text() ='Save & Exit']"
    select_service_tab_extension_xpath = "//*[@class='ui-tabs-header ui-state-default ui-corner-top']"
    select_services_edit_request_xpath = "//*[@class='ui-button-text ui-c' and text()= 'Edit Request']"
    button_title_home_xpath = "//a[@title='Home']"

    def __init__(self, driver):
        self.driver = driver

    def clickMedical(self):
        self.driver.find_element(By.XPATH, self.button_Medical_Inpatient_text).click()

    def clickTreatment(self):
        self.driver.find_element(By.XPATH, self.button_treatment_id).click()

    def clickTreatmentsetting(self):
        self.driver.find_element(By.XPATH, self.button_treatment_setting_xpath).click()

    def clickTreatment_type(self):
        self.driver.find_element(By.ID, self.button_treatment_type_id).click()

    def clickRequest_treatment_type(self):
        self.driver.find_element(By.XPATH, self.textbox_request_treatment_type_xpath).click()

    def setAdmit_date(self, Admit_date):
        self.driver.find_element(By.XPATH, self.textbox_Admit_date_xpath).send_keys(Admit_date)

    def clickrequest_units(self):
        self.driver.find_element(By.XPATH, self.textbox_request_name).click()

    def setUnits(self, unit_date):
        self.driver.find_element(By.XPATH, self.textbox_request_units_name).send_keys(unit_date)

    def clickurgency(self):
        self.driver.find_element(By.XPATH, self.button_urgency_xpath).click()

    def clickurgency_type(self):
        self.driver.find_element(By.XPATH, self.textbox_urgency_type_name).click()

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

    def click_servicing_provider_dropdown(self):
        self.driver.find_element(By.XPATH, self.button_servicing_provider_dropdown).click()

    def click_servicing_provider_dropdown_value(self):
        self.driver.find_element(By.XPATH, self.select_servicing_provider_dropdown_value).click()

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

    def clickextend(self):
        self.driver.find_element(By.XPATH, self.button_extend_xpath).click()

    def clicksave(self):
        self.driver.find_element(By.XPATH, self.button_save_text).click()

    def clicktitle_home(self):
        self.driver.find_element(By.XPATH, self.button_title_home_xpath).click()