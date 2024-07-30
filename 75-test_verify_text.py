from playwright.sync_api import Page, expect

def test_contains_text(page: Page):
    page.goto("http://uitestingplayground.com/verifytext")
    
    # Add delay to allow the page to load completely
    page.wait_for_timeout(1000)  # Wait for 3 seconds

    text = page.locator("div.bg-primary").get_by_text("Welcome")
    
    # Add delay to visually confirm the text locator
    page.wait_for_timeout(3000)  # Wait for 3 seconds

    # Verify the text
    expect(text).to_have_text("Welcome UserName!")
    
    # Add final delay to inspect the final state
    page.wait_for_timeout(1000)  # Wait for 3 seconds
