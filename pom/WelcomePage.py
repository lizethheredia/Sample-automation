from selenium.webdriver.common.by import By
from pom.BasePage import BasePage
from pom.LoginPage import LoginPage

class WelcomePage(BasePage):
    loginButtonLocator = (By.CSS_SELECTOR, "#welcome-page .button-login")

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def clickLogin(self):
        self.findAndClick(WelcomePage.loginButtonLocator)
