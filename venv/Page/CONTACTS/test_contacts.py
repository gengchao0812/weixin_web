from Page.Index.base_page import BasePage
from Page.CONTACTS.work_index import WorkIndex
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import pytest


class TestContacts():
    _base_url = 'https://work.weixin.qq.com/wework_admin/frame#index'

    def setup(self):
        self.index = WorkIndex()

    #微信邀请案例已过，抓取弹出框是否显示
    @pytest.skip
    def test_wechat_invitation(self):
        self.index.goto_contacts().goto_Invitation()
        # assert self.index._driver.find_element_by_xpath('//*[@id="party_name"]').text == '霍格沃兹'
        assert WebDriverWait(self.index._driver,10).until(EC.visibility_of_element_located((By.CLASS_NAME,'ww_tip error')))

    #新增通讯录功能
    def test_contacts_add_new(self):

        assert  WebDriverWait(self.index._driver,10).until(EC.visibility_of_element_located((By.CLASS_NAME,'ww_tip success')))