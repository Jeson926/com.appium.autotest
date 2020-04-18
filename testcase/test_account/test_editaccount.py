#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@file   :test_editaccount.py
#@time   :2020/4/17 13:49
#@Author :jmgen
#@Version:1.0
#@Desc   :
from util.action import ElementActions
from page.account.collect import Account
class Test_Add_Account:

    def test_addaccount_001(self, action: ElementActions):
        action.click(Account.add_account.account)
        action.click(Account.add_account.add)
        action.click(Account.add_account.cash)

    def test_addaccount_002(self, action: ElementActions):
        action.click(Account.add_account.account)
        action.click(Account.add_account.add)
        action.click(Account.add_account.cash)