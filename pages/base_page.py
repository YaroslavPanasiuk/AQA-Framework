import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.text_input_locator = (By.NAME, 'search')
        self.language_selector = (By.XPATH, '/html/body/div[1]/header/div[1]/div[1]/div/div/div/div/div[2]/div/div[4]/form')
        self.language_options = (By.XPATH, '/html/body/div[1]/header/div[1]/div[1]/div/div/div/div/div[2]/div/div[4]/form/div/ul')
        self.phone_span = (By.XPATH, '/html/body/div[1]/header/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/span')
        self.schedule_span = (By.XPATH, '/html/body/div[1]/header/div[1]/div[1]/div/div/div/div/div[1]/div/div[2]/span')
        self.search_button = (By.XPATH, '/html/body/div[1]/header/div[1]/div[2]/div/div/div/div/div/div/div[2]/button')
        self.items_grid = (By.XPATH, '//*[@id="content"]/div[3]')
        self.content_header = (By.XPATH, '//*[@id="content"]/h1')
        self.sort_popup = (By.XPATH, '/html/body/div[1]/div[3]/div/div/div[2]/div[2]/div/a[1]')
        self.sort_options = (By.XPATH, '/html/body/div[1]/div[3]/div/div/div[2]/div[2]/div/ul')
        self.animal_categories = (By.XPATH, '/html/body/div[1]/header/div[2]/div/div/div/div/div/div/div/div/ul')
        self.products_header = (By.XPATH, '/html/body/div[1]/div[3]/h2')
        self.color_selector = (By.XPATH, '/html/body/div[1]/div[3]/div/div/div[1]/div[2]/div/div[2]/div[1]/div')
        self.color_options = (By.XPATH, '/html/body/div[1]/div[3]/div/div/div[1]/div[2]/div/div[2]/div[1]/div/ul')
        self.size_selector = (By.XPATH, '/html/body/div[1]/div[3]/div/div/div[1]/div[2]/div/div[2]/div[2]/div')
        self.size_options = (By.XPATH, '/html/body/div[1]/div[3]/div/div/div[1]/div[2]/div/div[2]/div[2]/div/ul')
        self.buy_button = (By.XPATH, '//*[@id="button-cart"]')
        self.basket_logo = (By.XPATH, '//*[@id="cart"]/button')
        self.basket_button = (By.CLASS_NAME, 'btn-l')
        self.basket_popup = (By.XPATH, '//*[@id="cart"]/ul')
        self.table_of_items_in_basket = (By.XPATH, '//*[@id="content"]/form/div/table/tbody')


    def open(self):
        self.driver.get("https://www.example.com")

    def get_title(self):
        return self.driver.title

    def enter_text_into_input(self, search_query):
        input_element = self.driver.find_element(*self.text_input_locator)
        input_element.clear()
        input_element.send_keys(search_query)
        input_element.send_keys(Keys.ENTER)

    def get_input_value(self):
        input_element = self.driver.find_element(*self.text_input_locator)
        return input_element.get_attribute('value')

    def exists(self, element):
        try:
            self.driver.find_element(*element)
            return True
        except:
            return False

    def get_children(self, element):
        return element.find_elements(By.XPATH, "./*")

    def find_elements_by_class(self, class_name):
        return self.driver.find_elements(By.CLASS_NAME, class_name)

    def get_items(self):
        assert self.exists(self.items_grid), "not exists"
        return self.get_children(self.driver.find_element(*self.items_grid))

    def get_item_names(self):
        names = []
        for item in self.get_items():
            names.append(item.find_element(By.TAG_NAME, "h4").text)
        return names

    def get_item_prices(self):
        prices = []
        for item in self.get_items():
            prices.append(float(item.find_element(By.CLASS_NAME, 'price').text.removeprefix("$").split()[0]))
        return prices

    def get_item_ratings(self):
        ratings = []
        for item in self.get_items():
            ratings.append(len(item.find_elements(By.CLASS_NAME, 'star')))
        return ratings

    def choose_item_in_menu(self, menu, item):
        for option in menu:
            if item in self.get_children(option)[0].text:
                return option
        return None


def list_is_sorted(arr: [], order):
    if order == "ascending":
        return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
    else:
        return all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1))


