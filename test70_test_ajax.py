from playwright.sync_api import Page, expect

def test_ajax_data(page: Page):
    page.goto("http://uitestingplayground.com/ajax")
    
    btn = page.get_by_role("button", name="Button Triggering Ajax Request")
    btn.click()
    
    paragraph = page.locator("p.bg-success")
    paragraph.wait_for()
    
    expect(paragraph).to_be_visible()
    