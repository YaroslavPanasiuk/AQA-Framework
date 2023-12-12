# test_module1.py

import pytest
from behave import given, when, then
from steps import open_website, enter_search_text, choose_item, choose_options, click_buy, go_to_basket, \
    verify_basket_items, clear_basket


@pytest.fixture
def setup_teardown():
    open_website("http://opencart.qatestlab.net/")
    yield
    clear_basket()


def test_add_first_item_to_basket(setup_teardown):
    enter_search_text("Pet")
    choose_item("1")
    choose_options("default size", "default color")
    click_buy()
    go_to_basket()
    verify_basket_items("1")


def test_add_second_item_to_basket(setup_teardown):
    enter_search_text("Pet")
    choose_item("2")
    choose_options("default size", "default color")
    click_buy()
    go_to_basket()
    verify_basket_items("1")


def test_add_multiple_items_to_basket(setup_teardown):
    enter_search_text("Pet")
    choose_item("4")
    choose_options("default size", "default color")
    click_buy()
    enter_search_text("Pet")
    choose_item("6")
    choose_options("default size", "default color")
    click_buy()
    go_to_basket()
    verify_basket_items("2")
