from selenium.webdriver.common.by import By
from pom.BasePage import BasePage
from pom.AddNotePage import AddNotePage

class NotesPage(BasePage):
    addNoteButtonLocator = (By.CSS_SELECTOR, "#my-notes-page button.btn-primary")
    notesLocator = (By.CSS_SELECTOR, "#my-notes-page .list-group-item")
    noteTitleLocator = (By.CSS_SELECTOR, "h4.list-group-item-heading")
    noteDescriptionLocator = (By.CSS_SELECTOR, "p.list-group-item-text")

    def clickAddNote(self):
        self.findAndClick(NotesPage.addNoteButtonLocator)

    def addNote(self, title, description):
        self.clickAddNote()
        page_addNote = AddNotePage(self.driver)
        page_addNote.addNote(title, description)

    def getNote(self, titleToGet):
        notes = self.waitForElements(NotesPage.notesLocator)
        assert(notes is not None)

        for note in notes:
            title = note.find_element(NotesPage.noteTitleLocator[0], NotesPage.noteTitleLocator[1])
            assert(title is not None)
            print(title.text)

            if title.text == titleToGet:
                description = note.find_element(NotesPage.noteDescriptionLocator[0], NotesPage.noteDescriptionLocator[1])
                assert(description is not None)
                return description.text

        return None
