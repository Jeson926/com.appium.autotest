#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @file   :util.py
# @time   :2020/4/16 19:05
# @Author :jmgen
# @Version:1.0
# @Desc   :
import time, os
from config.config import Config
from util.shell import Shell
from util.logger import Logger

log = Logger(name=__file__).get_logger()
# 单例装饰器
def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance

def get_attrsname(obj):
    # 获取当前对象的非私有的属性名字列表
    attrs = [attr for attr in dir(obj) if not callable(attr) and not attr.startswith("__")]
    return attrs

def ls_by_key(path: str, key: str):
    # 获取当前路径下,通过ls命令获取的文件或文件夹名的列表,过滤条件为对应的key参数
    # 输出list
    result = []
    out = Shell.invoke('ls', cwd=path, is_log=False)
    for ele in out.splitlines():
        if key in ele:
            result.append(ele)
    return result

def dir_by_key(path: str, key: str):
    # 获取当前路径下,通过dir命令获取的文件或文件夹名的列表,过滤条件为对应的key参数
    # 输出list
    result = []
    out = Shell.invoke('dir', cwd=path, is_log=False)
    for ele in out.splitlines():
        if key in ele:
            result.append(ele.split(' ')[-1])
    return result

class Conf():
    def __init__(self):
        self.info =Config().platform
        self.androidname = 'android'
        self.iosname = 'ios'
        self.platform = Config.platform['run']

    def set_platform(self, platform):
        log.info("设置平台为：{}".format(platform))

class Waittime_count:
    # 用于计算一个步骤的执行时间，如果超出规定时间就输出日志
    def __init__(self, msg="等待时间有：", durationtime=3):
        self.msg = msg
        self.starttime = None
        self.endtime = None
        self.durationtime = durationtime

    def start(self):
        self.starttime = time.time()

    def end(self):
        self.endtime = time.time()
        Waittime = round(self.starttime - self.endtime, 2)
        if Waittime > self.durationtime:
            log.info(self.msg + " {}s ".format(Waittime))