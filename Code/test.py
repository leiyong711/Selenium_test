# !/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Lei yong"
# Email:leiyong711@163.com
import time

from Screenshots.le import ass
d = ass()

# d.dk("http://www.taobao.com")
# d.max()
# d.link_text('亲，请登录').click()
# d.link_text('密码登录').click()
# d.id('TPL_username_1').send_keys('18216060753')
# d.id('TPL_password_1').send_keys('QQ20071314520')
# d.id('J_SubmitStatic').click()

# d.dk('http://127.0.0.1:9945/BBS/bbs/member.php?mod=logging&action=login')
# # d.max()
# d.name('username').send_keys('admin')
# d.name('password').send_keys('leiyong')
# a = d.screenshots('vseccode_cSC61QJa')
# print '----%s----'%a
# d.name('seccodeverify').send_keys(a)
import unittest


class a(unittest.TestCase):
    def test_01(self):
        d.dk('https://www.baidu.com')
        d.link_text('登录').click()
        d.id('TANGRAM__PSP_8__userName').send_keys('18216060753')
        d.name('password').send_keys('lei520')
        a = d.screenshots('TANGRAM__PSP_8__verifyCodeImgParent')
        print '若快返回验证码：',a
        d.name('verifyCode').send_keys(a)
        d.id('TANGRAM__PSP_8__submit').click()


# driver.get("http://www.taobao.com")
# # driver.set_window_size(480,800)
# driver.maximize_window()  # 浏览器最大化
# driver.find_element_by_link_text('亲，请登录').click()
# print 124
# driver.find_element_by_link_text('密码登录').click()
# driver.find_element_by_id('TPL_username_1').send_keys('18216060753')
# driver.find_element_by_id('TPL_password_1').send_keys('QQ20071314520')

# time.sleep(1)
# driver.find_element_by_id('J_SubmitStatic').click()
# driver.find_element_by_class_name("s_ipt").send_keys(u"唐润芳")
# driver.find_element_by_id("su").click()
# driver.quit()
# driver.find_element_by_link_text('会员名/邮箱/手机号').send_keys(1)
# driver.find_element_by_class_name("bg s_btn")u

