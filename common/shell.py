#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@file   :shell.py
#@time   :2020/4/16 20:30
#@Author :jmgen
#@Version:1.0
#@Desc   :
from common.logger import Logger
import subprocess,os,platform
log = Logger(name=__file__).get_logger()
def get_command():
    # 判断是否设置环境变量ANDROID_HOME
    if "ANDROID_HOME" in os.environ:
        command = os.path.join(
            os.environ["ANDROID_HOME"],
            "platform-tools",
            "adb")
    else:
        raise EnvironmentError(
            "Adb not found in $ANDROID_HOME path: %s." %
            os.environ["ANDROID_HOME"])
    return command

#Device类，用get_android_devices返回执行adb devices命令时的devices信息（即获取当前链接的机子devicename）
class Device:
    @staticmethod
    def get_android_devices():
        android_devices_list = []
        for device in Shell.invoke('adb devices').splitlines():
            if 'device' in device and 'devices' not in device:
                device = device.split('\t')[0]
                android_devices_list.append(device)
        return android_devices_list

    @staticmethod
    def get_ios_devices():
        ios_devices_list=[]
        for device in Shell.invoke('Instruments -s devices').splitlines():
            if 'device' in device and 'devices' not in device:
                device = device.split('\t')[0]
                ios_devices_list.append(device)
        return ios_devices_list

class Shell:
    @staticmethod
    def invoke(cmd,cwd=None,is_log=True):
        # shell设为true，程序将通过shell来执行
        # stdin, stdout, stderr分别表示程序的标准输入、输出、错误句柄。
        # 他们可以是PIPE，文件描述符或文件对象，也可以设置为None，表示从父进程继承。
        # subprocess.PIPE实际上为文本流提供一个缓存区
        if is_log==True:
            log.info("执行命令: {}".format(cmd))
        p= subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,cwd=cwd)
        output, errors=p.communicate()
        if(platform.system()=='Windows'):
            out= output.decode("utf-8","ignore")
        else:
            out = output.decode("utf-8")
        return out

class ADB:
    """
      参数:  device_id
    """
    def __init__(self, device_id=""):
        self.command=get_command
        if device_id == "":
            self.device_id = ""
        else:
            self.device_id = "-s %s" % device_id

    def adb(self, args):
        cmd = "%s %s %s" % (self.command, self.device_id, str(args))
        return Shell.invoke(cmd)

    def shell(self, args):
        cmd = "%s %s shell %s" % (self.command, self.device_id, str(args),)
        return Shell.invoke(cmd)

    def get_device_state(self):
        """
        获取设备状态： offline | bootloader | device
        """
        device_state=self.adb("get-state").strip(' \t\n\r')
        return device_state

    def get_device_id(self):
        """
        获取设备id号，return serialNo
        """
        device_id=self.adb("get-serialno").strip(' \t\n\r')
        return device_id

    def get_android_version(self):
        """
        获取设备中的Android版本号，如4.2.2
        """
        android_version=self.shell(
            "getprop ro.build.version.release").strip()
        return android_version

    def get_sdk_version(self):
        """
        获取设备SDK版本号
        """
        sdk_version=self.shell("getprop ro.build.version.sdk").strip()
        return sdk_version

    # 得到手机信息
    def get_phone_info(self,devicename):
        cmd = "adb -s " + devicename + " shell cat /system/build.prop "
        cmd2 = "adb -s " + devicename + " shell dumpsys window displays "

        phone_info = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE).stdout.readlines()
        display_info = subprocess.Popen(cmd2, shell=True, stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE).stdout.readlines()
        result = {"release": "release", "model": "model", "brand": "brand", "device": "device", "display": "display"}
        release = "ro.build.version.release="  # 版本
        model = "ro.product.model="  # 型号
        brand = "ro.product.brand="  # 品牌
        device = "ro.product.device="  # 设备名
        display = "init="  # 分辨率
        for line in phone_info:
            for i in line.split():
                temp = i.decode()
                if temp.find(release) >= 0:
                    result["release"] = temp[len(release):]
                    break
                if temp.find(model) >= 0:
                    result["model"] = temp[len(model):]
                    break
                if temp.find(brand) >= 0:
                    result["brand"] = temp[len(brand):]
                    break
                if temp.find(device) >= 0:
                    result["device"] = temp[len(device):]
                    break
        for line in display_info:
            for i in line.split():
                temp = i.decode()
                if temp.find(display) >= 0:
                    result["display"] = temp[len(display):]
                    break
        return  result

    # 获取测试包版本号和更新时间
    def get_app_version(self,devicename):
        cmd = "adb -s " + devicename + " shell dumpsys package com.mymoney"
        app_info = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
        # print(app_info)
        result = {"version": "version", "updatetime": "updatetime"}
        version = "versionName="  # 版本
        updatetime = "lastUpdateTime="  # 时间
        for line in app_info:
            for i in line.split():
                temp = i.decode()
                if temp.find(version) >= 0:
                    result["version"] = temp[len(version):]
                    break
                if temp.find(updatetime) >= 0:
                    result["updatetime"] = temp[len(updatetime):]
                    break
        return result