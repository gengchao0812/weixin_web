from Page.Index.base_page import BasePage
from Page.CONTACTS.work_index import WorkIndex
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import pytest
import yaml
import os
import logging


class TestContacts():
    _base_url = 'https://work.weixin.qq.com/wework_admin/frame#index'

    rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    log_path = os.path.dirname(os.getcwd()) + '/Logs/'
    log_name = log_path + rq + '.log'
    logfile = log_name
    logger = logging.getLogger(__name__)
    logger.setLevel(level=logging.INFO)
    handler = logging.FileHandler(logfile)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    def setup(self):
        self.index = WorkIndex()

    # 获取当前文件路径
    filePath = os.path.dirname(__file__)
    # 获取当前文件的Realpath  D:\WorkSpace\StudyPractice\Python_Yaml\YamlStudy\YamlDemo.py
    fileNamePath = os.path.split(os.path.realpath(__file__))[0]
    #新增通讯录功能
    @pytest.mark.skip
    # @pytest.mark.run(order=1)
    @pytest.mark.parametrize("username,englishname",yaml.safe_load(open(f"{fileNamePath}/name.yml",encoding='utf-8')))
    logger.info('开始新增人员用例')
    def test_contacts_add_new(self,username,englishname):
        self.index.goto_contacts().goto_contacts_add().contacts_new(username,englishname)
        self.index._driver.implicitly_wait(3)
        assert  WebDriverWait(self.index._driver,10).until(EC.visibility_of_element_located((By.ID,'js_tips')))

    #微信邀请案例已过，抓取弹出框是否显示
    # @pytest.mark.run(order=2)
    logger.info('开始微信分享用例')
    @pytest.mark.skip
    def test_wechat_invitation(self):
        self.index.goto_contacts().goto_Invitation()
        # assert self.index._driver.find_element_by_xpath('//*[@id="party_name"]').text == '霍格沃兹'
        assert WebDriverWait(self.index._driver,10).until(EC.visibility_of_element_located((By.ID,'js_tips')))
        self.index._driver.find_element_by_xpath('//*[@class="qui_dialog ww_dialog ww_dialog_NoFoot index_exploreDownloadDialog"]/div[1]/a[1]').click()

    logger.info('开始翻页案例')
    @pytest.mark.skip
    #测试翻页
    def test_go_back(self):
        self.index.goto_contacts().goto_next_back()
        assert self.index._driver.find_element_by_xpath('//*[@class="ww_pageNav_info_text"]').text == self.index.goto_contacts().goto_next_back()

    #添加部门
    logger.info('开始添加部门用例')
    @pytest.mark.skip
    def test_party_add(self):
        self.index.goto_contacts().goto_party_add().party_new()
        assert WebDriverWait(self.index._driver,10).until(EC.visibility_of_element_located((By.CLASS_NAME,'ww_tip success')))

    #文件上传
    logger.info('开始上传文件用例')
    def test_inout(self):
        self.index.goto_contacts().goto_in_out()
        assert WebDriverWait(self.index._driver,10).until(EC.visibility_of_element_located((By.CLASS_NAME,'ww_fileImporter_successImportText')))