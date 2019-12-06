# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from config.sysconffig import *

class BaseOperate():
    #声明一个webdriver类
    operate_driver = webdriver.Chrome()

    def __init__(self, driver):
        #构造函数传入driver
        self.operate_driver = driver

    def find_element(self, *loc):
        """
        封装find方法，接受元祖类型的参数，默认等待元素5秒，寻找元素失败时自动截图
        :param loc:元祖类型，必须是（By.NAME, 'username'）这样的结构
        :return: 元素对象webelement
        """
        try:
            webelement = WebDriverWait(self.operate_driver, 5).until(lambda x: x.find_element(*loc))
            return webelement
        except (TimeoutException, NoSuchElementException) as e:
            #寻找失败时，自动截图并保存到指定目录sreenshot，截图名称为调用方法名（测试用例额名）+时间戳+png后缀
            self.operate_driver.get_screenshot_as_file(SCREENSHOTURL + sys._getframe(1).f_code.co_name + time.strftime(ISOTIMEFORMAT, time.localtime(time.time())) + ".png")

    def click_element(self, *loc):
        """
        封装click方法，将寻找和点击封装到一起，适用于点击次数不多的元素
        :param loc:元祖类型，必须是（By.NAME, 'username'）这样的结构
        :return: None
        """
        try:
            webelemnt = self.find_element(*loc)
            webelemnt.click()
        except (TimeoutException, NoSuchElementException) as e:
            print('Error details :%s' %(e.msg))


