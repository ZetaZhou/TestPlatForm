#-*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class BasePage(object):
    """description of class"""

    # webdriver instance
    def __init__(self, browser , sec = 3 ):
        '''
        initialize selenium webdriver, use chrome as default webdriver
        '''

        self.driver     = browser                                        # 窗口句柄
        self.wait       = WebDriverWait(browser, sec)                           # 等待时间
        self.actions    = ActionChains(browser)                              # 鼠标句柄

    def findElement(self, element):
        '''
        Find element

        element is a set with format (identifier type, value), e.g. ('id','username')

        Usage:
        self.findElement(element)
        '''

        try:
            type = element[0]
            value = element[1]

            if type == "id":
                elem = self.driver.find_element_by_id(value)

            elif type == "name" or type == "NAME" or type == "Name":
                elem = self.driver.find_element_by_name(value)

            elif type == "class" or type == "CLASS" or type == "Class":
                elem = self.driver.find_element_by_class_name(value)

            elif type == "link_text" or type == "LINK_TEXT" or type == "Link_text":
                elem = self.driver.find_element_by_link_text(value)

            elif type == "xpath" or type == "XPATH" or type == "Xpath":
                elem = self.driver.find_element_by_xpath(value)

            elif type == "css" or type == "CSS" or type == "css selector":
                elem = self.driver.find_element_by_css_selector(value)
            else:
                raise NameError("Please correct the type in function parameter")

        except Exception:
            raise ValueError("No such element found" + str(element))
        return elem

    def findElements(self, element):
        '''
        Find elements

        element is a set with format (identifier type, value), e.g. ('id','username')

        Usage:
        self.findElements(element)
        '''
        try:
            type = element[0]
            value = element[1]
            if type == "id" or type == "ID" or type == "Id":
                elem = self.driver.find_elements_by_id(value)

            elif type == "name" or type == "NAME" or type == "Name":
                elem = self.driver.find_elements_by_name(value)

            elif type == "class" or type == "CLASS" or type == "Class":
                elem = self.driver.find_elements_by_class_name(value)

            elif type == "link_text" or type == "LINK_TEXT" or type == "Link_text":
                elem = self.driver.find_elements_by_link_text(value)

            elif type == "xpath" or type == "XPATH" or type == "Xpath":
                elem = self.driver.find_elements_by_xpath(value)

            elif type == "css" or type == "CSS" or type == "css selector":
                elem = self.driver.find_elements_by_css_selector(value)
            else:
                raise NameError("Please correct the type in function parameter")
        except Exception:
            raise ValueError("No such element found" + str(element))
        return elem

    def open(self, url):
        '''
        Open web url

        Usage:
        self.open(url)
        '''
        if url != "":
            self.driver.get(url)
        else:
            raise ValueError("please provide a base url")

    def type(self, element, text):
        '''
        Operation input box.

        Usage:
        self.type(element,text)
        '''
        element.send_keys(text)

    def enter(self, element):
        '''
        Keyboard: hit return

        Usage:
        self.enter(element)
        '''
        element.send_keys(Keys.RETURN)

    def click(self, element):
        '''
        Click page element, like button, image, link, etc.
        '''
        element.click()

    def quit(self):
        '''
        Quit webdriver
        '''
        self.driver.quit()

    def getAttribute(self, element, attribute):
        '''
        Get element attribute

        '''
        return element.get_attribute(attribute)

    def getText(self, element):
        '''
        Get text of a web element

        '''
        return element.text

    def getTitle(self):
        '''
        Get window title
        '''
        return self.driver.title

    def getCurrentUrl(self):
        '''
        Get current url
        '''
        return self.driver.current_url

    def getScreenshot(self, targetpath):
        '''
        Get current screenshot and save it to target path
        '''
        self.driver.get_screenshot_as_file(targetpath)

    def maximizeWindow(self):
        '''
        Maximize current browser window
        '''
        self.driver.maximize_window()

    def back(self):
        '''
        Goes one step backward in the browser history.
        '''
        self.driver.back()

    def forward(self):
        """
        Goes one step forward in the browser history.
        """
        self.driver.forward()

    def getWindowSize(self):
        """
        Gets the width and height of the current window.
        """
        return self.driver.get_window_size()

    def refresh(self):
        '''
        Refresh current page
        '''
        self.driver.refresh()
        self.driver.switch_to()


