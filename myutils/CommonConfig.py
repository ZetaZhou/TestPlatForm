import os
import logging
import sys
import queue
import traceback
import threading
import subprocess

from datetime import datetime
from collections import defaultdict

class CommonConfig():
    # def __new__(cls, *args, **kwargs):
    #     if not hasattr(CommonConfig, "_instance"):
    #         CommonConfig._instance = object.__new__(cls)
    #     return CommonConfig._instance

    def __init__(self):
        self.today = datetime.now().strftime('%Y_%m_%d')
        self.testcase_dirlist = ['.\\uiATMod\\uiAT_testcase\\', '.\\apiATMod\\apiAT_testcase\\']
        self.config_dir = '.\\config\\'
        self.result_dir = '.\\result\\'
        self.config = self.initconfig()

    def initconfig(self):
        '''
        初始化config文件, 把配置写入self.config字典中
        :return:
        '''
        config_dict = dict()
        with open(self.config_dir + 'config.txt', 'r') as file:
            configdatalist = file.readlines()
        if '[config]' in configdatalist[0]:
            for configdata in configdatalist:
                try:
                    config = configdata.split('=')
                    config_dict[config[0]] = config[1].strip('\n ')
                except:
                    pass

        return config_dict

    def initLog(self):
        '''
        初始化log文件
        :return:
        '''

        from myutils.LogMethod import initlogfile

        initlogfile(self.config_dir, self.config['main_log'], 'main')
        initlogfile(self.config_dir, self.config['detail_log'], 'detail')

        # self.loggermain = logging.getLogger("main")
        # self.loggerdetail = logging.getLogger("detail")

    @staticmethod
    def getCurrentTime():
        format = "%Y-%m-%d %H:%M:%S"
        return datetime.now().strftime(format)

    @staticmethod
    def timeDiff(starttime, endtime):
        format = "%Y-%m-%d %H:%M:%S"
        return datetime.strptime(endtime, format) - datetime.strptime(starttime, format)
