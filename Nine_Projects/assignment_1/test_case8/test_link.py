import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

all = []
file = open("test_flipkart.json")
data = json.load(file)
file.close()

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(data["url"])
driver.implicitly_wait(5)
print("Test Started")



def test_TotalLink():
    links = driver.find_elements(By.XPATH, '//*[@class="eFQ30H"]/a')
    for link in links:
        all.append(str(link.get_attribute("href")))
        print("link text: ", link.text)
        print("link url: ", link.get_attribute("href"))
        print("---------------------------------------------------------------------------")
    print("Total no of links present in homepage is ", len(all))
    driver.close()
    driver.quit()
    print("Test Completed")