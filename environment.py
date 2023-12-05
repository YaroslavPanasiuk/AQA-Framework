from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def before_all(context):
    chrome_options = Options()
    chrome_options.binary_location = r"C:\Drivers\chrome-win64\chrome.exe"
    context.driver = webdriver.Chrome(options=chrome_options)


def after_all(context):
    context.driver.quit()
