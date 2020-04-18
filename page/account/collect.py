#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@file   :collect.py
#@time   :2020/4/17 14:40
#@Author :jmgen
#@Version:1.0
#@Desc   :
from .add_account_page import Add_Account_Page
class Account:
    add_account=Add_Account_Page()
    def sub_into_account(self,action):
        action.click(self.add_account.account)
