from playwright.sync_api import sync_playwright


with sync_playwright() as playwright:
    # Launch the browser
    playwright.chromium
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    # Visit the playwright website
    page.goto("https://playwright.dev/")
    
    docs_button = page.get_by_role("link", name="Docs")
    docs_button.click()
    
    print("Docs:", page.url)
    # Close the browser
    browser.close()
    
    