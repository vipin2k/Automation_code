from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('launch chrome browser')
def Open_browser(context):
    context.driver = webdriver.Chrome()


@when('open swag labs homepage')
def homepage(context):
    context.driver.get("https://www.saucedemo.com/v1/")


@then('verify that the logo present on page')
def logo_present(context):
    logo_displayed = context.driver.find_element(By.XPATH, "//*[@class='login_logo']").is_displayed()
    assert logo_displayed, "Logo is not displayed on the page."
    print("Logo is displayed on the page:", logo_displayed)


@then('close the browser')
def close_the_browser(context):
    context.driver.close()