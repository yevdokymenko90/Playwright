import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def page():
    playwright = sync_playwright().start
    browser = playwright.chromium.launch()
    return browser.new_new_page()
    

def test_website(page):
    pass 