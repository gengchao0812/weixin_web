from Page.Index.register import Register
from selenium.webdriver.chrome.webdriver import WebDriver
from Page.Index.base_page import BasePage

class Login(BasePage):


    def goto_register(self):
        #按钮的事件，按钮定位和事件分开

        self._driver.find_element_by_xpath('//*[@class="login_registerBar_link"]').click()
        # register = self.find('//*[@class="login_registerBar_link"]')
        # register = self.find(By.Xpath,'//*[@class="login_registerBar_link"]')
        # register.click()
        # 把driver传递
        return Register(self._driver)