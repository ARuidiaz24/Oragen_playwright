from playwright.sync_api import expect

class ResetPassword:
    
    #Constructor
    def __init__(self, page):
        
        self.page = page

        #Selecctores
        self.username = 'input[placeholder="Username"]'
        self.buttonReset = 'button[type="submit"]'
        self.buttonCancel = 'button[type="button"]'
        self.title = page.locator('.oxd-text.oxd-text--h6.orangehrm-forgot-password-title')
        self.card = page.locator('.orangehrm-card-container')
        self.text_uno = page.locator('body > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > p:nth-child(3) > p:nth-child(1)')
        self.text_dos = page.locator('body > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > p:nth-child(4) > p:nth-child(1)')
        self.title_note = page.locator('.oxd-text.oxd-text--p.orangehrm-sub-title')
        self.text_note = page.locator("p[class='oxd-text oxd-text--p orangehrm-card-note orangehrm-card-note--background orangehrm-forgot-password-card-note'] p[class='oxd-text oxd-text--p']")
    
    def navigate(self):
        #Navegar a la página
        self.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/requestPasswordResetCode")
    
    def reset_password(self, username):
        #Llenar campo de usuario y hacer click en el botón de reset
        self.page.fill(self.username, username)
        self.page.click(self.buttonReset)

    def cancel(self):
        #Hacer click en el botón de cancelar
        self.page.click(self.buttonCancel)
    
    
    def reset_confirm(self):
        #Validación de card visible
        expect(self.card).to_be_visible()

        #Validación de texto en card
        expect(self.title).to_have_text("Reset Password link sent successfully")
        expect(self.text_uno).to_have_text("A reset password link has been sent to you via email.")
        expect(self.text_dos).to_have_text("You can follow that link and select a new password.")
        expect(self.title_note).to_have_text("Note:")
        expect(self.text_note).to_have_text("If the email does not arrive, please contact your OrangeHRM Administrator.")