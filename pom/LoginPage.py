from selenium.webdriver.common.by import By
from pom.BasePage import BasePage

class LoginPage(BasePage):
    usernameFieldLocator = (By.NAME, "login.username")
    passwordFieldLocator = (By.NAME, "login.password")
    loginButtonLocator = (By.CSS_SELECTOR, "#login-page .button-login")
    cancelButtonLocator = (By.CSS_SELECTOR, "#login-page .button-cancel")

    def __init__(self, driver):
        BasePage.__init__(self, driver)

        self.usernameField = self.waitForElement(LoginPage.usernameFieldLocator)
        assert(self.usernameField is not None)
        self.passwordField = self.waitForElement(LoginPage.passwordFieldLocator)
        assert(self.passwordField is not None)
        self.loginButton = self.waitForElement(LoginPage.loginButtonLocator)
        assert(self.loginButton is not None)
        self.cancelButton = self.waitForElement(LoginPage.cancelButtonLocator)
        assert(self.cancelButton is not None)

    def enterUsername(self, username):
        self.usernameField.clear()
        self.usernameField.send_keys(username)

    def enterPassword(self, password):
        self.passwordField.clear()
        self.passwordField.send_keys(password)

    def clickLogin(self):
        self.loginButton.click()

    def clickCancel(self):
        self.cancelButton.click()

    def submitCredentials(self, username, password):
        self.enterUsername(username)
        self.enterPassword(password)
        self.clickLogin()
