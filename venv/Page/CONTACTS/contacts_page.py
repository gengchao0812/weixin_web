from Page.Index.base_page import BasePage
import time
class Contacts_Page(BasePage):
    """
    通讯录按钮事件
    """
    #添加成员
    def goto_contacts_add(self):
        self._driver.find_element_by_xpath('//*[@class="qui_btn ww_btn js_add_member"]').click()

    #导入导出
    def goto_in_out(self):
        self._driver.find_element_by_xpath('//*[@class="ww_btn_PartDropdown_left"]').click()

    #点击邀请
    def goto_Invitation(self):
        self._driver.find_element_by_xpath('//*[@class="ww_icon ww_icon_WeChatInviteInToolbar"]/..').click()
        time.sleep(1)
        self._driver.find_element_by_xpath('//*[@class="index_exploreDownloadDialog_pcLink"]').click()
