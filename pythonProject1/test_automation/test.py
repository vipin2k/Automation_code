from selenium import webdriver
from selenium.webdriver.common.by import By
import time


add = []
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.gcitsolutions.com/gold-coast-it-solutions/")
# driver.implicitly_wait(10)


def test_lnk():
    driver.find_element(By.XPATH, "//*[@class='menu']").click()
    time.sleep(3)
    links = driver.find_elements(By.XPATH, "(//*[@class='social so-slide']//*[@target='_blank'])")
    for link in links:
        add.append(link.get_attribute('href'))
    print(add)
    driver.switch_to.new_window()
    time.sleep(2)
    driver.get(add[1])
    driver.get_screenshot_as_file("screenshot/screen1.png")
    time.sleep(2)
    driver.get(add[2])
    driver.get_screenshot_as_file("screenshot/screen2.png")
    time.sleep(2)
    print("Twitter and linkedin click in successfully")

    try:
        driver.get(add[0])
        driver.switch_to.new_window()
        time.sleep(1)

    except:
        driver.get_screenshot_as_file("screenshot/screen3.png")
        print("An exception error occurred ", add[0])



