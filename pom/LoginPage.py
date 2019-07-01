from selenium.webdriver.common.by import By
from pom.BasePage import BasePage

class LoginPage(BasePage):
    usernameFieldLocator = (By.NAME, "login.username")
    passwordFieldLocator = (By.NAME, "login.password")
    loginButtonLocator = (By.CSS_SELECTOR, "#login-page .button-login")
    cancelButtonLocator = (By.CSS_SELECTOR, "#login-page .button-cancel")

    def enterUsername(self, username):
        self.findAndTypeInto(LoginPage.usernameFieldLocator, username)

    def enterPassword(self, password):
        self.findAndTypeInto(LoginPage.passwordFieldLocator, password)

    def clickLogin(self):
        self.findAndClick(LoginPage.loginButtonLocator)

    def clickCancel(self):
        self.findAndClick(LoginPage.cancelButtonLocator)

    def submitCredentials(self, username, password):
        self.enterUsername(username)
        self.enterPassword(password)
        self.clickLogin()
