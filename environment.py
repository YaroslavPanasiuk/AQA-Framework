from behave.runner import Context
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys


def before_all(context: Context):
    #sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8')
    chrome_options = Options()
    chrome_options.binary_location = r"/usr/bin/chrome"#r"C:\Drivers\chrome-win64\chrome.exe"
    firefox_options = Options()
    firefox_options.binary_location = r"/usr/bin/firefox"
    context.driver = webdriver.Chrome(chrome_options)


def after_all(context: Context):
    context.driver.quit()


