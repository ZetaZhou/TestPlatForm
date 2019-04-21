from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponseNotFound
from django.http import StreamingHttpResponse

from uiATMod.controler.mtd_testcase import *
from uiATMod.controler.mtd_runcase import *

from myutils.TestReport import TestReport
from myutils.EmailUtils import send_report
from myutils.CommonConfig import CommonConfig

true = True
false = False

run_hwnd = None

CASE_INFO_LIST = list()  # 全局 testcase 初始化信息

TestResult = TestReport()  # 实例化测试报告
Que = queue.Queue()  # 测试用例执行情况队列


def uiAT_index(request):
    '''
    uiATMod 首页
    :param request:
    :return:
    '''
    CASE_INFO_LIST.clear()
    return render(request, 'uiATMod/index.html')


def uiAT_result(request):
    '''
    測試結果頁
    :param request:
    :return:
    '''

    return render(request, 'uiATMod/uiATResult.html')


def init_filetree(request):
    '''
    初始化树数据
   :param request:
    :return:
    '''

    inithandler = TestcaseMethod(0)

    data = dict()
    testcase_lsit = inithandler.create_testcaselist()
    data['treeinfo'] = testcase_lsit

    return JsonResponse(data)


def init_casetable(request):
    '''
    初始化测试用例列表
    :param request:
    :return:
    '''
    global CASE_INFO_LIST
    data = dict()

    if request.method == 'POST':
        caselist = request.POST['caselist']
        if caselist:
            caselist = caselist.split(',')
            caselist = list(filter(lambda x: False if x.endswith('_folder') else True, caselist))
            caselist = [[index, data, True, data.split('\\')[-2], os.path.basename(data)] for index, data in
                        enumerate(caselist, start=1)]

            CASE_INFO_LIST = caselist

        data['caselength'] = len(caselist)
        data['caselist'] = caselist[:10]

        return JsonResponse(data)


def page_func(request):
    '''
    翻页功能
    :param request:
    :return:
    '''

    data = dict()

    pagenum = int(request.GET['pagenum'])
    # print(pagenum)
    start_ind = (pagenum - 1) * 10
    end_ind = pagenum * 10

    if CASE_INFO_LIST:
        caselist = CASE_INFO_LIST[start_ind:end_ind]
        data['caselist'] = caselist
    else:
        data['caselist'] = []

    return JsonResponse(data)


def bkp_teststatus(request):
    '''
    确认本次测试用例后，将上次未完成 0测试用例状态改成放弃2
    :param request:
    :param sign:
    :return:
    '''
    data = dict()
    sign = request.GET['sign']

    if sign == 'true':
        sql_bkp_Test_status()  # 将status 未执行 0的用例改为废弃状态 2

        caseinfo_list = list()
        case_dict = dict()
        for caseinfo in CASE_INFO_LIST:
            case_dict['CASE_ID'] = caseinfo[0]
            case_dict['CASE_NAME'] = caseinfo[4]
            case_dict['MODEL_NAME'] = caseinfo[3]
            case_dict['ADDR'] = caseinfo[1]
            case_dict['ADDTIME'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            case_dict['SIGN'] = caseinfo[2]
            case_dict['STATUS'] = '0'
            caseinfo = [case_dict[key] for key in case_dict]
            caseinfo_list.append(caseinfo)

        sql_creatTestCase_many(caseinfo_list)  # 把数据写入 testcase 表

        data['result'] = True
        return JsonResponse(data)
    else:
        data['result'] = False
        return JsonResponse(data)


def runloop_ctrl(request):
    '''
    控制测试用例执行进程
    :param request:
    :return:
    '''

    data = dict()

    method = request.GET['method']
    # print('debug info :', method, run_hwnd)
    runloop_ctrl_mtd(method, run_hwnd)

    return JsonResponse(data)


def run_case(request):
    '''
    run_case, 初始化本次执行用例列表
    :param request:
    :return:
    '''

    data = dict()

    caselist = sql_selectTestcase()  # 查询本次待执行用例
    # CommonConfig().initLog()  # 初始化日志

    # def runloop():
    #
    #     for caseinfo in caselist:
    #         case_addr = caseinfo[-1]
    #
    #         stdout = subprocess.Popen("python " + case_addr, stdout=subprocess.PIPE, shell=True)
    #         out, err = stdout.communicate()
    #
    #         for line in out.splitlines():
    #             info = line.decode()
    #             if info.startswith('Error msg'):
    #                 print(info)
    #             try:
    #                 result = eval(info)
    #                 result['CASE_ID'] = caseinfo[0]
    #                 result['MODEL_NAME'] = caseinfo[1]
    #                 result['ADDR'] = caseinfo[3]
    #                 result['CASE_NAME_DETAIL'] = caseinfo[2] + ' ==> ' + result['CASE_NAME_DETAIL']
    #                 # print(result, type(result))
    #                 Que.put(result.copy())
    #                 TestResult.WriteHTML(result)
    #                 sql_creatTestcCaseDetail(result)
    #             except Exception as e:
    #                 # print('发生错误的文件：', e.__traceback__.tb_frame.f_globals['__file__'])
    #                 # print('错误所在的行号：', e.__traceback__.tb_lineno)
    #                 print(traceback.format_exc())

    method = request.GET['method']

    global run_hwnd

    run_hwnd = runloop_ctrl_mtd(method, caselist, Que, TestResult)
    # print('debug info :', run_hwnd)

    Que.queue.clear()

    return JsonResponse(data)


def info_loop(request):
    '''
    runcase页面定时刷新table功能
    :param request:
    :return:
    '''

    flag = request.GET['flag']
    data = dict()
    caseinfo_list = list()

    sql_selectCaseDetail(flag)

    # while sign:
    #
    #     if not Que.empty():
    #         caseinfo_list.append(Que.get())
    #     else:
    #         sign = False

    while True:
        if not Que.empty():
            caseinfo_list.append(Que.get())

        else:
            break

    # print(caseinfo_list)
    data['caseinfo_list'] = caseinfo_list
    return JsonResponse(data)


def result_download(request):
    '''
    下载测试报告
    :param request:
    :return:
    '''
    file_name = TestResult.reportfile

    # print(file_name)

    def file_iterator(file_name, chunk_size=512):
        with open(file_name) as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    the_file_name = file_name
    response = StreamingHttpResponse(file_iterator(the_file_name))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)
    return response


def send_resultmail(request):
    '''
    发送测试报告邮件
    :param request:
    :return:
    '''
    data = dict()
    try:
        send_report(TestResult.reportfile)
        data['result'] = 1
    except Exception as e:
        data['errmsg'] = str(e)
    return JsonResponse(data)
