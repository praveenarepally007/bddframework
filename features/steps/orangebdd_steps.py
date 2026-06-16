from behave import when,then,given
from pages.orangebdd_page import Orange_hrm
from conftest import driver
@given('user navigates to login page')
def step_impl(context):
    context.orangebdd_page.initial_load()

@when('user enters login details')
def step_impl(context):
    context.orangebdd_page.login()
@when('user clicks on myinfo')
def step_impl(context):
    context.orangebdd_page.info()
@when('user updates nationality and marital status')
def step_impl(context):
    context.orangebdd_page.personal_details()
@when('user clicks on save')
def step_impl(context):
    context.orangebdd_page.save_details()
# @when('user clicks on delete record checkbox and clicks on delete button')
# def step_impl(context):
#     context.orangebdd_page.record_deletion()
@when('user clicks on contact details and user clicks on save button')
def step_impl(context):
    context.orangebdd_page.contact_details()


