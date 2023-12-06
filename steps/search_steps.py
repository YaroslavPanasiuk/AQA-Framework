import time

from behave import *
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


@given('open website "{path}"')
def open_website(context, path):
    context.base_page = BasePage(context.driver)
    context.driver.get(path)
    context.driver.get_cookies()
    time.sleep(15)


@when('enter "{search_query}" in search field')
def check_title(context, search_query):
    context.base_page.enter_text_into_input(search_query)
    time.sleep(3)


@then('I should see search results related to "{search_term}"')
def verify_search_results(context, search_term):
    results_header = context.driver.find_element(*context.base_page.content_header)
    assert search_term.lower() in results_header.text.lower(), f"Expected search term '{search_term}' not found in results"


@then('close browser')
def close_browser(context):
    context.driver.close()
