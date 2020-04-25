#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@file   :env_check_ios.py
#@time   :2020/4/24 12:39
#@Author :jmgen
#@Version:1.0
#@Desc   :
from common.envinfo import EnvironmentIOS

#检测环境和启动appium
if __name__ == '__main__':
    env=EnvironmentIOS()
    env.check_environment()