import time
from behave import *
from selenium.webdriver.common.by import By
from Tools import take_screenshot, file_reader


@given("User on the homepage")
def step_impl(context):
    context.driver.get(file_reader.read_config("precondition","url"))
    time.sleep(1)
    

@when("User click login button")
def step_impl(context):
    context.driver.find_element(By.XPATH, file_reader.get_element("header","button_login")).click()
    time.sleep(1)

@when("User enter correct registred email")
def step_impl(context):
    context.driver.find_element(By.NAME, file_reader.get_element("login","input_email")).send_keys("testing_user1@yopmail.com")
    time.sleep(1)


@when("User enter correct registred password")
def step_impl(context):
    context.driver.find_element(By.NAME, file_reader.get_element("login","input_password")).send_keys("Sup3rm@n123")
    time.sleep(1)


@when("User click on sign in button")
def step_impl(context):
    context.driver.find_element(By.XPATH, file_reader.get_element("login","button_sign_in")).click()


@then("User successfuly login to website")
def step_impl(context):
    time.sleep(1)

@when("User enter inccorect email")
def step_impl(context):
    context.driver.find_element(By.NAME, file_reader.get_element("login","input_email")).send_keys("testing@yopmail.com")
    time.sleep(1)


@when('User enter inccorect password')
def step_impl(context):
    context.driver.find_element(By.NAME, file_reader.get_element("login","input_password")).send_keys("Sup3rm@n")
    time.sleep(1)


@then('User unsuccessfuly login to website')
def step_impl(context):
    time.sleep(1)

@then('Take screenshot "{file_name}"')
def step_impl(context, file_name):
    if file_reader.read_config("precondition","screenshot") == "yes":
        take_screenshot.page_screenshot(context.driver, file_name)
    time.sleep(1)