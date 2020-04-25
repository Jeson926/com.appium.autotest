#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@file   :envinfo.py
#@time   :2020/4/16 19:38
#@Author :jmgen
#@Version:1.0
#@Desc   :
import abc,time
from common.utils import singleton
from common.shell import Shell,Device,get_command
from common.logger import Logger
from config.config_android import Config_Android
from config.config_ios import Config_iOS
from config.config_api import Config_Api

log = Logger(name=__file__).get_logger()
#环境的抽象类
class Environment(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def check_environment(self):
        pass

@singleton
class EnvironmentAndroid(Environment):
    def __init__(self):
        self.conf=Config_Android()
        self.appium = self.conf.appium #key: apk、appActivity、appPackage、appiumversion
        self.path=self.conf.path
        self.devices=self.conf.devices
        #最开始运行时动态获取，存储suit和device的对应关系
        self.current_device={}
        self.current_path=None

    def callback_current_device(self,device:dict):
        #传入当前的device信息
        self.current_device=device

    def callback_current_path(self,current_path):

        self.current_path=current_path

    def check_environment(self):
        log.info('检查环境...')
        get_command()

        # 检查设备
        current_devices = Device.get_android_devices()
        if len(current_devices) == 0:
            log.info('没有设备连接')
            exit()
        for key,device in self.devices.items():
            deviceName = device.get("deviceName")
            if deviceName in current_devices:
                log.info('已正常连接设备{}'.format(deviceName))
            else:
                log.error('设备{}未正常连接'.format(deviceName))

            # 检查appium版本
            appium_v = Shell.invoke('appium -v')
            if self.appium.get("version") not in appium_v:
                log.info('appium 版本有问题')
                exit()
            else:
                log.info('appium version {}'.format(appium_v))

            # 检测appium-doctor输出
            result = Shell.invoke('appium-doctor').splitlines()
            log.info(result)

@singleton
class EnvironmentIOS(Environment):
    def __init__(self):
        self.conf=Config_iOS()
        self.appium = self.conf.appium
        self.path=self.conf.path
        self.devices=self.conf.devices
        #最开始运行时动态获取，存储suit和device的对应关系
        self.current_device={}
        self.current_path=None

    def callback_current_device(self,device:dict):
        #传入当前的device信息
        self.current_device=device

    def callback_current_path(self,current_path):

        self.current_path=current_path

    def start_device(self):
        devices = dict(self.devices)
        for d in devices:
            Shell.invoke("xcrun instruments -w " + "'" + d.get('iphonename') + '(' + d.get('deviceName') + ')' + "'")
            time.sleep(10)
            self.install_app()
        return devices

    def install_app(self):
        Shell.invoke("xcrun simctl install booted {}".format(self.appium.get('app')))

    def uninstall_app(self):
        Shell.invoke("xcrun simctl uninstall booted {}".format(self.appium.get('bundleId')))

    def check_environment(self):
        log.info('检查环境...')
        get_command()

        # 检查设备
        current_devices = Device.get_ios_devices()
        if len(current_devices) == 0:
            log.info('没有设备连接')
            exit()
        for key,device in self.devices.items():
            deviceName = device.get("deviceName")
            if deviceName in current_devices:
                log.info('已正常连接设备{}'.format(deviceName))
            else:
                log.error('设备{}未正常连接'.format(deviceName))

            # 检查appium版本
            appium_v = Shell.invoke('appium -v')
            if self.appium.get("version") not in appium_v:
                log.info('appium 版本有问题')
                exit()
            else:
                log.info('appium version {}'.format(appium_v))

            # 检测appium-doctor输出
            result = Shell.invoke('appium-doctor').splitlines()
            log.info(result)