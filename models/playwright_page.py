'''    from playwright.sync_api import Page, Locator


class PlaywrightPage:

    def __init__(self, page: Page):
        self.page = page
        self.page.goto("https://playwright.dev/python")

        self.docs_link = self.page.get_by_role(
            "link", name="Docs"
        )

        self.search_input = self.page.get_by_placeholder("Search docs")

    
    def visit_docs(self):
        self.docs_link.click()


    def search(self, query):
        self.page.keyboard.press("Control+KeyK")
        self.search_input.fill(query)


    def search_results(self) -> Locator:
        print("Search Results:")
        for result in self.page.locator("span.DocSearch-Hit-title").all():
            print(result.inner_text())

        return self.page.locator("div.DocSearch-Dropdown")
    
'''
from playwright.sync_api import Page, Locator

class PlaywrightPage:
    def __init__(self, page: Page):
        self.page = page
        self.page.goto("https://playwright.dev/python")

        self.docs_link = self.page.get_by_role("link", name="Docs")
        self.search_button = self.page.locator('button.DocSearch-Button[aria-label="Search"]')
        self.search_input = self.page.locator('input#docsearch-input.DocSearch-Input')

    def visit_docs(self):
        self.docs_link.click()

    def search(self, query):
        try:
            # Ensure the search button is visible and click it
            self.page.wait_for_selector('button.DocSearch-Button[aria-label="Search"]', state='visible', timeout=60000)
            self.search_button.click()
            self.search_input.click()
            self.search_input.fill(query)
        except Exception as e:
            print(f"Initial search attempt failed, trying fallback: {e}")
            # Use keyboard shortcut as fallback
            self.page.keyboard.press("Control+KeyK")
            self.search_input.click()
            self.search_input.fill(query)
        
        self.search_input.press("Enter")

    def search_results(self) -> Locator:
        return self.page.locator("div.DocSearch-Dropdown")

    def log_search_results(self):
        results = self.page.locator("span.DocSearch-Hit-title").all_text_contents()
        print("Search Results:")
        for result in results:
            print(result)
        return results
