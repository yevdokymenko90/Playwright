import pytest # type: ignore
from playwright.sync_api import Page, TimeoutError # type: ignore


def test_nbsp(page: Page):
    page.goto("http://uitestingplayground.com/nbsp")
    
    # using normal space
    with pytest.raises(TimeoutError):
        page.locator("//button[text()='My Button']").click(
            timeout=2000
        )
    # using non-breaking space
    page.locator("//button[text()='My\u00a0Button']").click()