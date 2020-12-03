import pytest
from selenium import webdriver
from Page.Index.register import Register
from Page.Index.download import Download
from Page.Index.base_page import BasePage
from Page.Index.login import Login
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Index(BasePage):
    #初始化driver
    #driver=webdriver.Chrome()
    #立即注册按钮
    def __init__(self):
        self.driver=BasePage.driver
        self.driver.get("https://work.weixin.qq.com/")
        # 隐式等待10秒
        self.driver.implicitly_wait(10)

    #点击立即注册按钮
    def goto_register(self):
        #按钮的事件，按钮定位和事件分开
        register = self.driver.find_element_by_xpath('//*[@class="index_head_info_pCDownloadBtn"]')
        register.click()
        # 把driver传递
        return Register(self.driver)

    #点击企业登录按钮
    def goto_login(self):
        # 按钮的事件，按钮定位和事件分开
        # 企业登录按钮
        login = self.driver.find_element_by_xpath('//*[@class="index_top_operation_loginBtn"]')
        login.click()
        #把driver传递
        return Login(self.driver)

    #点击下载按钮
    def goto_download(self):
        # 按钮的事件，按钮定位和事件分开
        # 下载按钮
        download = self.driver.find_element_by_xpath('//*[@class="index_top_operation_registerBtn"]')
        download.click()
        # 把driver传递
        return Download()
