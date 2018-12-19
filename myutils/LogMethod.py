import os
import re
from datetime import datetime

'''
默认生成的root logger的level是logging.WARNING,低于该级别的就不输出了

级别排序:CRITICAL > ERROR > WARNING > INFO > DEBUG

debug : 打印全部的日志,详细的信息,通常只出现在诊断问题上

info : 打印info,warning,error,critical级别的日志,确认一切按预期运行

warning : 打印warning,error,critical级别的日志,一个迹象表明,一些意想不到的事情发生了,或表明一些问题在不久的将来(例如。磁盘空间低”),这个软件还能按预期工作

error : 打印error,critical级别的日志,更严重的问题,软件没能执行一些功能

critical : 打印critical级别,一个严重的错误,这表明程序本身可能无法继续运行
'''


def initlogfile(url, filename, type):
    if type == 'main':
        pattern = r"args=(.*?)# main.log"
    elif type == 'detail':
        pattern = r"args=(.*?)# detail.log"
    else:
        return 'type error'

    day = datetime.now()
    time_index = '{0}-{1}-{2}'.format(day.year, day.month, day.day)
    processdir = os.getcwd()
    path = os.path.join(processdir, "Log")
    if os.path.exists(path) == False:
        os.mkdir(path)

    logname = path + '\\' + filename + '_%s.log' % time_index
    with open(url + 'logger.config', 'r') as f:
        content = f.read()
    # print (content)

    re_text = re.search(pattern, content)

    pattern_new = eval(re_text.group(1).strip(' '))[0]
    re_text_new = re.sub(repr(pattern_new), "'%s'" %logname, content)

    with open(url + 'logger.config', 'w') as f:
        f.write(re_text_new)


# initlogfile(11,'detail')
