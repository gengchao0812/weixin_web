from Page.Index.base_page import BasePage
from Page.CONTACTS.work_index import WorkIndex
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import pytest
import yaml
import os

class TestContacts():
    _base_url = 'https://work.weixin.qq.com/wework_admin/frame#index'

    def setup(self):
        self.index = WorkIndex()

    # 获取当前文件路径
    filePath = os.path.dirname(__file__)
    # 获取当前文件的Realpath  D:\WorkSpace\StudyPractice\Python_Yaml\YamlStudy\YamlDemo.py
    fileNamePath = os.path.split(os.path.realpath(__file__))[0]
    #新增通讯录功能
    @pytest.mark.skip
    # @pytest.mark.run(order=1)
    @pytest.mark.parametrize("username,englishname",yaml.safe_load(open(f"{fileNamePath}\\name.yml",encoding='utf-8')))
    def test_contacts_add_new(self,username,englishname):
        self.index.goto_contacts().goto_contacts_add().contacts_new(username,englishname)
        self.index._driver.implicitly_wait(3)
        assert  WebDriverWait(self.index._driver,10).until(EC.visibility_of_element_located((By.ID,'js_tips')))

    #微信邀请案例已过，抓取弹出框是否显示
    # @pytest.mark.run(order=2)
    @pytest.mark.skip
    def test_wechat_invitation(self):
        self.index.goto_contacts().goto_Invitation()
        # assert self.index._driver.find_element_by_xpath('//*[@id="party_name"]').text == '霍格沃兹'
        assert WebDriverWait(self.index._driver,10).until(EC.visibility_of_element_located((By.ID,'js_tips')))
        self.index._driver.find_element_by_xpath('//*[@class="qui_dialog ww_dialog ww_dialog_NoFoot index_exploreDownloadDialog"]/div[1]/a[1]').click()

    def test_go_back(self):
        self.index.goto_contacts().goto_next_back()