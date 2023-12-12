from behave.runner import Context
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys


def before_all(context: Context):
    #sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8')
    chrome_options = Options()
    #chrome_options.binary_location = r"C:\Drivers\chrome-win64\chrome.exe"
    context.driver = webdriver.Firefox()


def after_all(context: Context):
    return
#    context.driver.quit()


