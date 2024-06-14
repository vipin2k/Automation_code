import time
from selenium.webdriver.common.by import By
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
import os
import re
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load data from JSON file
with open("./testcases/values.json") as file:
    data = json.load(file)

# List of URLs to test
urls = [data.get("proton_Dev_url"), data.get("proton_Demo_url"), data.get("proton_Prod_url")]

# Filter out None values in case some URLs are missing
urls = [url for url in urls if url]

# Create screenshot directory if it doesn't exist
screenshot_dir = "./screenshot"
os.makedirs(screenshot_dir, exist_ok=True)


# Pytest fixture to initialize and quit the WebDriver
@pytest.fixture(scope="module")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Enable headless mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()


# Test function to run tests on all URLs
def test_proton(driver):
    for url in urls:
        run_test_proton(driver, url)


# Function to perform the test on a single URL
def run_test_proton(driver, url):
    try:
        driver.get(url)
        driver.find_element(By.XPATH, "//input[@placeholder='Email']").send_keys(data["Username"])
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='password']").send_keys(data["Password"])
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@type='submit']").click()
        time.sleep(5)
        login_status = "Login successfully"
        print(login_status)
        logger.info(f"{url}: {login_status}")
        save_screenshot(driver, f"Login_page_{sanitize_filename(url)}.png")

        driver.find_element(By.XPATH, "//*[@class='p-dropdown-trigger-icon ng-tns-c68-3 pi pi-chevron-down']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@aria-label='Today']").click()
        time.sleep(3)
        save_screenshot(driver, f"Today_Dashboard_{sanitize_filename(url)}.png")

        driver.find_element(By.XPATH, "//*[@class='dropdown-toggle nav-link ng-star-inserted']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@class='feather feather-log-out icon-dual icon-xs mr-2']").click()
        time.sleep(5)
        logout_status = "Logout successfully"
        print(logout_status)
        logger.info(f"{url}: {logout_status}")
        save_screenshot(driver, f"Logout_page_{sanitize_filename(url)}.png")

    except Exception as e:
        error_message = f"An error occurred while testing {url}: {e}"
        print(error_message)
        logger.error(error_message)


# Helper function to save screenshots
def save_screenshot(driver, filename):
    try:
        path = os.path.join(screenshot_dir, filename)
        print(f"Saving screenshot to: {path}")
        driver.save_screenshot(path)
    except Exception as e:
        error_message = f"Error saving screenshot: {e}"
        print(error_message)
        logger.error(error_message)


# Helper function to sanitize filenames
def sanitize_filename(url):
    return re.sub(r'[^\w\-_\. ]', '_', url.split('//')[1])
