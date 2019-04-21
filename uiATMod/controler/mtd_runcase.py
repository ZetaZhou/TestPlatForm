# -*- coding:utf-8 -*-
'''
auhor: ZetaZhou
'''

from myutils.CommonConfig import *

from uiATMod.controler.mtd_uiATSql import *


class Runloop(threading.Thread):
    def __init__(self, caselist, Que, TestResult):
        super().__init__()
        self.caselist = caselist
        self.Que = Que
        self.TestResult = TestResult

        self.__flag = threading.Event()  # 用于暂停线程的标识
        self.__flag.set()  # 设置为True
        self.__running = threading.Event()  # 用于停止线程的标识
        self.__running.set()  # 将running设置为True

    def run(self):
        for caseinfo in self.caselist:
            if not self.__running.isSet():
                break

            self.__flag.wait()  # 为True时立即返回, 为False时阻塞直到内部的标识位为True后返回

            case_addr = caseinfo[-1]

            stdout = subprocess.Popen("python " + case_addr, stdout=subprocess.PIPE)
            out, err = stdout.communicate()

            for line in out.splitlines():
                info = line.decode()
                if info.startswith('Error msg'):
                    print(info)
                try:
                    result = eval(info)
                    result['CASE_ID'] = caseinfo[0]
                    result['MODEL_NAME'] = caseinfo[1]
                    result['ADDR'] = caseinfo[3]
                    result['CASE_NAME_DETAIL'] = caseinfo[2] + ' ==> ' + result['CASE_NAME_DETAIL']
                    # print(result, type(result))
                    self.Que.put(result.copy())
                    self.TestResult.WriteHTML(result)
                    sql_creatTestcCaseDetail(result)

                except Exception as e:
                    # print('发生错误的文件：', e.__traceback__.tb_frame.f_globals['__file__'])
                    # print('错误所在的行号：', e.__traceback__.tb_lineno)
                    # print(traceback.format_exc())
                    print(e)

    def pause(self):
        self.__flag.clear()  # 设置为False, 让线程阻塞

    def resume(self):
        self.__flag.set()  # 设置为True, 让线程停止阻塞

    def stop(self):
        self.__flag.set()  # 将线程从暂停状态恢复, 如果已经暂停的话
        self.__running.clear()  # 设置为False


def runloop_ctrl_mtd(*para):
    # print('debug info : method = ', para[0])

    def run_start(caselist, Que, TestResult):
        runloop = Runloop(caselist, Que, TestResult)
        runloop.start()
        return runloop

    method_switch = dict()
    method_switch['0'] = run_start
    method_switch['1'] = lambda runloop: runloop.stop
    method_switch['2'] = lambda runloop: runloop.pause
    method_switch['3'] = lambda runloop: runloop.resume

    if para[0] == '0':
        runloop = method_switch[para[0]](para[1], para[2], para[3])
        return runloop

    elif para[0] in ['1', '2', '3']:
        method_switch[para[0]](para[1])()

    else:
        assert ValueError, 'Error msg : wrong method!'
