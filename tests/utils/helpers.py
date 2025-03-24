from fixtures.browser import browser
from playwright.sync_api import Page

def screenshot (page: Page, path: str, full_page: bool = True):
    page.screenshot(path=path, full_page=full_page)