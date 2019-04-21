import os
import logging
import sys
import queue
import time
import traceback
import threading
import subprocess
import configparser

from datetime import datetime
from collections import defaultdict

from myutils.logmtd import setup_logging


class CommonConfig(object):
    # def __new__(cls, *args, **kwargs):
    #     if not hasattr(CommonConfig, "_instance"):
    #         CommonConfig._instance = object.__new__(cls)
    #     return CommonConfig._instance

    def __init__(self):
        self.today = datetime.now().strftime('%Y_%m_%d')
        self.testcase_dirlist = ['.\\uiATMod\\uiAT_testcase\\', '.\\apiATMod\\apiAT_testcase\\']
        self.config_dir = '.\\config\\'
        self.result_dir = '.\\result\\'
        self.config = self.initconfig('conf')
        self.mail_cfg = self.initconfig('mail')

        ''' 初始化日志 '''
        setup_logging()
        self.main_log = logging.getLogger('main')
        self.detail_log = logging.getLogger('detail')

    def initconfig(self, content):
        '''
        初始化config文件
        :return:
        '''

        confdict = dict()
        inifile = os.path.join(self.config_dir + 'config.ini')
        conf = configparser.ConfigParser()  # 生成conf对象
        conf.read(inifile, encoding='utf-8')

        # print(conf.sections())  # 显示所有节名称
        # print(conf.options('conf'))  # 显示节下面的option名称

        for sect in conf.sections():
            if sect == content:
                for opt in conf.options(sect):
                    confdict[opt] = conf.get(sect, opt)

        return confdict

    @staticmethod
    def getCurrentTime():
        format = "%Y-%m-%d %H:%M:%S"
        return datetime.now().strftime(format)

    @staticmethod
    def timeDiff(starttime, endtime):
        format = "%Y-%m-%d %H:%M:%S"
        return datetime.strptime(endtime, format) - datetime.strptime(starttime, format)
