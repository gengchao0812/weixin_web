import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import random
import yaml
import datetime


class BasePage():

    _driver = None
    _base_url=""
    _list=[]

    def __init__(self,driver: WebDriver = None):
        if driver is None:
            chrome_options = Options()
            # 和浏览器打开的调试端口进行通信
            # 浏览器要使用Chrome --remote-debugging-port=9222 开启调试
            chrome_options.debugger_address = "127.0.0.1:9222"
            self._driver = webdriver.Chrome(options=chrome_options)
            self._driver.implicitly_wait(3)
        else:
            self._driver = driver
        if self._base_url != "":
            self._driver.get(self._base_url)
            # 隐式等待10秒
            self._driver.implicitly_wait(10)

    #
    # def find(self,locator):
    #     print(f"开始用xpath查找{locator}")
    #     return self._driver.find_element_by_xpath(locator)

    #生成人员规模随机数
    def get_data_value(self):
        data_value=['2001','2002','2003','2004','2005','2006']
        n=random.randint(0,5)
        self._list.append(data_value[n])
        return data_value[n]

    #生成时间戳随机数
    @property
    def get_random_time(self):
        nowTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S");
        randomNum = random.randint(0, 99);
        if randomNum <= 10:
            randomNum = str(0) + str(randomNum);
        uniqueNum = str(nowTime) + str(randomNum);
        return uniqueNum

    def get_random_telphone(self):
        nowTime = datetime.datetime.now().strftime("%d%H%M%S")
        a = 158
        return (str(a) + str(nowTime))

