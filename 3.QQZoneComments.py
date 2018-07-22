#coding:utf-8

import unittest
import time
from bs4 import BeautifulSoup

from auto_everything.web import Selenium

def handle_text(text, file_name):
    with open(file_name, 'a') as f:
        text = text.strip('\n ')
        text += """

——————————————

"""
        f.write(text)

text_list = []

class seleniumTest(unittest.TestCase):
    user = ''  # 你的QQ号
    pw = ''  # 你的QQ密码

    def setUp(self):
        pass

    def testEle(self):
        my_selenium = Selenium("https://h5.qzone.qq.com/mqzone/index")
        driver = my_selenium.driver

        # 账号输入框输入已知qq账号
        driver.find_element_by_id("u").send_keys(self.user)
        # 密码框输入已知密码
        driver.find_element_by_id("p").send_keys(self.pw)
        # 自动点击登陆按钮
        driver.find_element_by_id("go").click()

        # 如果登录比较频繁或者服务器繁忙的时候，一次模拟点击可能失败，所以想到可以尝试多次，
        # 但是像QQ空间这种比较知名的社区在多次登录后都会出现验证码，验证码自动处理又是一个
        # 大问题，本例不赘述。本例采用手动确认的方式。即如果观察到自动登陆失败，手动登录后
        # 再执行下列操作。
        r = ''
        while r != 'y':
            print("Login seccessful?[y]")
            r = input()

        # 让webdriver操纵当前页
        driver.switch_to.default_content()
        while True:
            # 下拉滚动条，使浏览器加载出动态加载的内容，可能像这样要拉很多次，中间要适当的延时（跟网速也有关系）。

            elements = []
            elements += list(driver.find_elements_by_xpath('//*[@class="reply-txt"]'))
            elements += list(driver.find_elements_by_xpath('//*[@class="comment-text"]'))

            for e in elements:
                text = e.text
                if text not in text_list:
                    print(text)
                    text_list.append(e.text)
                    handle_text(text, 'QQZoneComments.txt')
                else:
                    pass

            element = my_selenium.wait_until_exists('//*[@class="btn js_morebtn"]') 
            driver.execute_script("arguments[0].click();", element)

            my_selenium.wait_until_exists('//*[@class="comment-text"]')
            time.sleep(1)

    def tearDown(self):
        print('down')

if __name__ == "__main__":
    unittest.main()
