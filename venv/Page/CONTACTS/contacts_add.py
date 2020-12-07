from Page.Index.base_page import BasePage


class ContactsAdd(BasePage):

    def contacts_new(self,name,englishname):
        #姓名
        self._driver.find_element_by_xpath('//*[@id="username"]').send_keys(name)
        #别名
        self._driver.find_element_by_xpath('//*[@id="memberAdd_english_name"]').send_keys(englishname)
        #唯一标识（准备用时间戳做随机数）
        acctid = self.get_random_time()
        self._driver.find_element_by_xpath('//*[@id="memberAdd_acctid"]').send_keys(acctid)
        #选男
        self._driver.find_element_by_xpath('//*[@class="member_edit_item_right"]/lable[1]/input').click()
        #选女
        self._driver.find_element_by_xpath('//*[@class="member_edit_item_right"]/lable[2]/input').click()
        #手机号
        self._driver.find_element_by_xpath('//*[@class="ww_telInput_mainNumber"]').send_keys(telphone)

        #修改标签为第二个
        self._driver.find_element_by_xpath('//*[@class="member_edit_formWrap "]/div[3]/div[2]/div[2]/div').click()
        self._driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div/div/div[1]/div[1]/div[4]/div[3]/ul/li[2]').click()
        self._driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/a[1]').click()

        #点击上方保存
        self._driver.find_element_by_xpath('//*[@class="member_container"]/div[2]/div/div[4]/div/form[@class="js_member_editor_form"]/div/a')[0].click()