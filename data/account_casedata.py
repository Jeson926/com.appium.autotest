#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@file   :account_casedata.py
#@time   :2020/4/17 19:36
#@Author :jmgen
#@Version:1.0
#@Desc   :
class AccountCaseData():
    addaccount_001 = {
        'case_no': 'addaccount_001',
        'info': '新建一个现金账户',
        'params': {'account': ['*现金测试账户*','dsgdj','shdgkdfh'],
                   'data': ['66.84'],
                   'remark': ['#现金测试账户#'],
                   'iconinfo': ['标准'],
                   'position': [18]},
        'script_step': {'step1': '输入账户名',
                        'step2': '选择账户图标',
                        'step3': '输入账户余额',
                        'step4': '输入备注信息',
                        'step5': '保存并校验账户是否创建成功'}
    }
    addaccount_002 = {
        'case_no': 'addaccount_002',
        'info': '新建一个现金账户',
        'params': {'account': ['**现金测试账户**'],
                   'data': ['66.84'],
                   'remark': ['#现金测试账户#'],
                   'iconinfo': ['标准'],
                   'position': [18]},
        'script_step': {'step1': '输入账户名',
                        'step2': '选择账户图标',
                        'step3': '输入账户余额',
                        'step4': '输入备注信息',
                        'step5': '保存并校验账户是否创建成功'}
    }
