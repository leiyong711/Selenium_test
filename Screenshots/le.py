# !/usr/bin/env python
# -*- coding:utf-8 -*-
# project name: untitled
# created by leiyong at @time: 2017/5/12 0012 14:51
# Email:leiyong711@163.com
# !/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Lei yong"
# Email:leiyong711@163.com

import time
from PIL import Image

from selenium import webdriver

from Screenshots.dfsy import verification_code


class ass(object):

    def __init__(self):
        self.driver = webdriver.Firefox()

    def dk(self,ult):
        return self.driver.get(ult)

    def max(self):
        return self.driver.maximize_window()  # 浏览器最大化

    def link_text(self,text):
        return self.driver.find_element_by_link_text(text)

    def id(self,id):
        element = self.driver.find_element_by_id(id)
        return element

    def name(self,name):
        return self.driver.find_element_by_name(name)

    def screenshots(self,id):
        self.driver.get_screenshot_as_file("..\\_img\\1.jpg")
        element = self.driver.find_element_by_id(id)
        left = int(element.location['x'])
        top = int(element.location['y'])
        right = int(element.location['x'] + element.size['width'])
        bottom = int(element.location['y'] + element.size['height'])
        # print left,top,right,bottom
        im = Image.open("..\\_img\\1.jpg")
        im = im.crop((left,top,right,bottom))
        im.save('..\\img\\1.jpg')
        return self.lei()

    def lei(self):
        sd = verification_code()
        while 1:
            # print sd
            try:
                return sd['Result']
                break
            except:
                s = sd['Error_Code']
                b = sd['Error']
                print s, b
                print '3s后重新比对验证码'
                time.sleep(3)


