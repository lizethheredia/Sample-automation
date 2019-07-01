import argparse
from selenium import webdriver
from pom.WelcomePage import WelcomePage
from pom.LoginPage import LoginPage

parser = argparse.ArgumentParser(description="Test login and note-adding")
parser.add_argument("-u", dest="username", help="The username to log in with")
parser.add_argument("-p", dest="password", help="The password to log in with")

args = parser.parse_args()

driver = webdriver.Firefox()
driver.get("http://testapp.galenframework.com")

page_welcome = WelcomePage(driver)
page_welcome.clickLogin()

page_login = LoginPage(driver)
page_login.submitCredentials(args.username, args.password)
