import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome',
                     help='Choose browser: chrome or firefox', choices=('chrome', 'firefox'))
    parser.addoption('--language', action='store', default='en', help='Choose language')


@pytest.fixture(scope='function')
def driver(request):
    browser = request.config.getoption('browser')
    language = request.config.getoption('language')
    if browser == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        driver = webdriver.Chrome(options=options)
    elif browser == 'firefox':
        options = webdriver.FirefoxOptions()
        options.set_preference("intl.accept_languages", 'user_language')
        driver = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield driver
    print("\nquit driver..")
    driver.quit()
