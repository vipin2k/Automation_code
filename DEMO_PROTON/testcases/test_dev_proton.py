import time

import webdriver_manager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import os
import re

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
    # Specify ChromeDriver port
    # chrome_driver_port = int(os.getenv('WEBDRIVER_CHROME_DRIVER_PORT', 9515))

    # Set ChromeDriver options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Enable headless mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    # chrome_options.add_argument(f'--remote-debugging-port={chrome_driver_port}')

    # Start ChromeDriver with specified port
    driver = webdriver.Chrome(executable_path=r"D:\vipin_test_automation\proton_headless\DEMO_PROTON\chromedriver-win64\chromedriver.exe", options=chrome_options)
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
        # Navigate to the URL
        driver.get(url)

        # Perform login
        driver.find_element(By.XPATH, "//input[@placeholder='Email']").send_keys(data["Username"])
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='password']").send_keys(data["Password"])
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@type='submit']").click()
        time.sleep(5)
        print("Login successfully")

        # Save login screenshot
        save_screenshot(driver, f"Login_page_{sanitize_filename(url)}.png")

        # Interact with dashboard
        driver.find_element(By.XPATH, "//*[@class='p-dropdown-trigger-icon ng-tns-c68-3 pi pi-chevron-down']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@aria-label='Today']").click()
        time.sleep(3)

        # Save dashboard screenshot
        save_screenshot(driver, f"Today_Dashboard_{sanitize_filename(url)}.png")

        # Perform logout
        driver.find_element(By.XPATH, "//*[@class='dropdown-toggle nav-link ng-star-inserted']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@class='feather feather-log-out icon-dual icon-xs mr-2']").click()
        time.sleep(5)

        # Save logout screenshot
        save_screenshot(driver, f"Logout_page_{sanitize_filename(url)}.png")
        print("Logout successfully")

    except Exception as e:
        print(f"An error occurred while testing {url}: {e}")


# Helper function to save screenshots
def save_screenshot(driver, filename):
    try:
        path = os.path.join(screenshot_dir, filename)
        print(f"Saving screenshot to: {path}")
        driver.save_screenshot(path)
    except Exception as e:
        print(f"Error saving screenshot: {e}")


# Helper function to sanitize filenames
def sanitize_filename(url):
    # Extract the main part of the URL and replace any invalid characters with underscores
    sanitized = re.sub(r'[^\w\-_\.]', '_', url.split('//')[1])
    return sanitized
