from selenium import webdriver
import re

driver = webdriver.Firefox()
driver.implicitly_wait(3)

driver.get("http://testapp.galenframework.com")

# Log in
preLoginButton = driver.find_element_by_css_selector("#welcome-page .button-login")
preLoginButton.click()

userField = driver.find_element_by_name("login.username")
passField = driver.find_element_by_name("login.password")

userField.send_keys("testuser@example.com")
passField.send_keys("test123")

loginButton = driver.find_element_by_css_selector("#login-page .button-login")
loginButton.click()

# Add note
addNoteButton = driver.find_element_by_css_selector("#my-notes-page button.btn-primary")
addNoteButton.click()

noteTitleField = driver.find_element_by_name("note.title")
noteDescriptionField = driver.find_element_by_name("note.description")
submitNoteButton = driver.find_element_by_css_selector("#ad-note-page .btn-primary")

noteTitleField.send_keys("C flat")
noteDescriptionField.send_keys("Not actually a note, it would be B")

submitNoteButton.click()

# Verify note was added
notes = driver.find_elements_by_css_selector("#my-notes-page .list-group-item")
theDesiredNote = None
for note in notes:
    if re.search("C flat", note.text):
        theDesiredNote = note

assert(theDesiredNote is not None)

driver.close()
