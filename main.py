from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

import atexit
import json
import os

import googleapi

def make_chrome_browser(path_to, run_headless=False, quit_on_done=False):
    if run_headless:
        headless_options = webdriver.ChromeOptions()
        headless_options.add_argument("headless")
        b = webdriver.Chrome(executable_path=path_to, options=headless_options)
    else: b = webdriver.Chrome(executable_path=path_to)
    b.implicitly_wait(2)
    WebDriverWait(b, 10)

    if quit_on_done: atexit.register(b.close)

    return b

def get_account(account):
    with open(os.path.join(os.path.dirname(__file__), "credentials" + os.sep + "accounts.json")) as jf:
        creds = json.load(jf)
    return creds[account]

def twitter_login(driver_instance, username, password):
    driver_instance.get("https://twitter.com/login")

    username_box = driver_instance.find_element_by_class_name("js-username-field")
    password_box = driver_instance.find_element_by_class_name("js-password-field")

    username_box.send_keys(username)
    password_box.send_keys(password)

    driver_instance.find_element_by_class_name("EdgeButtom--medium").click()

def make_poll_tweet(driver_instance, title, options):
    if len(options) < 2:
        print("Polls must have at least 2 options!")
        return
    else:
        driver_instance.get("https://twitter.com/compose/tweet")

        tweetbox = driver_instance.find_element_by_xpath("//div[contains(concat(' ',normalize-space(@class),' '),' public-DraftEditor-content ')][1][1]")
        tweetbox.send_keys(title)

        poll_toggle = driver_instance.find_element_by_xpath("//div[@aria-label='Add poll']")  # lmao the most meme tag to xpath on
        poll_toggle.click()

        for i in range(0, len(options)-2):
            add_option_toggle = driver_instance.find_element_by_xpath("//div[@aria-label='Add a choice']")
            add_option_toggle.click()

        for i in range(0, len(options)):
            choice = driver_instance.find_element_by_xpath("//input[@name='Choice"+str(i+1)+"']")
            choice.send_keys(options[i])

        tweet_button = driver_instance.find_element_by_xpath("//div[@data-testid='tweetButton']")
        tweet_button.click()

if __name__ == '__main__':
    driver = make_chrome_browser(path_to="/Users/zackamiton/Resources/chromedriver", run_headless=True)

    twitter_creds = get_account("twitter")
    twitter_login(driver, twitter_creds['username'], twitter_creds['password'])
    make_poll_tweet(driver, "which of these greetings best defines you", ["hey", "hi", "howdy", "heyo"])
    pass
