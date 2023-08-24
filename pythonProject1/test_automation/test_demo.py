from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import pytest

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("headless")
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.apple.com/in/")
# driver.implicitly_wait(15)


# time.sleep(2)

def test_airpods_compare():
    driver.find_element(By.XPATH, "//a[@class='ac-gn-link ac-gn-link-airpods']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//*[@class='chapternav-item chapternav-item-airpods-compare']").click()
    time.sleep(3)
    driver.implicitly_wait(15)
    driver.get_screenshot_as_file("screenshots/screenshot1.png")
    print("Airpods compare Successfully")


def test_select_airpods_types():
    driver.find_element(By.XPATH, "//*[@id='selector-0']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "(//*[@value='9FGnsPAg' and text()='AirPods (3rd generation) with MagSafe Charging "
                                  "Case'])[1]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='selector-1']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "(//*[@value='OxCPGeVO' and text()='AirPods Max'])[1]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@class='colornav-swatch colornav-swatch-pink']").click()
    print("Successfully test completed")
    time.sleep(1)
    driver.get_screenshot_as_file("screenshots/screenshots2.png")
    driver.close()
    driver.quit()




