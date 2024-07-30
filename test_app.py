from playwright.sync_api import Page, expect

DOCS_URL = "https://playwright.dev/docs/intro"


def test_page_get_started_link(page: Page):
    page.goto("https://playwright.dev/python")
    
    link = page.get_by_role("link", name="Get Started")
    link.click()
    
    #assert page.url == DOCS_URL
    expect(page).to_have_title("Installation | Playwright Python")
    