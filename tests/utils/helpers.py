from fixtures.browser import browser

def screenshot (browser):
    page = browser.new_page()
    # Take a screenshot
    page.screenshot(path="after_click.png")