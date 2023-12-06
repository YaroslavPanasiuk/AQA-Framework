import time
import logging
from behave import *

logging.basicConfig(level=logging.INFO)


@when('choose item #"{item_index}"')
def implement(context, item_index):
    index = int(item_index)
    items = context.base_page.get_items()
    assert len(items) > index, f"no item at index {index} found. there are {len(items)} items overall"
    items[index-1].click()
    time.sleep(15)


@when('choose "{item_size}" and "{item_color}" options')
def implement(context, item_size, item_color):
    context.driver.find_element(*context.base_page.size_selector).click()
    time.sleep(1)
    sizes = context.base_page.get_children(context.driver.find_element(*context.base_page.size_options))
    assert len(sizes) > 1, "no sizes to choose from"
    if item_size == "default size":
        size_option = sizes[1]
    else:
        size_option = context.base_page.choose_item_in_menu(sizes, item_size)
    assert size_option is not None, f"no size '{item_size}' found"
    size_option.click()

    time.sleep(1)
    context.driver.find_element(*context.base_page.color_selector).click()
    time.sleep(1)
    colors = context.base_page.get_children(context.driver.find_element(*context.base_page.color_options))
    assert len(colors) > 1, "no colors to choose from"
    if item_color == "default color":
        color_option = colors[1]
    else:
        color_option = context.base_page.choose_item_in_menu(colors, item_color)
    assert color_option is not None, f"no color '{item_color}' found"
    color_option.click()
    time.sleep(5)


@when('click buy')
def implement(context):
    context.driver.find_element(*context.base_page.buy_button).click()
    time.sleep(7)


@when('go to basket')
def implement(context):
    context.driver.find_element(*context.base_page.basket_logo).click()
    time.sleep(1)
    cart_list = context.driver.find_element(*context.base_page.basket_popup)
    context.driver.execute_script("arguments[0].scrollBy(0, 500);", cart_list)
    context.driver.find_element(*context.base_page.basket_button).click()
    time.sleep(10)


@then('basket should have "{items_count}" items')
def implement(context, items_count):
    current_items_count = len(context.base_page.get_children(context.driver.find_element(*context.base_page.table_of_items_in_basket)))
    assert int(items_count) == current_items_count, f"wrong items count: {current_items_count}\n Should be: {items_count}"
    time.sleep(5)

