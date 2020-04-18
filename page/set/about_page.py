#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@file   :about_page.py
#@time   :2020/4/17 13:57
#@Author :jmgen
#@Version:1.0
#@Desc   :
from util.page import BasePage

class About_Page(BasePage):
    name='关于页面'

    def load_android(self):
        self.set = self.get_locator('设置','XPATH', self.text_view_text("设置"))
        self.about = self.get_locator('关于','XPATH', self.text_view_desc("关于"))