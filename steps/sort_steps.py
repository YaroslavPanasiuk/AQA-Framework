import time
import logging
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base_page import list_is_sorted
logging.basicConfig(level=logging.INFO)


@when('select sort by "{sort_by}"')
def implement(context, sort_by):
    context.driver.find_element(*context.base_page.sort_popup).click()
    options = context.base_page.get_children(context.driver.find_element(*context.base_page.sort_options))
    button = context.base_page.choose_item_in_menu(options, sort_by)
    assert button is not None, f"no option '{sort_by}' found"
    button.click()
    time.sleep(5)


@then('results should be sorted by "{sort_by}" "{order}"')
def implement(context, sort_by, order):
    match sort_by:
        case "name":
            assert list_is_sorted(context.base_page.get_item_names(), order), f"not sorted by name {order}\nActual order: {context.base_page.get_item_names()}"
        case "rating":
            assert list_is_sorted(context.base_page.get_item_ratings(), order), f"not sorted by rating {order}\nActual order: {context.base_page.get_item_ratings()}"
        case "price":
            assert list_is_sorted(context.base_page.get_item_prices(), order), f"not sorted by price {order}\nActual order: {context.base_page.get_item_prices()}"
