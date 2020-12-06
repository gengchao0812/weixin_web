from Page.Index.base_page import BasePage
from Page.CONTACTS.contacts_page import Contacts_Page
import time

class WorkIndex(BasePage):

    def goto_contacts(self):
        self._driver.find_element_by_xpath('//*[@id="menu_contacts"]').click()
        time.sleep(1)
        return Contacts_Page(self._driver)