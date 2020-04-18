#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@file   :conftest.py
#@time   :2020/4/17 14:49
#@Author :jmgen
#@Version:1.0
#@Desc   :
# import pytest
from util.utils import Conf
# from page.account.set import Account

conf = Conf()

if conf.platform == conf.androidname:
    from util.conf_android import *
elif conf.platform == conf.iosname:
    from util.conf_ios import *


#运行时通过执行的配置的平台决定导入的模块
#导入base.conftest里的pytest上下文环境函数:driverenv、action(ElementActions的实例)、caselog
#pytest框架运行原理：先运行test文件夹下面的conftest.py，然后才运行带test开头的py文件

# @pytest.fixture('package',autouse=True)
# def suitinit(action):
#     # p.特卖首页.home(action)
#     Account.add_account.pageinto(action)
#     # base_business.set_appenv(action)