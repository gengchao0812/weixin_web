from Page.Index.base_page import BasePage


class ContactsAdd(BasePage):



    def contacts_new(self,username,englishname):
        #姓名
        self._driver.find_element_by_xpath('//*[@id="username"]').send_keys(username)
        #别名
        self._driver.find_element_by_xpath('//*[@id="memberAdd_english_name"]').send_keys(englishname)
        #唯一标识（准备用时间戳做随机数）
        acctid = self.get_random_time
        self._driver.find_element_by_xpath('//*[@id="memberAdd_acctid"]').send_keys(acctid)
        #选男
        # self._driver.find_element_by_xpath('//*[@class="member_edit_formWrap "]/div[1]/div[3]/div[2]/label[1]/input').click()
        #选女
        self._driver.find_element_by_xpath('//*[@class="member_edit_formWrap "]/div[1]/div[3]/div[2]/label[2]/input').click()
        #手机号
        telephone = self.get_random_telphone()
        self._driver.find_element_by_xpath('//*[@class="qui_inputText ww_inputText ww_telInput_mainNumber"]').send_keys(telephone)

        # #修改标签为第二个
        # self._driver.find_element_by_xpath('//*[@class="member_edit_formWrap "]/div[3]/div[2]/div[2]/div[1]').click()
        # self._driver.find_element_by_xpath('//*[@class="qui_dialog ww_dialog qui_dialog ww_dialog ww_dialog_NoWidthLimit multiselect_dialog hidden_checkbox"]//*[@class="member_tag_list"]/li[2]').click()
        # self._driver.find_element_by_xpath(
        #     '//*[@class="qui_dialog ww_dialog qui_dialog ww_dialog ww_dialog_NoWidthLimit multiselect_dialog hidden_checkbox"]/div[3]/a').click()
        # # self._driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/a[1]').click()
        # $x('//div[text()="我的标签"]')
        #点击上方保存

        self._driver.find_elements_by_xpath('//*[@class="member_container"]/div[2]/div/div[4]/div/form[@class="js_member_editor_form"]/div/a')[1].click()