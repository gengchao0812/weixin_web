import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Page.Index.base_page import BasePage
import time
import yaml
import allure

class Register(BasePage):
    """
    企业注册模块
    """
    def __init__(self, driver: WebDriver):
        self.driver = driver
    
    def register(self,corp_name):
        #企业名称
        
        self.driver.find_element_by_xpath('//*[@id="corp_name"]').send_keys(corp_name)
        #行业类型
        self.driver.find_element_by_xpath('//*[@id="corp_industry"]').click()
        self.driver.find_element_by_xpath('//*[@data-value="1001"]').click()
        self.driver.find_element_by_xpath('//*[@data-value="1001000"]').click()
        #人员规模
        self.driver.find_element_by_xpath('//*[@id="corp_scale_btn"]').click()
        data_value = self.get_data_value()
        self.driver.find_element_by_xpath(f'//*[@data-value="{data_value}"]').click()
        #勾选框
        self.driver.find_element_by_xpath('//*[@id="iagree"]').click()
        #管理员姓名
        self.driver.find_element_by_xpath('//*[@id="manager_name"]').send_keys("耿超")
        #管理员手机号
        self.driver.find_element_by_xpath('//*[@id="register_tel"]').send_keys("15810179927")
        #获取手机验证码
        self.driver.find_element_by_xpath('//*[@id="get_vcode"]').click()
        #手动填写验证码和扫描微信
        #点击注册
        # WebDriverWait(self.driver,30,1).until(EC.visibility_of_element_located(title))
        time.sleep(20)
        # title = self.driver.find_element_by_xpath('//*[@class="register_result_fromThirdAuth"]')
        # print(title.text)
        self.driver.find_element_by_xpath('//*[@id="submit_btn"]').click()
        self.driver.implicitly_wait(5)

