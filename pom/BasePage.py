from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Maximum time to wait for elements
timeout = 10

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def waitForElement(self, locator):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def waitForElements(self, locator):
        # HACK: There isn't a native way to wait for all matching elements to be
        #       clickable, so we wait for the first one to be clickable, get an
        #       array of all of them, and return that.
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        return self.driver.find_elements(locator[0], locator[1])

    def findAndTypeInto(self, locator, text):
        element = self.waitForElement(locator)
        assert(element is not None)
        element.clear()
        element.send_keys(text)

    def findAndClick(self, locator):
        element = self.waitForElement(locator)
        assert(element is not None)
        element.click()
