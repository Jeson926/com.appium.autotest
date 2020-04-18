#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@file   :test_addaccount.py
#@time   :2020/4/17 10:10
#@Author :jmgen
#@Version:1.0
#@Desc   :
from util.action import ElementActions
from page.account.collect import Account
from data.account_casedata import  AccountCaseData as data

class Test_Add_Account(Account):

    def test_addaccount_001(self, action: ElementActions):
        # action.click(Account.add_account.account)
        self.sub_into_account(action)
        action.click(self.add_account.add)
        action.click(self.add_account.cash)
        action.input_text(self.add_account.account_name,data.addaccount_001.get('params').get('account'))
        action.click(self.add_account.create)

    def test_addaccount_002(self, action: ElementActions):
        # action.click(Account.add_account.account)
        self.sub_into_account(action)
        action.click(self.add_account.add)
        action.click(self.add_account.cash)
        action.input_text(self.add_account.account_name, data.addaccount_002.get('params').get('account'))
        action.click(self.add_account.create)



