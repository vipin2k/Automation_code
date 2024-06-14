import datetime
from selenium import webdriver
import ssl
import socket
import time


def get_certificate_expiry(domain):
    try:
        ssl_date_fmt = r'%b %d %H:%M:%S %Y %Z'
        context = ssl.create_default_context()
        conn = context.wrap_socket(socket.create_connection((domain, 443)), server_hostname=domain)
        ssl_info = conn.getpeercert()
        expires = datetime.datetime.strptime(ssl_info['notAfter'], ssl_date_fmt)
        return expires
    except Exception as e:
        print("Error occurred while fetching SSL certificate information:", e)
        return None


def save_screenshot(driver, filename):
    driver.save_screenshot(filename)


# Set up Chrome WebDriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--ignore-certificate-errors")  # Ignore SSL certificate errors
driver = webdriver.Chrome(executable_path=r"D:\vipin_test_automation\proton_headless\DEMO_PROTON\chromedriver-win64\chromedriver.exe", options=chrome_options)

# Define the domain for which you want to check SSL certificate expiration
domain = "app.goproton.co"

# Check SSL certificate expiration
expiry_date = get_certificate_expiry(domain)

if expiry_date:
    print("SSL Certificate Expiry Date:", expiry_date)
    # Load the website
    driver.get("https://" + domain)
    # Wait for the website to load
    time.sleep(5)  # Adjust the delay time as needed
    # Take screenshot
    save_screenshot(driver, "SSL_certificate_details.png")
    # Introduce a delay to ensure the screenshot is captured before closing the browser
    time.sleep(2)  # Adjust the delay time as needed
else:
    print("Failed to retrieve SSL certificate information for", domain)
    # Save screenshot for failed SSL certificate retrieval
    save_screenshot(driver, "SSL_certificate_not_found.png")

# Close the browser
driver.quit()
