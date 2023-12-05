import time
import logging
from behave import *

logging.basicConfig(level=logging.INFO)


@when('click on "{item}" in menu')
def implement(context, item):
    items = context.base_page.get_children(context.driver.find_element(*context.base_page.animal_categories))
    button = context.base_page.choose_item_in_menu(items, item)
    assert button is not None, f"no item '{item}' found"
    button.click()
    time.sleep(5)


@then('Products header should be "{header}"')
def implement(context, header):
    current_header = context.driver.find_element(*context.base_page.products_header).text
    assert current_header.lower() == header.lower(), f"wrong header: {current_header}\nShould be: {header}"
