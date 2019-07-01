from selenium.webdriver.common.by import By
from pom.BasePage import BasePage

class AddNotePage(BasePage):
    titleFieldLocator = (By.NAME, "note.title")
    descriptionFieldLocator = (By.NAME, "note.description")
    addNoteButtonLocator = (By.CSS_SELECTOR, "#ad-note-page .btn-primary")
    cancelButtonLocator = (By.CSS_SELECTOR, "#ad-note-page .btn-default")

    def enterTitle(self, title):
        self.findAndTypeInto(AddNotePage.titleFieldLocator, title)

    def enterDescription(self, description):
        self.findAndTypeInto(AddNotePage.descriptionFieldLocator, description)

    def clickAddNote(self):
        self.findAndClick(AddNotePage.addNoteButtonLocator)

    def clickCancel(self):
        self.findAndClick(AddNotePage.cancelButtonLocator)

    def addNote(self, title, description):
        self.enterTitle(title)
        self.enterDescription(description)
        self.clickAddNote()
