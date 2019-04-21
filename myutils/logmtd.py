# -*- coding:utf-8 -*-
'''
auhor: ZetaZhou
'''

'''
默认生成的root logger的level是logging.WARNING,低于该级别的就不输出了

级别排序:CRITICAL > ERROR > WARNING > INFO > DEBUG

debug : 打印全部的日志,详细的信息,通常只出现在诊断问题上

info : 打印info,warning,error,critical级别的日志,确认一切按预期运行

warning : 打印warning,error,critical级别的日志,一个迹象表明,一些意想不到的事情发生了,或表明一些问题在不久的将来(例如。磁盘空间低”),这个软件还能按预期工作

error : 打印error,critical级别的日志,更严重的问题,软件没能执行一些功能

critical : 打印critical级别,一个严重的错误,这表明程序本身可能无法继续运行
'''

import yaml
import logging.config
import os


def setup_logging(default_path=r".\config\config.yaml", default_level=logging.INFO, env_key="LOG_CFG"):
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, "r") as f:
            config = yaml.load(f)
            logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

# def func():
#     logging.info("start func")
#
#     logging.info("exec func")
#
#     logging.info("end func")
#
#     hwd = logging.getLogger('my_module')
#     hwd.info('test')

if __name__ == "__main__":
    setup_logging()
    # func()