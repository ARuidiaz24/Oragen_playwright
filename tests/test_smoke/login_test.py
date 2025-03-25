from playwright.sync_api import expect
from pages.login_page import LoginPage
from fixtures.browser import browser


# -------------Login con credenciales correctas-------------
def test_login_Correct(browser):
    page = browser.new_page()
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("Admin", "admin123")

    #Selecctores
    url_actual = page.url
    url_esperada = 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'

    #Validación de URL
    assert url_actual == url_esperada, f"Se esperaba {url_esperada}, pero se obtuvo {url_actual}"

    page.wait_for_timeout(2000) 
    page.screenshot(path="tests/test_smoke/screenshots/login/test_login_Correct.png", full_page=True)

    page.close()

# -------------Login con password incorrecta-------------
def test_login_password(browser):
    page = browser.new_page()
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("Admin", "admin12")

    #Selecctores
    alert = page.locator("div[role='alert']")
    text_alert = page.locator(".oxd-text.oxd-text--p.oxd-alert-content-text")

    #Validación que el elemento sea visible
    expect(alert).to_be_visible()

    #Validación texto de alerta de validación
    expect(text_alert).to_have_text("Invalid credentials")

    page.wait_for_timeout(1000) 
    page.screenshot(path="tests/test_smoke/screenshots/login/test_login_password.png", full_page=True)

    page.close()

# -------------Login con user incorrecta-------------
def test_login_user(browser):
    page = browser.new_page()
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("Admin1", "admin123")

    #Selecctores
    alert = page.locator("div[role='alert']")
    text_alert = page.locator(".oxd-text.oxd-text--p.oxd-alert-content-text")

    #Validación que el elemento sea visible
    expect(alert).to_be_visible()

    #Validación texto de alerta de validación
    expect(text_alert).to_have_text("Invalid credentials")

    page.wait_for_timeout(1000) 
    page.screenshot(path="tests/test_smoke/screenshots/login/test_login_user.png", full_page=True)

    page.close()

# -------------Login con campos nulos-------------
def test_login_null(browser):
    page = browser.new_page()
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("", "")

    #Selecctores
    alert_user = page.locator("//div[@class='orangehrm-login-slot-wrapper']//div[1]//div[1]//span[1]")
    alert_password = page.locator("//div[@class='orangehrm-login-form']//div[2]//div[1]//span[1]")

    #Validación que el elemento sea visible
    expect(alert_user).to_be_visible()
    expect(alert_password).to_be_visible()

    #Validación texto de alerta de validación
    expect(alert_user).to_have_text("Required")
    expect(alert_password).to_have_text("Required")

    page.wait_for_timeout(1000) 
    page.screenshot(path="tests/test_smoke/screenshots/login/test_login_null.png", full_page=True)

    page.close()

# -------------Redireccionar page recordar contraseña-------------  
def test_login_recor_password(browser):
    page = browser.new_page()
    login_page = LoginPage(page)
    login_page.navigate()

    #Click forgot you password
    recor_password = page.locator("//p[@class='oxd-text oxd-text--p orangehrm-login-forgot-header']")
    recor_password.click()

    #Selecctores
    url_actual = page.url
    url_esperada = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/requestPasswordResetCode'
    
    #Validación de URL
    assert url_actual == url_esperada, f"Se esperaba {url_esperada}, pero se obtuvo {url_actual}"

    page.wait_for_timeout(1000) 
    page.screenshot(path="tests/test_smoke/screenshots/login/test_login_recor_password.png", full_page=True)

    page.close()