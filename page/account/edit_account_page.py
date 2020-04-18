#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@file   :edit_account_page.py
#@time   :2020/4/17 13:58
#@Author :jmgen
#@Version:1.0
#@Desc   :
from util.page import BasePage

class Edit_Account_Page(BasePage):
    name='编辑账户'

    def load_android(self):
        self.cash = self.get_locator('现金','XPATH', self.text_view_text("现金"))
        self.add = self.get_locator('添加','XPATH', self.text_view_desc("添加"))
        self.save=self.get_locator('保存','XPATH', self.text_view_text("保存"))