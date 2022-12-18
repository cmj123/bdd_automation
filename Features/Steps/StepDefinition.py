from behave import given, when, then
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
# from selenium.

@given(u'User is on Registration page')
def step_impl(context):
    context.driver = Chrome()
    context.driver.get('http:www.thetestingworld.com/testings')
    # raise NotImplementedError(u'STEP: Given User is on Registration page')


@when(u'User enters username')
def step_impl(context):
    context.driver.find_element('name', 'fld_username').send_keys("abcd")
    # fld_username
    # raise NotImplementedError(u'STEP: When User enters username')


@when(u'User enter email id')
def step_impl(context):
    context.driver.find_element('name','fld_email').send_keys("abcd@gmail.com")
    # raise NotImplementedError(u'STEP: When User enter email id')


@when(u'User enter password')
def step_impl(context):
    context.driver.find_element('name', 'fld_password').send_keys("password")
    # raise NotImplementedError(u'STEP: When User enter password')


@when(u'User click on signup button')
def step_impl(context):
    context.driver.find_element(by=By.XPATH,value='//input[@type="submit" and @value="Sign up"]').click()
    # raise NotImplementedError(u'STEP: When User click on signup button')


@then(u'User should be registered successfully')
def step_impl(context):
    print("Registered")
    # raise NotImplementedError(u'STEP: Then User should be registered successfully')


@when(u'User enters duplicate username')
def step_impl(context):
    print("Not Registered")
    # raise NotImplementedError(u'STEP: When User enters duplicate username')