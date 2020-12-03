from Page.Index.register import Register
from selenium.webdriver.remote.webdriver import WebDriver

class Login():

    def __init__(self,driver: WebDriver):
        self.driver = driver

    def goto_register(self):
        #按钮的事件，按钮定位和事件分开

        register = self.driver.find_element_by_xpath('//*[@class="login_registerBar_link"]')
        register.click()
        # 把driver传递
        return Register(self.driver)