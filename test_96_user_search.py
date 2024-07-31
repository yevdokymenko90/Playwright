import pytest
from playwright.sync_api import Playwright, APIRequestContext

# Fixture to create and dispose of API context
@pytest.fixture
def api_context(playwright: Playwright) -> APIRequestContext: # type: ignore
    api_context = playwright.request.new_context(
        base_url="https://dummyjson.com"
    )
    yield api_context
    api_context.dispose()

# Test function to search for users
def test_users_search(api_context: APIRequestContext):
    query = "John"
    response = api_context.get(f"/users/search?q={query}")

    # Ensure that the response status is OK (200)
    assert response.status == 200, f"Expected status 200 but got {response.status}"

    users_data = response.json()
    total_users = users_data.get("total", 0)
    print("Users found:", total_users)

    # Check if the response contains the expected structure
    assert "users" in users_data, "The response does not contain 'users' key"

    # Flag to track if any user matches the query
    user_found = False

    # Iterate through the users and check if the query is in the first name
    for user in users_data["users"]:
        print("Checking user:", user["firstName"])
        if query.lower() in user["firstName"].lower():
            user_found = True
            break

    # Assert that at least one user matches the query
    assert user_found, f"No user found with the first name containing the query {query}"

# Wrapper to run the test with Playwright
def run_test():
    with sync_playwright() as playwright: # type: ignore
        test_users_search(playwright.request.new_context(base_url="https://dummyjson.com"))

# Entry point for direct script execution
if __name__ == "__main__":
    run_test()
