from playwright.sync_api import Route, Request, Response, Page, expect # type: ignore


def on_route(route:Route):
    print("Request aborted:", route.requsest)
    route.abort()
    


def test_docs_link(page: Page):
    page.route(
        "https://playwright.dev/python/img/playwright.svg",
        on_route
        )
    
    page.goto("https://playwright.dev/python")
    
    page.screenshot(path="screenshot.png")