from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, driver, url, timeout=5):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)

    def open(self):
        self.driver.get(self.url)

    def is_element_present(self, by, value):
        try:
            self.driver.find_element(by, value)
        except NoSuchElementException:
            return False
        return True
