import argparse
from selenium import webdriver
from pom.WelcomePage import WelcomePage
from pom.LoginPage import LoginPage
from pom.NotesPage import NotesPage

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

page_notes = NotesPage(driver)
page_notes.addNote("C flat", "Not actually a note; would be B")
note = page_notes.getNote("C flat")
assert(note == "Not actually a note; would be B")

driver.close()
