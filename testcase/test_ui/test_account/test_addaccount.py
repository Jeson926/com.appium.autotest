#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@file   :test_addaccount.py
#@time   :2020/4/17 10:10
#@Author :jmgen
#@Version:1.0
#@Desc   :
import allure,pytest
from common.action import ElementActions
from page.android_ui.actions.account import Account
from data.account_casedata import  AccountCaseData as data

@allure.feature("添加账户模块")
@allure.description('账户添加成功')
class Test_Add_Account(Account):
    @allure.story('现金账户名称正常，添加成功')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize('account_name',
                             data.addaccount_001.get('params').get('account'))
    def test_addaccount_001(self, action: ElementActions,account_name,):
        self.sub_into_account(action)
        self.sub_into_cash(action)
        # action.input_text(self.add_account.account_name,data.addaccount_001.get('params').get('account'))
        action.input_text(self.add_account.account_name,account_name)
        action.click(self.add_account.create)

    @allure.story('银行卡账户名称正常，添加成功')
    def test_addaccount_002(self, action: ElementActions):
        # action.click(Account.add_account.account)
        self.sub_into_account(action)
        action.click(self.add_account.add)
        action.click(self.add_account.cash)
        action.input_text(self.add_account.account_name, data.addaccount_002.get('params').get('account'))
        action.click(self.add_account.create)