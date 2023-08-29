import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', default='en',
                     help="Choose browser language. Run example: pytest --language=es test_items.py")


@pytest.fixture(scope="function")
def browser(request):
    accept_language = request.config.getoption("language")
    options = Options()
    options.binary_location = \
        '/Users/user/Downloads/chrome-mac-x64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing'
    options.add_experimental_option('prefs', {'intl.accept_languages': accept_language})
    browser = webdriver.Chrome(options=options)

    yield browser
    print("\nquit browser..")
    browser.quit()
