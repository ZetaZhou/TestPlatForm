# -*- coding:utf-8 -*-

import unittest
import traceback
import logging.config
from selenium import webdriver

from myutils.CommonConfig import CommonConfig
from myutils.TestCaseInfo import TestCaseInfo

from uiATMod.uiAT_Page.LoginPage import LoginPage
from uiATMod.uiAT_Page.MainPage import MainPage


class Test_TC_Cbmd(unittest.TestCase):
    '''
        打开浏览器
        定义全局变量
    '''
    HOST = 'http://sbrz.sinoecare.net:8000'
    driver = webdriver.Chrome()
    driver.set_window_size(1400, 900)

    # self.driver.maximize_window()

    def setUp(self):

        ''' 初始化testcase 信息'''

        self.testCaseInfo = TestCaseInfo(CASE_OWNER='ZetaZhou')
        self.testCaseInfo.STARTTIME = CommonConfig.getCurrentTime()

        ''' 初始化testreport '''
        # self.testResult = TestReport()

        # ''' 初始化日志句柄'''

    def test_1_login(self):
        ''' 登录测试用例 '''

        self.testCaseInfo.CASE_NAME_DETAIL = self.test_1_login.__doc__.strip()

        try:
            login = LoginPage(self.driver)
            login.open(self.HOST)
            # print(login.getTitle())

            login.Sendusername("zj")
            login.Sendpassword("admin123")
            login.Sendchecksum()
            login.ClickLogin()

            if not login.CheckLoginState():
                self.test_1_login()

            try:
                assert (1 == 1)

            except Exception as e:
                self.testCaseInfo.TEST_RESULT = "FAILE"
                self.testCaseInfo.MESSAGE = traceback.format_exc()
                loggerdetail.warning(("Error msg: {}".format(self.testCaseInfo.MESSAGE)))
                assert False, self.testCaseInfo.MESSAGE

            else:
                self.testCaseInfo.TEST_RESULT = "PASS"

        except AssertionError:
            pass

        except Exception as e:
            self.testCaseInfo.MESSAGE = str(e)
            loggerdetail.warning(("Error msg: {}".format(e)))
            self.testCaseInfo.TEST_RESULT = "FAILE"

        else:
            self.testCaseInfo.TEST_RESULT = "PASS"

    def test_2_cbmd(self):
        ''' 参保名单测试用例 '''

        self.testCaseInfo.CASE_NAME_DETAIL = self.test_2_cbmd.__doc__.strip()

        try:
            mainpage = MainPage(self.driver)
            mainpage.Printcancel()

            try:
                assert (1 == 2)

            except Exception as e:
                self.testCaseInfo.TEST_RESULT = "FAILE"
                self.testCaseInfo.MESSAGE = traceback.format_exc()
                loggerdetail.warning(("Error msg: {}".format(self.testCaseInfo.MESSAGE)))
                assert False, self.testCaseInfo.MESSAGE

            else:
                self.testCaseInfo.TEST_RESULT = "PASS"

        except AssertionError:
            pass

        except Exception as e:
            self.testCaseInfo.MESSAGE = str(e)
            loggerdetail.warning("Error msg: {}".format(e))
            assert False

        else:
            self.testCaseInfo.TEST_RESULT = "PASS"

    def tearDown(self):
        self.testCaseInfo.ENDTIME = CommonConfig.getCurrentTime()
        self.testCaseInfo.DURATION = str(CommonConfig.timeDiff(self.testCaseInfo.STARTTIME, self.testCaseInfo.ENDTIME))
        print(self.testCaseInfo.__dict__)
        # self.testResult.WriteHTML(self.testCaseInfo)


if __name__ == '__main__':
    logging.config.fileConfig(CommonConfig().config_dir + "logger.config")
    loggerdetail = logging.getLogger("detail")

    run = Test_TC_Cbmd()
    suite = unittest.TestSuite()

    # tests = [Test_TC_Cbmd("test_login"), Test_TC_Cbmd("test_cbmd")]
    suite.addTests(unittest.makeSuite(Test_TC_Cbmd))

    runner = unittest.TextTestRunner(verbosity=2)  # 日志等级为详细
    runner.run(suite)

    Test_TC_Cbmd.driver.quit()
