from Page.Index.base_page import BasePage
import time
from Page.CONTACTS.contacts_add import ContactsAdd
import re
from Page.CONTACTS.party_add import PartyAdd

class Contacts_Page(BasePage):
    """
    通讯录按钮事件
    """
    #添加成员
    def goto_contacts_add(self):
        self._driver.find_elements_by_xpath('//*[@class="qui_btn ww_btn js_add_member"]')[2].click()
        return ContactsAdd(self._driver)

    #导入导出
    def goto_in_out(self):
        self._driver.find_element_by_link_text('批量导入/导出').click()
        self._driver.find_element_by_link_text('文件导入').click()
        self._driver.find_element_by_xpath('//*[@class="ww_fileImporter_fileContainer_uploadInputMask"]').send_keys('H:\\333_test.xlsx')
        self._driver.find_element_by_link_text('导入').click()

    #点击邀请
    def goto_Invitation(self):
        self._driver.find_element_by_xpath('//*[@class="ww_icon ww_icon_WeChatInviteInToolbar"]/..').click()
        time.sleep(1)
        self._driver.find_element_by_xpath('//*[@class="index_exploreDownloadDialog_pcLink"]').click()

    #添加部门
    def goto_party_add(self):
        self._driver.find_element_by_xpath('//*[@class="member_colLeft_top_addBtnWrap js_create_dropdown"]').click()
        self._driver.find_element_by_xpath('//*[@class="js_create_party"]').click()
        return PartyAdd()

    #翻页功能
    def goto_next_back(self):
        _PageNumber = self._driver.find_elements_by_xpath('//*[@class="ww_pageNav_info_text"]')[1].text
        #（.+？）和（.*?）  一个及以上的匹配和任意多个匹配的区别  $ 取到尾
        PageNumberMax = re.findall('1/(.+?)$',_PageNumber)
        print(f"PageNumberMax={PageNumberMax}")
        for i in range(int(PageNumberMax[0])-1):
            self._driver.find_elements_by_xpath('//*[@class="ww_pageNav_info_arrowWrap js_next_page"]')[1].click()
            time.sleep(1)
        for i in range(int(PageNumberMax[0]) - 1):
            self._driver.find_elements_by_xpath('//*[@class="ww_pageNav_info_arrowWrap js_pre_page"]')[1].click()
            time.sleep(1)
        return _PageNumber