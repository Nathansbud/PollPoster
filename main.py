from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

import bs4 as BeautifulSoup
import time

import atexit
import json
import os


def make_chrome_browser(path_to, run_headless=False):
    if run_headless:
        headless_options = webdriver.ChromeOptions()
        headless_options.add_argument("headless")
        b = webdriver.Chrome(executable_path=path_to, chrome_options=headless_options)
    else: b = webdriver.Chrome(executable_path=path_to)
    b.implicitly_wait(2)
    WebDriverWait(b, 10)

    return b

def get_account(account):
    with open(os.path.join(os.path.dirname(__file__), "creds" + os.sep + "accounts.json")) as jf:
        creds = json.load(jf)
    return creds[account]

def twitter_login(driver_instance, username, password):
    driver_instance.get("https://twitter.com/login")

    username_box = driver_instance.find_element_by_class_name("js-username-field")
    password_box = driver_instance.find_element_by_class_name("js-password-field")

    username_box.send_keys(username)
    password_box.send_keys(password)

    driver_instance.find_element_by_class_name("EdgeButtom--medium").click()

driver = make_chrome_browser(path_to="/Users/zackamiton/Resources/chromedriver")

twitter_creds = get_account("twitter")
twitter_login(driver, twitter_creds['username'], twitter_creds['password'])

def handle_exit():
    driver.close()

atexit.register(handle_exit)

if __name__ == '__main__':
    pass
