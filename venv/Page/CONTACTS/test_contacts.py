from Page.Index.base_page import BasePage
from Page.CONTACTS.work_index import WorkIndex
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class TestContacts():
    _base_url = 'https://work.weixin.qq.com/wework_admin/frame#index'

    def setup(self):
        self.index = WorkIndex()


    def test_ba(self):
        self.index.goto_contacts().goto_Invitation()
        # assert self.index._driver.find_element_by_xpath('//*[@id="party_name"]').text == '霍格沃兹'
        assert WebDriverWait(self.index._driver,10).until(EC.visibility_of_element_located((By.CLASS_NAME,'ww_tip error')))
