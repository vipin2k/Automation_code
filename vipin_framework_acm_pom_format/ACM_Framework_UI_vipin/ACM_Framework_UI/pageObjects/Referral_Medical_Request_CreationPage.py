from selenium import webdriver
from selenium.webdriver.common.by import By

class Referral_Medical_Request_CreationPage:
    button_Referral_Medical_text = "//*[@class='ui-menuitem-text' and text() = 'Medical Referral']"
    button_treatment_id = "//*[@id='requestForm:treatmentSetting_label']"
    button_treatment_setting_xpath = "//*[@data-label='Inpatient']"
    button_treatment_type_id = "//*[@id='requestForm:treatmentType']/div[3]"
    textbox_request_treatment_type_xpath = "//*[@data-label='Medical']"
    # textbox_Admit_date_xpath = "(//*[@class='ui-inputfield ui-widget ui-state-default ui-corner-all hasDatepicker'])[1]"
    textbox_request_name = "//*[@name='requestForm:requestedUnits']"
    textbox_request_units_name = "//*[@name='requestForm:requestedUnits']"
    textbox_request_start_date = "//*[@id='requestForm:startDate_input']"
    button_providers_text = "(//span[@class='ui-menuitem-text' and text()='Providers'])[1]"
    textbox_facility_name = "//*[@id='providersAccordion:providerMultiSearchForm:providerSearchTabView:providerNameSearchView:practitionerLastName']"
    button_search_aerial_xpath = "//*[@class='ui-button-text ui-c' and text()= 'Search Aerial']"
    button_add_facility_xpath = "(//*[@class='ui-button-text ui-c' and text()= 'Add'])[6]"
    button_select_servicing_provider_facility_xpath = "//*[@id='providersAccordion:providersForm:requestProviders:providersDataTable:0:providerRoleList']/tbody/tr[4]/td/div/div[2]"
    button_select_referring_provider_facility_xpath = "//*[@id='providersAccordion:providersForm:requestProviders:providersDataTable:0:providerRoleList']/tbody/tr[3]/td/div/div[2]"
    button_select_diagnoses_xpath = "//*[@class='ui-menuitem-text' and text()= 'Diagnoses']"
    button_diagnoses_dropdown = "//*[@class='ui-selectonemenu-trigger ui-state-default ui-corner-right']"
    button_select_diagnoses_dropdown = "(//*[@class='ui-selectonemenu-item ui-selectonemenu-list-item ui-corner-all'])[3]"
    button_select_diagnosis_add = "(//*[@class='ui-button-text ui-c' and text()='Add'])[1]"
    button_select_services_xpath = "//*[@class='ui-menuitem-text' and text()= 'Services']"
    button_click_service_dropdown = "//*[@class='ui-icon ui-icon-triangle-1-s ui-c']"
    button_select_service_dropdown = "(//*[@class='ui-selectonemenu-item ui-selectonemenu-list-item ui-corner-all'])[3]"
    button_select_service_add = "//*[@class='ui-button-text ui-c' and text() = 'Add']"
    button_select_service_scheme = "//*[@class='ui-menuitem-link ui-corner-all requestNavigationMenuItem requestNavigationIconNone requestNavigationMenuItemService']"
    button_servicing_provider_dropdown = "(//*[@class='ui-selectonemenu-trigger ui-state-default ui-corner-right'])[4]"
    select_servicing_provider_dropdown_value = "//*[@id='serviceDetailsForm:servicingProvider_1']"
    button_Review_tab_xpath = "(//*[@class='ui-menuitem-text' and text()= 'Review'])[1]"
    click_button_to_date_xpath = "//*[@id='reviewAccordion:newOutcomeForm:newOutcomeAccordion:serviceReviewOutcomeEntry:toDate_input']"
    button_To_date_xpath = "//*[@id='reviewAccordion:newOutcomeForm:newOutcomeAccordion:serviceReviewOutcomeEntry:toDate_input']"
    button_review_status_dropdown = "//*[@id='reviewAccordion:newOutcomeForm:newOutcomeAccordion:serviceReviewOutcomeEntry:outcomeStatus_label']"
    button_status_dropdown_value = "//*[@data-label='Approve']"
    # button_status_reason_dropdown_id = "reviewAccordion:newOutcomeForm:newOutcomeAccordion:statusReason_label"
    # button_status_reason_dropdown_value = "//*[@data-label='Clinical Criteria Met']"
    button_click_Add_outcome = "//*[@class='ui-button-text ui-c' and text()= 'Add Outcome']"
    button_extend_xpath = "//*[@class='ui-button-text ui-c' and text()= 'Extend']"
    button_save_text = "//*[@class='ui-button-text ui-c' and text() ='Save & Exit']"
    select_service_tab_extension_xpath = "//*[@class='ui-tabs-header ui-state-default ui-corner-top']"
    select_services_edit_request_xpath = "//*[@class='ui-button-text ui-c' and text()= 'Edit Request']"
    button_title_home_xpath = "//a[@title='Home']"

    def __init__(self, driver):
        self.driver = driver

    def clickMedical(self):
        self.driver.find_element(By.XPATH, self.button_Referral_Medical_text).click()

    def clickTreatment(self):
        self.driver.find_element(By.XPATH, self.button_treatment_id).click()

    def clickTreatmentsetting(self):
        self.driver.find_element(By.XPATH, self.button_treatment_setting_xpath).click()

    def clickTreatment_type(self):
        self.driver.find_element(By.XPATH, self.button_treatment_type_id).click()

    def clickRequest_treatment_type(self):
        self.driver.find_element(By.XPATH, self.textbox_request_treatment_type_xpath).click()

    def click_request_units(self):
        self.driver.find_element(By.XPATH, self.textbox_request_name).click()

    def set_requested_units(self, requested_units):
        self.driver.find_element(By.XPATH, self.textbox_request_units_name).send_keys(requested_units)

    def click_start_date(self):
        self.driver.find_element(By.XPATH, self.textbox_request_start_date).click()

    def set_start_date(self, start_date):
        self.driver.find_element(By.XPATH, self.textbox_request_start_date).send_keys(start_date)

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

    def click_select_referring_provider_facility(self):
        self.driver.find_element(By.XPATH, self.button_select_referring_provider_facility_xpath).click()

    def click_select_servicing_provider_facility(self):
        self.driver.find_element(By.XPATH, self.button_select_servicing_provider_facility_xpath).click()

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

    def click_To_date(self):
        self.driver.find_element(By.XPATH, self.click_button_to_date_xpath).click()

    def set_To_date(self, To_date):
        self.driver.find_element(By.XPATH, self.button_To_date_xpath).send_keys(To_date)

    def clickreview_status_dropdown(self):
        self.driver.find_element(By.XPATH, self.button_review_status_dropdown).click()

    def click_dropdown_value(self):
        self.driver.find_element(By.XPATH, self.button_status_dropdown_value).click()

    # def click_reason_dropdown_id(self):
    #     self.driver.find_element(By.XPATH, self.button_status_reason_dropdown_id).click()
    #
    # def clickreason_dropdown_value(self):
    #     self.driver.find_element(By.XPATH, self.button_status_reason_dropdown_value).click()

    def clickAdd_outcome(self):
        self.driver.find_element(By.XPATH, self.button_click_Add_outcome).click()

    def clickextend(self):
        self.driver.find_element(By.XPATH, self.button_extend_xpath).click()

    def clicksave(self):
        self.driver.find_element(By.XPATH, self.button_save_text).click()

    def clicktitle_home(self):
        self.driver.find_element(By.XPATH, self.button_title_home_xpath).click()