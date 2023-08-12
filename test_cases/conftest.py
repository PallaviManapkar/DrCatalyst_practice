import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture
def setup():
    # if browser == "chrome":
    #     driver = webdriver.Chrome()
    # elif browser == "edge":
    #     driver = webdriver.Edge()
    # elif browser == "firefox":
    #     options = Options()
    #     options.binary_location = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
    #     driver = webdriver.Firefox(options=options)
    # else:
    #     chrome_options = webdriver.ChromeOptions()
    #     chrome_options.add_argument("headless")
    #     driver = webdriver.Chrome(options=chrome_options)
    # driver.maximize_window()
    # driver.implicitly_wait(10)
    # driver.get("https://iemodemoindia.meditab.com/#/login")
    # yield driver
    # driver.quit()

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://iemodemoindia.meditab.com/#/login")
    return driver

