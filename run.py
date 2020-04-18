#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@file   :run.py
#@time   :2020/4/17 9:47
#@Author :jmgen
#@Version:1.0
#@Desc   :
import sys
# import pytest
# from multiprocessing import Pool
from util.run import Run
from util.utils import Conf
# from util.logger import log
# from util.shell import Shell

"""
run all case:
    python3 run.py

run one module case:
    python3 run.py testcase/test_account/test_addaccount.py

run case with key word:
    python3 run.py -k <keyword>
run class case:
    python3 run.py  test/test_demo.py::Test_demo
run class::method case:
    python3 run.py  test/test_demo.py::Test_demo::test_home
"""
if __name__ == '__main__':
    platform=Conf().androidname  #android  or  ios
    run=Run(platform)
    #获取命令行参数中的用例执行作用域
    run.exec(sys.argv[1:])
    run.generate_report()