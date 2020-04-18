#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@file   :env_check.py
#@time   :2020/4/17 9:53
#@Author :jmgen
#@Version:1.0
#@Desc   :
from util.envinfo import EnvironmentAndroid

#检测环境和启动appium
if __name__ == '__main__':
    env=EnvironmentAndroid()
    env.check_environment()