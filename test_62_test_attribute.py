import re
from playwright.sync_api import Page, expect

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/python")
    
    docs_link = page.get_by_role("link", name="Docs")

    # expect exact class value
    expect(docs_link).to_have_class(
        "navbar__item navbar__link"
    )
    
    # expect class to contain value
    expect(docs_link).to_have_class(
        re.compile(r"navbar__link")
    )

    # expect attribute in locator - checking for the presence of href attribute with a specific value
    expect(docs_link).to_have_attribute("href", "/python/docs/intro")

    # If you want to check the presence of an attribute without specifying its value
    href_value = docs_link.get_attribute("href")
    assert href_value is not None
