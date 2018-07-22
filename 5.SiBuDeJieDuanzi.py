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

    def setUp(self):
        pass

    def testEle(self):
        my_selenium = Selenium("http://www.budejie.com/")
        driver = my_selenium.driver

        # 让webdriver操纵当前页
        driver.switch_to.default_content()
        while True:
            # 下拉滚动条，使浏览器加载出动态加载的内容，可能像这样要拉很多次，中间要适当的延时（跟网速也有关系）。
            driver.execute_script("window.scrollBy(0,40000)")
            time.sleep(3)

            elements = []
            elements += list(my_selenium.wait_until_exists('//div[@class="j-r-list-c-desc"]/a'))

            for e in elements:
                try:
                    text = e.text
                    if text not in text_list:
                        print(text)
                        text_list.append(e.text)
                        handle_text(text, 'SiBuDeJieDuanzi.txt')
                    else:
                        pass
                except Exception as e:
                    print(e)

            my_selenium.wait_until_exists('//a[@class="pagenxt" and text()="下一页"]')[0].click()

    def tearDown(self):
        print('down')

if __name__ == "__main__":
    unittest.main()
