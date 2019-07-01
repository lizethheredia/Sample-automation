from selenium import webdriver
import re

driver = webdriver.Firefox()
driver.implicitly_wait(3)

def getInitialPage(driver):
    driver.get("http://testapp.galenframework.com")

def submitCredentials(driver, username, password):
    preLoginButton = driver.find_element_by_css_selector("#welcome-page .button-login")
    assert(preLoginButton is not None)
    preLoginButton.click()

    userField = driver.find_element_by_name("login.username")
    assert(userField is not None)
    passField = driver.find_element_by_name("login.password")
    assert(passField is not None)

    userField.clear()
    passField.clear()

    userField.send_keys(username)
    passField.send_keys(password)

    loginButton = driver.find_element_by_css_selector("#login-page .button-login")
    assert(loginButton is not None)
    loginButton.click()

def addNote(driver, noteTitle, noteDescription):
    addNoteButton = driver.find_element_by_css_selector("#my-notes-page button.btn-primary")
    assert(addNoteButton is not None)
    addNoteButton.click()

    noteTitleField = driver.find_element_by_name("note.title")
    assert(noteTitleField is not None)
    noteDescriptionField = driver.find_element_by_name("note.description")
    assert(noteDescriptionField is not None)
    submitNoteButton = driver.find_element_by_css_selector("#ad-note-page .btn-primary")
    assert(submitNoteButton is not None)

    noteTitleField.clear()
    noteDescriptionField.clear()

    noteTitleField.send_keys(noteTitle)
    noteDescriptionField.send_keys(noteDescription)

    submitNoteButton.click()

def containsNote(driver, titleToCheck, descriptionToCheck):
    notes = driver.find_elements_by_css_selector("#my-notes-page .list-group-item")
    assert(notes is not None)

    theDesiredNote = None
    for note in notes:
        title = note.find_element_by_css_selector("h4.list-group-item-heading")
        assert(title is not None)
        description = note.find_element_by_css_selector("p.list-group-item-text")
        assert(description is not None)

        if title.text == titleToCheck and description.text == descriptionToCheck:
            theDesiredNote = note
            break

    return True if theDesiredNote is not None else False

#Requires the driver to be on the notes page
def testNote(driver, noteTitle, noteDescription):
    addNote(driver, noteTitle, noteDescription)
    assert(containsNote(driver, noteTitle, noteDescription))


getInitialPage(driver)
submitCredentials(driver, "testuser@example.com", "test123")
testNote(driver, "C flat", "Not actually a note; would be B")
testNote(driver, "<script>alert('foo');</script>", "Is this vulnerable to html injection?")

driver.close()
