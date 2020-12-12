from Page.Index.index import Index
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time
import pytest
import allure
import sys


class TestRegister:

    #继承Index类
    def setup(self):
        self.index=Index()

    @pytest.skip
    @allure.feature('注册模块')
    @pytest.mark.parametrize("corp_name",["名字1","名字2","名字3"])
    def test_register_create(self,corp_name):
        """
        注册模块
        :param corp_name:
        :return:
        """
        #按照步骤编写流程
        resurt=self.index.goto_register().register(corp_name)
        self.index._driver.implicitly_wait(10)
        # WebDriverWait(self.index.driver,10).until(EC.visibility_of_element_located((By.CLASS_NAME,'register_result_fromThirdAuthInner')))
        # title=self.index.driver.find_element_by_xpath('//*[@class="register_result_fromThirdAuth"]/div[2]')
        # try:
        #     title = self.index._driver.find_element_by_xpath('//*[@class="register_result_fromThirdAuth"]/div[2]')
        # except:
        #     time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        #     a = '%s_%s.png'.format(corp_name, time_now)
        #     self.index._driver.save_screenshot('{}_{}.png'.format(corp_name, time_now))
        # else:
        #     assert title.text == '注册成功，扫码下载企业微信使用'
        title1 = self.index._driver.find_element_by_xpath('//*[@class="registerResult_succeed_cnt_title"]')
        assert title1.text == '注册成功'
    #

    @allure.feature('增加员工')
    def test_adb(self):
        pass

    # def teardown(self):
    #     self.index.driver.quit()