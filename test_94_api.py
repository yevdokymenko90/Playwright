import pytest
from playwright.sync_api import Page, sync_playwright

def test_users_api(page: Page):
    # Navigate to the API endpoint
    response = page.goto("https://dummyjson.com/users/1")

    # Ensure that the response status is OK (200)
    assert response.status == 200, f"Expected status 200 but got {response.status}"

    # Extract JSON data from the response
    user_data = response.json()
    print(user_data)  # Debugging line to see the actual data

    # Assertions to check if the keys exist in the response data
    assert "firstName" in user_data, "firstName key not found in response"
    assert "lastName" in user_data, "lastName key not found in response"

    # Update the expected values based on the actual API response
    expected_first_name = "Emily"
    expected_last_name = "Johnson"
    
    # Assertions to check actual values against expected values
    assert user_data["firstName"] == expected_first_name, f"Expected '{expected_first_name}' but got '{user_data['firstName']}'"
    assert user_data["lastName"] == expected_last_name, f"Expected '{expected_last_name}' but got '{user_data['lastName']}'"

# Wrapper to run the test with Playwright
def run_test():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        test_users_api(page)
        browser.close()

# Entry point for pytest
if __name__ == "__main__":
    run_test()
