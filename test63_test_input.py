from playwright.sync_api import Page, expect 

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/python")
    input = page.get_by_placeholder("Search docs")

    # input is hidden initially
    expect(input).to_be_hidden()

    # search button
    search_btn = page.get_by_role("button", name="Search")
    search_btn.press("Control+KeyK")

    # Add a small delay to allow the input to become editable
    page.wait_for_timeout(1000)

    # input should be visible/editable
    expect(input).to_be_editable()

    # Log the current value of the input
    input_value = input.input_value()
    print(f"Input value after pressing Control+KeyK: '{input_value}'")

    # Clear the input field
    input.fill('')

    # input should be empty after clearing it
    expect(input).to_be_empty()

    # type some query in the input
    query = "assertions"
    input.fill(query)

    # expect the input value as query
    expect(input).to_have_value(query)

