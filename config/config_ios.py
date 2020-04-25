#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@file   :config_ios.py
#@time   :2020/4/22 13:41
#@Author :jmgen
#@Version:1.0
#@Desc   :
class Config_iOS:
    appium = {
        'app': '/Users/apple/Desktop/MyMoneyPro.app',
        'bundleId': 'com.kingdee.MyMoneyPro',
        # 'bundleId': 'com.kingdee.MyMoney',
        'automationName': 'XCUITest',
        'xcodeOrgId': '7BUCF2VZ84',
        'xcodeSigningId': 'iPhone Developer',
        'appiumversion': '1.15.1',
        'host': 'http://localhost:4723/wd/hub',
    }
    devices = {
        'device1': {
            'deviceName': '979c83a516aa5252c5c4f18f93866cd35cc91ee4',
            'iphonename':'linhuang_Test_iPhone X',
            'platformName': 'ios',
            'platformVersion': '12.4',
            'appiumserver': 'http://localhost:4723/wd/hub',
            'systemPort': '8202'
        },
        # 'device2': {
        #     "deviceName": '8e4ecce5',
        #     'platformName': 'Android',
        #     'platformVersion': '8.1.0',
        #     'appiumserver': 'http://localhost:4723/wd/hub',
        #     'systemPort': '8201'
        # },
    }
    path = {
        'tests': 'testcase',
        'report': 'report'
    }