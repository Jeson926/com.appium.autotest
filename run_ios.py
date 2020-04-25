#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@file   :run_ios.py
#@time   :2020/4/22 14:40
#@Author :jmgen
#@Version:1.0
#@Desc   :
import sys
from common.run import Run
from common.utils import Conf

"""
run all case:
    python3 run_ios.py

run one module case:
    python3 run_ios.py testcase/test_ui/test_account/test_addaccount.py
    python3 run_ios.py testcase/test_ui

run case with key word:
    python3 run_ios.py -k <keyword>
run class case:
    python3 run_ios.py  test/test_demo.py::Test_demo
run class::method case:
    python3 run_ios.py  test/test_demo.py::Test_demo::test_home
"""
if __name__ == '__main__':
    platformname=Conf().iosname  #android  or  ios
    run=Run(platformname)
    #获取命令行参数中的用例执行作用域
    run.exec(sys.argv[1:])
    run.generate_report()