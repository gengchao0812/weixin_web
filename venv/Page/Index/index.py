import pytest
from selenium import webdriver
from Page.Index.register import Register
from Page.Index.download import Download
from Page.Index.base_page import BasePage
from Page.Index.login import Login
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import yaml

class Index(BasePage):

    # profile = yaml.safe_load(open('./comon.yaml'))
    # _base_url = profile['url']
    _base_url='https://work.weixin.qq.com/'

    #点击立即注册按钮
    def goto_register(self):
        #按钮的事件，按钮定位和事件分开
        self._driver.find_element_by_xpath('//*[@class="index_head_info_pCDownloadBtn"]').click()
        # register = self.find(By.Xpath,'//*[@class="index_head_info_pCDownloadBtn"]')
        # register = self.find('//*[@class="index_head_info_pCDownloadBtn"]')
        # 把driver传递
        return Register()

    #点击企业登录按钮
    def goto_login(self):
        # 按钮的事件，按钮定位和事件分开
        # 企业登录按钮
        login = self._driver.find_element_by_xpath('//*[@class="index_top_operation_loginBtn"]')
        login.click()
        #把driver传递
        return Login(self._driver)

    #点击下载按钮
    def goto_download(self):
        # 按钮的事件，按钮定位和事件分开
        # 下载按钮
        download = self._driver.find_element_by_xpath('//*[@class="index_top_operation_registerBtn"]')
        download.click()
        # 把driver传递
        return Download(self._driver)
