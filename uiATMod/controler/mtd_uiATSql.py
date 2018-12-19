# -*- coding:utf-8 -*-

'''
@ auther: ZetaZhou
'''

import django

django.setup()

import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'AutoTestFrame.settings'

from django.db import connection, connections
from django.db.models import Q
from uiATMod.models import TestCase, TestCaseTMP, TestCaseDetail

cur = connection.cursor()


# def sql_creatTestcasetmp(caseinfo):
#     p = TestCaseTMP(**caseinfo)
#     p.save()
#
# def sql_creatTestcasetmp_many(caseinfo_list):
#     sql_tmp = 'insert into autoapp_testcasetmp VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
#     cur.executemany(sql_tmp, caseinfo_list)

def sql_creatTestCase(caseinfo):
    p = TestCase(**caseinfo)
    p.save()


def sql_creatTestCase_many(caseinfo_list):
    sql_tmp = 'insert into uiATMod_testcase (id, CASE_ID, CASE_NAME, MODEL_NAME, ADDR, ADDTIME, SIGN, STATUS)' \
              'VALUES (NULL, %s, %s, %s, %s, %s, %s, %s)'
    cur.executemany(sql_tmp, caseinfo_list)


def sql_bkp_Test_status():
    '''
    STATUS 0-未完成, 1-完成, 2-放弃
    :return:
    '''

    cur.execute("update uiATMod_testcase set STATUS = '2' where STATUS = '0'")


def sql_selectTestcase():
    '''
    STATUS 0-未完成, 1-完成, 2-放弃
    SIGN 0-不执行 1-执行
    :return:
    '''
    sql_tmp = "select CASE_ID, MODEL_NAME, CASE_NAME, ADDR" \
              " from uiATMod_testcase where SIGN ='1' AND STATUS ='0'"

    result = cur.execute(sql_tmp)
    result = [result for result in result.fetchall()]

    return result


def sql_creatTestcCaseDetail(caseinfo):
    caseid = caseinfo['CASE_ID']
    hwnd_case = TestCase.objects.get(CASE_ID=caseid, STATUS='0')
    hwnd_case.save()

    caseinfo['ID'] = hwnd_case
    hwnd_TD = TestCaseDetail(**caseinfo)
    hwnd_TD.save()
