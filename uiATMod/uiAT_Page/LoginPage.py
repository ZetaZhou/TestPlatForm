#-*- coding:utf-8 -*-
import time

from PIL import Image
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from uiATMod.uiAT_Page.BasePage import BasePage
from myutils.CheckSumModule import CheckSum


class LoginPage(BasePage):

    ''' 定义全局elements'''
    username = (By.ID, 'username')
    password = (By.ID, 'password')
    checkimg = (By.ID, 'checkImg')
    checksum = (By.ID, 'yzm')
    okbutton = (By.ID, 'login')
    yzminfo  = (By.ID, 'errorlog')

    def Sendusername(self, name):
        ''' 输入帐号 '''
        username = self.findElement(self.username)
        username.clear()
        username.send_keys(name)
        time.sleep(1)

    def Sendpassword(self, pwd):
        ''' 输入密码 '''
        password = self.findElement(self.password)
        password.clear()
        password.send_keys(pwd)
        time.sleep(1)

    def Sendchecksum(self):
        ''' 屏幕截图 '''
        self.driver.get_screenshot_as_file('.\\image\\screenshot.png')

        ''' 获取指定元素 验证码标签的 位置 '''
        element = self.findElement(self.checkimg)
        left = int(element.location['x'])*1.24
        top = int(element.location['y'])*1.24
        right = int(element.location['x'] + element.size['width'])*1.24
        bottom = int(element.location['y'] + element.size['height'])*1.24

        ''' 通过Image处理剪切图像 '''
        im = Image.open('.\\image\\screenshot.png')
        im = im.crop((left, top, right, bottom))
        im.save('.\\image\\code.png')
        checksum_pic = '.\\image\\code.png'

        checksum = CheckSum(checksum_pic)   # 通过pytesser处理验证码图片

        yzm = self.findElement(self.checksum)
        yzm.send_keys(checksum)
        time.sleep(1)

    def ClickLogin(self):
        ''' 点登录按钮 '''
        okbtn = self.findElement(self.okbutton)
        okbtn.send_keys(Keys.ENTER)
        time.sleep(1)

    def CheckLoginState(self):
        time.sleep(2)

        try:
            self.wait.until(EC.presence_of_element_located((By.ID, "errorlog")))
        except:
            return True
        else:
            yzminfo = self.findElement(self.yzminfo)
            yzminfo = yzminfo.text
            print(">>>Yzminfo : ", yzminfo)
            return False
