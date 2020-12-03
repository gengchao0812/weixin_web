from Page.Index.index import Index
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time

class TestRegister:
    #继承Index类

    def setup(self):
        self.index=Index()

    def test_register(self):
        #按照步骤编写流程
        resurt=self.index.goto_register().register("这里是企业名称","这里是姓名")
        time.sleep(3)
        WebDriverWait(self.index.driver,10).until(EC.visibility_of_element_located((By.CLASS_NAME,'register_result_fromThirdAuthInner')))
        title=self.index.driver.find_element_by_xpath('//*[@class="register_result_fromThirdAuth"]/div[2]')
        assert title.text == '注册成功，扫码下载企业微信使用'
    #
    # def teardown(self):
    #     self.index.driver.quit()