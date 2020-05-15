from argparse import ArgumentParser
from selenium.webdriver import Chrome,Firefox,Ie


def get_driver_instance():
    parser = ArgumentParser()
    parser.add_argument("--browser",default="firefox")
    parser.add_argument("--url",default="test")
    parser.add_argument("--env",default="windows")

    options, arg = parser.parse_known_args()

    browser_type = options.browser.lower()
    url_info = options.url.lower()
    env_info = options.env.lower()

    if browser_type == "chrome":
        driver = Chrome("./browser-servers/chromedriver.exe")
    elif browser_type == "firefox":
        driver = Firefox("./browser-servers/geckodriver.exe")
    else:
        print("______!!!!!!!!!!!!!!Invalid Browser Option. Please provide proper value!!!!!!!!!!!!________")

    driver.maximize_window()
    driver.implicitly_wait(30)

    if url_info == "test":
        driver.get("https://learn.letskodeit.com/")
    else:
        print("invalid url")
    return driver

