from models.login_page import LoginPage # type: ignore
from playwright.sync_api import Page, expect # type: ignore


def test_successful_login(page: Page):
    username = "dan"
    password = "pwd"

    login_page = LoginPage(page)

    login_page.login(username, password)

    expect(login_page.label).to_have_text( # type: ignore
        f"Welcome, {username}!"
        )


def test_failed_login(page: Page):
    username = "dan"
    password = "cnasdjc"

    login_page = LoginPage(page)

    login_page.login(username, password)

    expect(login_page.label).to_have_text( # type: ignore
        "Invalid username/password"
    )