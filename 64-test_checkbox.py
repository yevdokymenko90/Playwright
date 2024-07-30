from playwright.sync_api import Page, expect

def test_app(page: Page):
    page.goto("https://bootswatch.com/default")
    
    # Add delay to allow the page to load completely
    page.wait_for_timeout(2000)  # Wait for 2 seconds

    default_checkbox = page.get_by_label("Default checkbox")
    checked_checkbox = page.get_by_label("Checked checkbox")

    # Add delay to visually inspect the initial state
    page.wait_for_timeout(2000)  # Wait for 2 seconds

    # Expect the checked checkbox to be checked
    expect(checked_checkbox).to_be_checked()

    # Add delay to visually confirm the state
    page.wait_for_timeout(2000)  # Wait for 2 seconds

    # Expect the default checkbox to be unchecked
    expect(default_checkbox).not_to_be_checked()

    # Add final delay to inspect the final state
    page.wait_for_timeout(2000)  # Wait for 2 seconds
