# -*- coding: utf-8 -*-
from selenium import webdriver
from operate.baseoperate import BaseOperate

import unittest

#主测试类继承自测试框架unittest
class MainCsae(unittest.TestCase):
    #声明一个webdriver
    driver = webdriver.Chrome()
    #声明一个基础操作类base_operate
    base_operate = BaseOperate

    def setUp(self):
        #测试准备，启动浏览器，打开一个网站
        # self.driver = webdriver.Chrome()
        self.driver.get("")
        #设置隐式等待时间
        self.driver.implicitly_wait(10)
        #设定页面加载限制时间
        self.driver.set_page_load_timeout(10)
        #设置异步脚本加载时间
        self.driver.set_script_timeout(10)
        #设置窗口最大化
        self.driver.maximize_window()
        #传入webdriver, 实例化这个类
        self.base_operate = BaseOperate(self.driver)

    def tearDown(self):
        #测试结束，关闭浏览器
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
