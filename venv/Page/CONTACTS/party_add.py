from Page.Index.base_page import BasePage
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class PartyAdd(BasePage):
    def party_new(self):
        self._driver.find_elements_by_xpath('//*[@class="inputDlg_item"]/input[@class="qui_inputText ww_inputText"]')[0].send_keys("开发部")
        self._driver.find_element_by_xpath('//*[@class="qui_btn ww_btn ww_btn_Dropdown js_toggle_party_list"]').click()
        # self._driver.find_element_by_xpath('//*[@class="jstree jstree-5 jstree-default"]/ul/li/div').click()

        # ActionChains(self._driver).move_to_element(self._driver.find_element_by_xpath('//*[@class="jstree-anchor"]')).perform()
        # down_data_click = WebDriverWait(self._driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, '//a[@class="jstree-anchor jstree-clicked"]')))
        # time.sleep(2)
        # down_data_click.click()
        time.sleep(1)
        self._driver.find_element_by_xpath('//*[@class="jstree-container-ul jstree-children jstree-striped jstree-wholerow-ul jstree-no-dots"][2]/ul/li/a[0]').click()
        # element = self._driver.find_element_by_xpath('//*[@class="jstree jstree-5 jstree-default"]/ul/li/div')
        # self._driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        self._driver.find_element_by_xpath('//*[@class="qui_btn ww_btn ww_btn_Blue"]').click()
