#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@file   :run_android.py
#@time   :2020/4/17 9:47
#@Author :jmgen
#@Version:1.0
#@Desc   :
import sys
from common.run import Run
from common.utils import Conf

"""
run all case:
    python3 run_android.py

run one module case:
    python3 run_android.py testcase/test_ui/test_account/test_addaccount.py
    python3 run_android.py testcase/test_ui

run case with key word:
    python3 run_android.py -k <keyword>
run class case:
    python3 run_android.py  test/test_demo.py::Test_demo
run class::method case:
    python3 run_android.py  test/test_demo.py::Test_demo::test_home
"""
if __name__ == '__main__':
    platformname=Conf().androidname  #android  or  ios
    run=Run(platformname)
    #获取命令行参数中的用例执行作用域
    run.exec(sys.argv[1:])
    run.generate_report()