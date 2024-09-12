from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('In launch chrome browser')
def Open_browser(context):
    context.driver = webdriver.Chrome()


@when('Enter username "{login_username}" and password "{login_password}"')
def Login_credentials(context, login_username, login_password):
    context.driver.find_element(By.XPATH, "//*[@name='user-name']").send_keys(login_username)
    context.driver.find_element(By.XPATH, "//*[@name='password']").send_keys(login_password)


@when('click on login button')
def submit_button(context):
    context.driver.find_element(By.XPATH, "//*[@type='submit']").click()


@when('close the browser')
def close_the_browser(context):
    context.driver.close()


@then('user must successfully login to the dashboard page')
def dashboard_content(context):
    try:
        dashboard_text = context.driver.find_element(By.XPATH, "//*[@class='product_label']").text
    except:
        context.driver.close()
        assert False, "Test failed"
    if dashboard_text == "Products":
        context.driver.close()
        assert True, "Test passed"
