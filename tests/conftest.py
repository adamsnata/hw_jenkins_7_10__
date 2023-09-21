import pytest
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config, browser

from utils import attach

PROJECT_ROOT_PATH = os.path.dirname(__file__)
print(PROJECT_ROOT_PATH)
RESOURCE_PATH = os.path.abspath(os.path.join(PROJECT_ROOT_PATH, 'resources'))


# @pytest.fixture(scope='function', autouse=True)
# def browser_managment():
#     browser.config.base_url = 'https://demoqa.com/automation-practice-form'
#     browser.config.window_width = 1920
#     browser.config.window_height = 1028
#
#     yield
#     browser.quit()


@pytest.fixture(scope='function')
def setup_browser():
    browser_version = "100.0"
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser.config.driver = driver
    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
