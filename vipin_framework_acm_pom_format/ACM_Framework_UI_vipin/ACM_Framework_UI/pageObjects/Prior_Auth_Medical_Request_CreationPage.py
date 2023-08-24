from selenium import webdriver
from selenium.webdriver.common.by import By

class Prior_Auth_Medical_Request_CreationPage:
    button_Medical_Prior_Auth_text = "//*[@class='ui-menuitem-text' and text() = 'Medical Prior Auth']"
    button_treatment_setting_dropdown = "(//*[@class='ui-selectonemenu-trigger ui-state-default ui-corner-right'])[1]"
    button_treatment_setting_dropdown_value = "(//*[@class='ui-selectonemenu-item ui-selectonemenu-list-item ui-corner-all'])[1]"
    button_urgency_dropdown = "//*[@id='requestForm:urgency_label']"
    button_urgency_dropdown_value = "//*[@data-label='Emergency']"
    button_providers_text = "//*[@id='menuForm:requestSectionMenu']/ul/li[3]/a/span"
    textbox_facility_name = "//*[@id='providersAccordion:providerMultiSearchForm:providerSearchTabView:providerNameSearchView:practitionerLastName']"
    button_search_aerial_xpath = "//*[@class='ui-button-text ui-c' and text()= 'Search Aerial']"
    button_add_facility_xpath = "(//*[@class='ui-button-text ui-c' and text()= 'Add'])[6]"
    button_select_facility_xpath = "//*[@id='providersAccordion:providersForm:requestProviders:providersDataTable:0:providerRoleListEven']/tbody/tr[2]/td[2]/div/div[2]"
    button_select_diagnoses_xpath = "//*[@class='ui-menuitem-text' and text()= 'Diagnoses']"
    button_diagnoses_dropdown = "//*[@class='ui-selectonemenu-trigger ui-state-default ui-corner-right']"
    button_select_diagnoses_dropdown = "(//*[@class='ui-selectonemenu-item ui-selectonemenu-list-item ui-corner-all'])[3]"
    button_select_diagnosis_add = "(//*[@class='ui-button-text ui-c' and text()='Add'])[1]"
    button_select_services_xpath = "//*[@class='ui-menuitem-text' and text()= 'Services']"
    button_click_service_dropdown = "//*[@class='ui-icon ui-icon-triangle-1-s ui-c']"
    button_select_service_dropdown = "(//*[@class='ui-selectonemenu-item ui-selectonemenu-list-item ui-corner-all'])[3]"
    button_select_service_add = "//*[@class='ui-button-text ui-c' and text() = 'Add']"
    button_select_service_scheme = "//*[@class='ui-menuitem-link ui-corner-all requestNavigationMenuItem requestNavigationIconNone requestNavigationMenuItemService']"
    button_service_treatment_dropdown = "(//*[@class='ui-selectonemenu-trigger ui-state-default ui-corner-right'])[1]"
    select_service_treatment_dropdown_value = "(//*[@class='ui-selectonemenu-item ui-selectonemenu-list-item ui-corner-all'])[5]"
    button_service_start_date_xpath = "//*[@id='serviceDetailsForm:startDate_input']"
    click_textbox_request_units_name = "//*[@id='serviceDetailsForm:requestedUnits']"
    textbox_request_units_name = "//*[@id='serviceDetailsForm:requestedUnits']"
    button_review_tab_xpath = "//*[@id='serviceMenuForm:reviewMenuItem']"
    button_select_mcg_page_xpath = "//*[@id='MainContent_cgxGuidelineSearchCriteria_rsltsGrid_rptSearchRelated_rptSearchRows_0_rptSearchCells_0_lblData_19']/a"
    button_mcg_episode_page = "//*[@id='MainContent_cgxEpisodeOverview_btnExitEpisode']"
    button_review_TODATE_xpath = "//*[@id='reviewAccordion:newOutcomeForm:newOutcomeAccordion:serviceReviewOutcomeEntry:toDate_input']"
    button_review_status_dropdown = "(//*[@class='ui-icon ui-icon-triangle-1-s ui-c'])[1]"
    button_review_status_dropdown_value_type = "//*[@id='reviewAccordion:newOutcomeForm:newOutcomeAccordion:serviceReviewOutcomeEntry:outcomeStatus_1']"
    button_click_Add_outcome = "//*[@class='ui-button-text ui-c' and text()= 'Add Outcome']"
    button_save_text = "//*[@class='ui-button-text ui-c' and text() ='Save & Exit']"
    button_extend_xpath = "//*[@class='ui-button-text ui-c' and text()= 'Extend']"
    select_services_edit_request_xpath = "//*[@class='ui-button-text ui-c' and text()= 'Edit Request']"
    button_title_home_xpath = "//a[@title='Home']"


    def __init__(self, driver):
        self.driver = driver

    def clickMedical(self):
        self.driver.find_element(By.XPATH, self.button_Medical_Prior_Auth_text).click()

    def click_treatment_setting_dropdown(self):
        self.driver.find_element(By.XPATH, self.button_treatment_setting_dropdown).click()

    def click_treatment_setting_dropdown_value(self):
        self.driver.find_element(By.XPATH, self.button_treatment_setting_dropdown_value).click()

    def clickurgency_dropdown(self):
        self.driver.find_element(By.XPATH, self.button_urgency_dropdown).click()

    def clickurgency_dropdown_value(self):
        self.driver.find_element(By.XPATH, self.button_urgency_dropdown_value).click()

    def clickproviders(self):
        self.driver.find_element(By.XPATH, self.button_providers_text).click()

    def clickfacility(self):
        self.driver.find_element(By.XPATH, self.textbox_facility_name).click()

    def setfacility(self, facility):
        self.driver.find_element(By.XPATH, self.textbox_facility_name).send_keys(facility)

    def clicksearch_aerial(self):
        self.driver.find_element(By.XPATH, self.button_search_aerial_xpath).click()

    def click_add_facility(self):
        self.driver.find_element(By.XPATH, self.button_add_facility_xpath).click()

    def click_select_facility(self):
        self.driver.find_element(By.XPATH, self.button_select_facility_xpath).click()

    def clickselect_diagnoses(self):
        self.driver.find_element(By.XPATH, self.button_select_diagnoses_xpath).click()

    def click_diagnoses_dropdown(self):
        self.driver.find_element(By.XPATH, self.button_diagnoses_dropdown).click()

    def click_select_diagnoses_dropdown(self):
        self.driver.find_element(By.XPATH, self.button_select_diagnoses_dropdown).click()

    def click_select_diagnosis_add(self):
        self.driver.find_element(By.XPATH, self.button_select_diagnosis_add).click()

    def click_select_services(self):
        self.driver.find_element(By.XPATH, self.button_select_services_xpath).click()

    def click_service_dropdown(self):
        self.driver.find_element(By.XPATH, self.button_click_service_dropdown).click()

    def click_select_service_dropdown(self):
        self.driver.find_element(By.XPATH, self.button_select_service_dropdown).click()

    def click_select_service_add(self):
        self.driver.find_element(By.XPATH, self.button_select_service_add).click()

    def click_select_service_scheme(self):
        self.driver.find_element(By.XPATH, self.button_select_service_scheme).click()

    def click_service_treatment_dropdown(self):
        self.driver.find_element(By.XPATH, self.button_service_treatment_dropdown).click()

    def click_service_treatment_dropdown_value(self):
        self.driver.find_element(By.XPATH, self.select_service_treatment_dropdown_value).click()

    def set_service_start_date(self, start_date):
        self.driver.find_element(By.XPATH, self.button_service_start_date_xpath).send_keys(start_date)

    def click_request_units(self):
        self.driver.find_element(By.XPATH, self.click_textbox_request_units_name).click()

    def set_request_units(self, requested_units):
        self.driver.find_element(By.XPATH, self.textbox_request_units_name).send_keys(requested_units)

    def click_review_tab(self):
        self.driver.find_element(By.XPATH, self.button_review_tab_xpath).click()

    def click_select_mcg_page(self):
        self.driver.find_element(By.XPATH, self.button_select_mcg_page_xpath).click()

    def click_mcg_episode(self):
        self.driver.find_element(By.XPATH, self.button_mcg_episode_page).click()

    def set_review_TO_DATE(self, To_date):
        self.driver.find_element(By.XPATH, self.button_review_TODATE_xpath).send_keys(To_date)

    def click_review_status_dropdown(self):
        self.driver.find_element(By.XPATH, self.button_review_status_dropdown).click()

    def click_review_status_dropdown_value(self):
        self.driver.find_element(By.XPATH, self.button_review_status_dropdown_value_type).click()

    def click_Add_outcome(self):
        self.driver.find_element(By.XPATH, self.button_click_Add_outcome).click()

    def clickextend(self):
        self.driver.find_element(By.XPATH, self.button_extend_xpath).click()

    def clicksave(self):
        self.driver.find_element(By.XPATH, self.button_save_text).click()

    def clicktitle_home(self):
        self.driver.find_element(By.XPATH, self.button_title_home_xpath).click()












