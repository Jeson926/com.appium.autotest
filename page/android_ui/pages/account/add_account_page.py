#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@file   :add_account_page.py
#@time   :2020/4/17 13:56
#@Author :jmgen
#@Version:1.0
#@Desc   :
from common.page import BasePage
from selenium.webdriver.common.by import By
class Add_Account_Page(BasePage):
    name='添加新账户'

    def load_android(self):
        self.account=self.get_locator('首页账户',By.XPATH, self.button_text("账户"),page='首页')
        self.add = self.get_locator('添加',By.XPATH, self.text_view_desc("添加"),page='账户首页')
        self.cash = self.get_locator('现金', By.XPATH, self.text_view_text("现金"))
        self.account_name=self.get_locator('账户名',By.ID, "com.mymoney:id/name_et", page='账户添加页的账户名')
        self.create=self.get_locator('确认新建',By.XPATH, self.button_text("确认新建"), page='账户添加页的确认新建')