# -*- coding:utf-8 -*-
'''
auhor: ZetaZhou
'''

from myutils.CommonConfig import *

class TestcaseMethod(CommonConfig):
    '''
    初始化测试用例
    '''
    # def __new__(cls, *args, **kwargs):
    #     if not hasattr(TestcaseMethod, "_instance"):
    #         TestcaseMethod._instance = object.__new__(cls)
    #     return TestcaseMethod._instance

    def __init__(self, index):
        super().__init__()
        # self.initconfig('conf')
        self.testcase_dir = self.testcase_dirlist[index]

    def create_testcaselist(self):
        '''
        testcase生成器
        从testcase列表文件中, 读取testcase名字并返回
        :return:
        '''

        root = {
            "id": "0",
            "text": self.testcase_dir,
            "value": "root_folder",
            "showcheck": True,
            'complete': True,
            "isexpand": True,
            "checkstate": 0,
            "hasChildren": True,
        }
        temp_folder = list()
        for addr in os.listdir(self.testcase_dir):
            if '.' not in addr:
                folder = {
                    "id": addr,
                    "text": addr,
                    "value": addr + '_folder',
                    "showcheck": True,
                    'complete': True,
                    "isexpand": False,
                    "checkstate": 0,
                    "hasChildren": True
                }
                temp_case = list()
                path = os.path.join(self.testcase_dir, addr)
                for file in os.listdir(path):
                    if file.endswith('.py'):
                        case = {
                            "id": os.path.join(path, file) + file,
                            "text": file,
                            "value": os.path.join(path, file),
                            "showcheck": True,
                            'complete': True,
                            "isexpand": False,
                            "checkstate": 0,
                            "hasChildren": False
                        }
                        temp_case.append(case.copy())
                folder['ChildNodes'] = temp_case
                temp_folder.append(folder.copy())

        root["ChildNodes"] = temp_folder
        return [root]


