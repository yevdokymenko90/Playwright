from playwright.sync_api import Request, Response, Page, expect # type: ignore


def on_request(request: Request):
    print("Sent request", request)


def on_response(response: Response):
    print("Received response", response)



def test_docs_link(page: Page):
    page.on("request", on_request)
    page.on("response", on_response)
    
    page.goto("https://playwright.dev/python")
    
    docs_link = page.get_by_role("link", name="Docs")
    docs_link.click()
    
    expect(page).to_have_url("https://playwright.dev/docs/intro")
    