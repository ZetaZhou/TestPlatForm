import logging
import os
import datetime

'''
默认生成的root logger的level是logging.WARNING,低于该级别的就不输出了

级别排序:CRITICAL > ERROR > WARNING > INFO > DEBUG

debug : 打印全部的日志,详细的信息,通常只出现在诊断问题上

info : 打印info,warning,error,critical级别的日志,确认一切按预期运行

warning : 打印warning,error,critical级别的日志,一个迹象表明,一些意想不到的事情发生了,或表明一些问题在不久的将来(例如。磁盘空间低”),这个软件还能按预期工作

error : 打印error,critical级别的日志,更严重的问题,软件没能执行一些功能

critical : 打印critical级别,一个严重的错误,这表明程序本身可能无法继续运行
'''
loggerAnalyze = logging.getLogger("analyze")
loggerDetail = logging.getLogger("detail")

def setAnalyzeLogging(filename=''):

    if not filename:
        day = datetime.datetime.now()
        time_index = '{0}-{1}-{2}'.format(day.year, day.month, day.day)
        # time_index = "%s-%s-%s" %(day.year, day.month, day.day)
        processdir = os.getcwd()
        # print (os.getcwd())
        path = os.path.join(processdir, "Log")
        if os.path.exists(path) == False:
            os.mkdir(path)
        else:
            pass

        filenamefinaly = path + '\\analyze_%s.log' %time_index

    else:
        day = datetime.datetime.now()
        time_index = '{0}-{1}-{2}'.format(day.year, day.month, day.day)
        # time_index = "%s-%s-%s" %(day.year, day.month, day.day)
        processdir = os.getcwd()
        # print (os.getcwd())
        path = os.path.join(processdir, "Log")
        if os.path.exists(path) == False:
            os.mkdir(path)
        else:
            pass

        filenamefinaly = path + '\\' + filename + '_%s.log' % time_index

    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s: %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename= filenamefinaly,
                        filemode='a')

    #################################################################################################
    #定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(lineno)s : %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('analyze').addHandler(console)
    #################################################################################################

def setDetailLogging(filename=''):

    if not filename:
        day = datetime.datetime.now()
        time_index = '{0}-{1}-{2}'.format(day.year, day.month, day.day)
        processdir = os.getcwd()
        path = os.path.join(processdir, "Log")
        if os.path.exists(path) == False:
            os.mkdir(path)
        else:
            pass

        filenamefinaly = path + '\\detail_%s.log' %time_index

    else:
        day = datetime.datetime.now()
        time_index = '{0}-{1}-{2}'.format(day.year, day.month, day.day)
        # time_index = "%s-%s-%s" %(day.year, day.month, day.day)
        processdir = os.getcwd()
        # print (os.getcwd())
        path = os.path.join(processdir, "Log")
        if os.path.exists(path) == False:
            os.mkdir(path)
        else:
            pass

        filenamefinaly = path + '\\' + filename + '_%s.log' % time_index

    logging.basicConfig(level=logging.WARNING,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename=filenamefinaly,
                        filemode='a')

    #################################################################################################
    #定义一个StreamHandler，将ERROR级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
    console = logging.StreamHandler()
    console.setLevel(logging.ERROR)
    formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(lineno)s : %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('detail').addHandler(console)
    #################################################################################################
