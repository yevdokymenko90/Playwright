from models.playwright_page import PlaywrightPage
from playwright.sync_api import Page, expect

def test_docs_link(page: Page):
    homepage = PlaywrightPage(page)
    homepage.visit_docs()

    expect(homepage.page).to_have_url(
        "https://playwright.dev/python/docs/intro"
    )

def test_docs_search(page: Page):
    query = "assertions"

    homepage = PlaywrightPage(page)
    homepage.search(query)

    # Adding a click action after performing the search
    homepage.search_input.click()

    # Log search results for debugging
    search_results = homepage.log_search_results()
    
    # Adjust the expected text based on the actual content
    expected_text = "Assertions"

    # Verify the search results contain the expected text
    expect(homepage.search_results()).to_contain_text(expected_text)
