from playwright.sync_api import Page



def test_page_has_get_started_link(page):
    page.goto("https://playwright.dev/")
    
    link = page.get_by_role("link", name="Get Started")
    link.click()
    page.url == "https://playwright.dev/docs/intro"
    
    assert page.url == "https://playwright.dev/docs/intro"
    