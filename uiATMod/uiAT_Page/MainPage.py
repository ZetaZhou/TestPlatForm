#-*- coding:utf-8 -*-
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from uiATMod.uiAT_Page.BasePage import BasePage


class MainPage(BasePage):

    # printcancel = ['CSS', 'span.l-btn-text:nth-child(2)']
    printcancel = (By.CSS_SELECTOR, '.messager-button>a:nth-child(2)')
    cbmd_button = (By.LINK_TEXT, '角色管理')

    def Printcancel(self):

        time.sleep(2)

        try:
            self.wait.until(EC.presence_of_element_located(self.printcancel))
        except:
            print (">>>TestInfo : printctrl wait error!")
        else:
            printcancel = self.findElement(self.printcancel)
            self.actions.click(printcancel)
            self.actions.perform()

