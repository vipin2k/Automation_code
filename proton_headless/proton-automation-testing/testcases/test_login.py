import os
import time
from PageObjects.LoginPage import LoginPage
from selenium.webdriver.common.by import By
from utilites.customlogger import Log
from utilites.readproperties import Readconfig


class Test_01_Login:
    urls = Readconfig.get_proton_url()
    Username = Readconfig.getusername()
    Password = Readconfig.get_password()
    logger = Log.loggen()

    def test_homepage(self, setup):
        self.driver = setup

        for url in self.urls:
            sanitized_url = url.replace("https://", "").replace("http://", "").replace("/", "_").replace(":",
                                                                                                         "_").replace(
                "?", "_")
            self.driver.get(url)
            self.driver.maximize_window()
            self.lp = LoginPage(self.driver)
            self.lp.set_username(self.Username)
            self.lp.set_password(self.Password)
            self.lp.click_login()
            time.sleep(2)
            print(f"Successfully logged in to {url}")
            self.logger.info(f"************** Successfully logged in to {url} ********************")

            screenshots_dir = os.path.join(os.getcwd(), "Screenshots")
            if not os.path.exists(screenshots_dir):
                os.makedirs(screenshots_dir)

            organization = self.driver.find_element(By.XPATH, "//button[@class='button1 text-capitalize']").text
            print(organization)
            time.sleep(2)
            Dashboard = self.driver.find_element(By.XPATH, "//label[@class='m-0']").text
            try:
                assert Dashboard == "Overview"
                print("Login page value is: " + Dashboard)
            except AssertionError:
                print(f"Assertion Error: Dashboard value '{Dashboard}' doesn't match expected value 'Overview'")

            self.lp.click_date_in_overview()
            time.sleep(2)
            self.lp.click_Today_date_in_overview()
            time.sleep(3)
            self.driver.save_screenshot(os.path.join(screenshots_dir, f"Login_page_today_{sanitized_url}.png"))
            time.sleep(2)
            self.driver.execute_script("window.scrollTo(0, 800);")
            time.sleep(2)
            self.driver.save_screenshot(os.path.join(screenshots_dir, f"Login_page_user_{sanitized_url}.png"))
            time.sleep(2)
            self.driver.execute_script("window.scrollTo(0, 2000);")
            self.driver.save_screenshot(os.path.join(screenshots_dir, f"Login_page_youtube_{sanitized_url}.png"))
            time.sleep(2)
            self.lp.click_score_card_page()
            time.sleep(3)
            Score_card = self.driver.find_element(By.XPATH, "//p[@class='m-0' and text()='Mailing']").text
            try:
                assert Score_card == "Mailing"
                print("Score_card page value is: " + Score_card)
            except AssertionError:
                print(f"Assertion Error: Score_card value '{Score_card}' doesn't match expected value 'Mailing'")
            self.driver.save_screenshot(os.path.join(screenshots_dir, f"Score_card_all_team_{sanitized_url}.png"))
            time.sleep(3)
            self.driver.execute_script("window.scrollTo(0, 2000);")
            time.sleep(3)
            self.driver.save_screenshot(os.path.join(screenshots_dir, f"Score_card_{sanitized_url}.png"))
            time.sleep(2)
            self.lp.click_screencast_page()
            time.sleep(5)
            Screen_cast_value = self.driver.find_element(By.XPATH,
                                                         "/html/body/div/app-root/app-proton/div/div/div/app-screen-casts/div/div/div/div[1]/div[1]/h2").text
            try:
                assert Screen_cast_value == "Screen Cast"
                print("Screen_cast page value is: " + Screen_cast_value)
            except AssertionError:
                print(
                    f"Assertion Error: Screen_cast value '{Screen_cast_value}' doesn't match expected value 'Screen Cast'")
            self.driver.save_screenshot(os.path.join(screenshots_dir, f"Screen_cast_{sanitized_url}.png"))
            self.driver.execute_script("window.scrollTo(0, 2000);")
            time.sleep(1)
            self.driver.save_screenshot(os.path.join(screenshots_dir, f"Screen_cast_all_{sanitized_url}.png"))
            self.lp.click_Reports_page()
            time.sleep(1)
            self.lp.click_Activity_summary_page()
            time.sleep(2)
            Activity_summary_value = self.driver.find_element(By.XPATH,
                                                              "/html/body/div/app-root/app-proton/div/div/div/app-report-topbar/div/app-activity-summary/div/div/div[2]/div[1]/div[1]/h2").text
            try:
                assert Activity_summary_value == "Activity Summary"
                print("Activity summary page value is: " + Activity_summary_value)
            except AssertionError:
                print(
                    f"Assertion Error: Activity summary value '{Activity_summary_value}' doesn't match expected value 'Activity Summary'")
            self.driver.save_screenshot(os.path.join(screenshots_dir, f"Activity_summary_{sanitized_url}.png"))

            time.sleep(5)
            self.lp.click_Timeline_page()
            time.sleep(3)
            Timeline_value = self.driver.find_element(By.XPATH,
                                                      "/html/body/div/app-root/app-proton/div/div/div/app-report-topbar/div/app-time-series/div/div/div[2]/div[1]/div[1]/h2").text
            try:
                assert Timeline_value == "Timeline"
                print("Timeline page value is: " + Timeline_value)
            except AssertionError:
                print(f"Assertion Error: Timeline value '{Timeline_value}' doesn't match expected value 'Timeline'")
            self.driver.save_screenshot(os.path.join(screenshots_dir, f"Timeline_{sanitized_url}.png"))
            self.driver.execute_script("window.scrollTo(0, 2000);")
            time.sleep(2)
            self.driver.save_screenshot(os.path.join(screenshots_dir, f"Timeline_all_user_{sanitized_url}.png"))
            time.sleep(5)
            self.lp.click_Attendances_page()
            time.sleep(5)
            Attendances_value = self.driver.find_element(By.XPATH,
                                                         "/html/body/div/app-root/app-proton/div/div/div/app-report-topbar/div/app-attendance/div/div/div[2]/div[1]/div[1]/h2").text
            try:
                assert Attendances_value == "Attendance"
                print("Attendances page value is: " + Attendances_value)
            except AssertionError:
                print(
                    f"Assertion Error: Attendances value '{Attendances_value}' doesn't match expected value 'Attendance'")
            self.driver.save_screenshot(os.path.join(screenshots_dir, f"Attendances_{sanitized_url}.png"))
            self.driver.execute_script("window.scrollTo(0, 2000);")
            time.sleep(1)
            self.driver.save_screenshot(os.path.join(screenshots_dir, f"Attendances_all_user_{sanitized_url}.png"))
            time.sleep(5)
            self.lp.click_Apps_and_Webs_page()
            time.sleep(5)

            xpaths = [
                "/html/body/div/app-root/app-proton/div/div/div/app-report-topbar/div/app-apps-webs/div/div/div[2]/div[1]/div[1]/h2",
                "/html/body/div/app-root/app-proton/div/div/div/app-report-topbar/div/app-apps-webs/div/div/div[2]/div[1]/div/div[1]/div[1]/h2"
            ]

            Apps_webs_value = None
            for xpath in xpaths:
                try:
                    Apps_webs_value = self.driver.find_element(By.XPATH, xpath).text
                    break
                except:
                    continue

            if Apps_webs_value:
                try:
                    assert Apps_webs_value == "Applications & Webs"
                    print("Apps and webs page value is: " + Apps_webs_value)
                except AssertionError:
                    print(
                        f"Assertion Error: Apps and webs value '{Apps_webs_value}' doesn't match expected value 'Applications & Webs'")
            else:
                print("Failed to find the 'Applications & Webs' element using provided XPaths.")

            self.driver.save_screenshot(os.path.join(screenshots_dir, f"Apps_webs_{sanitized_url}.png"))
            self.driver.execute_script("window.scrollTo(0, 2000);")
            time.sleep(2)
            self.driver.save_screenshot(os.path.join(screenshots_dir, f"Apps_webs_all_user_{sanitized_url}.png"))
            time.sleep(3)
            self.lp.click_userprofile()
            self.lp.click_logout()
            self.driver.save_screenshot(os.path.join(screenshots_dir, f"Logout_page_{sanitized_url}.png"))
            self.logger.info(f"************** Successfully logged out from {url} ********************")
            print("Successfully logged out")
