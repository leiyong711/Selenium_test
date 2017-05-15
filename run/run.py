# !/usr/bin/env python
# -*- coding:utf-8 -*-
# project name: seleniumtest
# created by leiyong at @time: 2017/5/13 0013 16:50
# Email:leiyong711@163.com
import HTMLTestRunner
import time
import logging
from Screenshots.folder_Path import *
from Code.test import *

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


Create_folder('..\\The_report\\', '\\log')
timestr = time.strftime('%Y-%m-%d-%H', time.localtime(time.time()))
b = '..\\The_report\\' + timestr[:10] + '\\' + timestr[11:] + '\\log\\'
logpath=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"log")
logging.basicConfig(
                    level=logging.NOTSET,
                    # level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s  %(pathname)s %(lineno)d %(funcName)s',
                    datefmt='%y-%m-%d %H:%M',
                    filename=os.path.join(logpath, b+'log.txt'),
                    filemode='a')



if __name__ == '__main__':
    suite = unittest.TestSuite()
    logging.error("出错啦")
    logging.warning("警告")
    logging.info("运行")
    logging.debug("调试")
    suite.addTest(a('test_01'))
    timestr = time.strftime('%Y-%m-%d-%H', time.localtime(time.time()))
    Create_folder('..\\The_report\\', '\\Case_report')  # 判断文件夹是否存在，不存在则创建
    filename = '..\\The_report\\'+ timestr[:10]+ '\\' + timestr[11:] + '\\Case_report\\' + 'Case_report.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title='Selenium自动化测试结果',
    description='测试报告'
    )
    runner.run(suite)
    fp.close()                       # 测试报告关闭

