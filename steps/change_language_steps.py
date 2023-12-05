import time
import logging
from behave import *

logging.basicConfig(level=logging.INFO)


@when('change language to "{language}"')
def implement(context, language):
    context.driver.find_element(*context.base_page.language_selector).click()
    time.sleep(1)
    options = context.base_page.get_children(context.driver.find_element(*context.base_page.language_options))
    button = context.base_page.choose_item_in_menu(options, language)
    assert button is not None, f"no language '{language}' found"
    button.click()
    time.sleep(5)


elements_names = {
    "phone": {"Ukrainian": "Телефони:", "English": "Phones:", "German": "Telefone:"},
    "schedule": {"Ukrainian": "Ми працюємо:", "English": "We are open:", "German": "Wir sind offen:"},
    "search": {"Ukrainian": "Пошук", "English": "Search", "German": "Suche"}
}


@then('view "{text_field}" should be written in "{language}"')
@step('view "{text_field}" should be written in "{language}"')
def implement(context, text_field, language):
    match text_field:
        case "phone":
            text = context.driver.find_element(*context.base_page.phone_span).text
            assert text.lower() == elements_names[text_field][language].lower(), \
                f"wrong text: {text}\nShould be: {elements_names[text_field][language]}"
        case "schedule":
            text = context.driver.find_element(*context.base_page.schedule_span).text
            assert text.lower() == elements_names[text_field][language].lower(), \
                f"wrong text: {text}\nShould be: {elements_names[text_field][language]}"
        case "search":
            text = context.driver.find_element(*context.base_page.search_button).text
            assert text.lower() == elements_names[text_field][language].lower(), \
                f"wrong text: {text}\nShould be: {elements_names[text_field][language]}"
        case _:
            assert False, f"no '{language}' found"
