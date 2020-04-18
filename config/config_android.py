#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @file   :config_android.py
# @time   :2020/4/16 19:47
# @Author :jmgen
# @Version:1.0
# @Desc   :
class Config_Android:
    appium = {
        'app': 'apk',
        'appPackage': 'com.mymoney',
        'appActivity': '.biz.main.v12.MainActivityV12',
        'appiumversion': '1.15.1',
        'host': 'http://localhost:4723/wd/hub',
    }
    devices = {
        'device1': {
            "deviceName": 'C7RGK16A18900656',
            'platformName': 'Android',
            'platformVersion': '7.1.2',
            'appiumserver': 'http://localhost:4723/wd/hub',
            'systemPort': '8201'
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
