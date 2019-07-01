from selenium.webdriver.common.by import By
from pom.BasePage import BasePage
from pom.LoginPage import LoginPage

class WelcomePage(BasePage):
    loginButtonLocator = (By.CSS_SELECTOR, "#welcome-page .button-login")

    def __init__(self, driver):
        BasePage.__init__(self, driver)

        self.loginButton = self.waitForElement(WelcomePage.loginButtonLocator)
        assert(self.loginButton is not None)

    def clickLogin(self):
        self.loginButton.click()
