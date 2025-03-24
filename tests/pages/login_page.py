class LoginPage:
    #Constructor
    def __init__(self, page):
        self.page = page
        #Selecctores
        self.username = 'input[placeholder="Username"]'
        self.password = 'input[placeholder="Password"]'
        self.login_button = 'button[type="submit"]'

    def navigate(self):
        #Navegar a la página
        self.page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    
    def login(self, username, password):
        #Llenar campos de login y hacer click en el botón de login
        self.page.fill(self.username, username) 
        self.page.fill(self.password, password)
        self.page.click(self.login_button)