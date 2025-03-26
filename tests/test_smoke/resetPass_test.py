from playwright.sync_api import expect
from pages.resetPass_page import ResetPassword
from fixtures.browser import browser

def test_resetPass_Correct(browser):
    page = browser.new_page()
    resetPass_page = ResetPassword(page)
    resetPass_page.navigate()
    resetPass_page.reset_password("Admin")


    #Selecctores
    url_actual = page.url
    url_esperada = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/sendPasswordReset'
 
    #Validacines
    assert url_actual == url_esperada, f"Se esperaba {url_esperada}, pero se obtuvo {url_actual}"
    resetPass_page.reset_confirm()
    page.screenshot(path="screenshots/resetPass/test_resetPass_Correct.png", full_page=True)

    

    page.close()

def test_resetPass_user(browser):
    page = browser.new_page()
    resetPass_page = ResetPassword(page)
    resetPass_page.navigate()
    resetPass_page.reset_password("Admin1")

    #Selecctores
    url_actual = page.url
    url_esperada = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/sendPasswordReset'

    #Validacines
    assert url_actual == url_esperada, f"Se esperaba {url_esperada}, pero se obtuvo {url_actual}"
    resetPass_page.reset_confirm()

    page.screenshot(path="screenshots/resetPass/test_resetPass_user.png", full_page=True)

    page.close()

def test_resetPass_null(browser):
    page = browser.new_page()
    resetPass_page = ResetPassword(page)
    resetPass_page.navigate()
    resetPass_page.reset_password("")

    #Selecctores
    alert = page.locator(".oxd-text.oxd-text--span.oxd-input-field-error-message.oxd-input-group__message")

    expect(alert).to_be_visible()
    expect(alert).to_have_text("Required")

    page.screenshot(path="screenshots/resetPass/test_resetPass_null.png", full_page=True)

    page.close()

def test_reset_cancel(browser):
    page = browser.new_page()
    resetPass_page = ResetPassword(page)
    resetPass_page.navigate()

    #Click cancel
    resetPass_page.cancel()

    #Selecctores
    url_actual = page.url
    url_esperada = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'

    assert url_actual == url_esperada, f"Se esperaba {url_esperada}, pero se obtuvo {url_actual}"

    page.wait_for_timeout(2000)

    page.screenshot(path="screenshots/resetPass/test_reset_cancel.png", full_page=True)

    page.close()