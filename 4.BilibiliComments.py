#coding:utf-8

import unittest
import time
from selenium import webdriver
from bs4 import BeautifulSoup

from auto_everything.web import Selenium

def handle_text(text, file_name):
    with open(file_name, 'a') as f:
        text += """

——————————————

"""
        f.write(text)


'''
urls = """
https://www.bilibili.com/video/av1415480
https://www.bilibili.com/video/av25255526
"""
urls = [url.strip(' \n') for url in urls.split('\n') if url.strip(' \n') != ""]
'''

top_url = "https://www.bilibili.com/ranking/all/155/0/3"
my_selenium = Selenium(top_url)
driver = my_selenium.driver

elements = my_selenium.wait_until_exists('//a[@class="title" and @target="_blank"]')
urls = [e.get_attribute("href") for e in elements]
driver.close()

text_list = []


class seleniumTest(unittest.TestCase):

    def setUp(self):
        pass

    def testEle(self):
        global text_list, urls
        for url in urls:
            my_selenium = Selenium(url)
            driver = my_selenium.driver
            driver.switch_to.default_content()

            while len(text_list) <= 100:
                # 下拉滚动条，使浏览器加载出动态加载的内容，可能像这样要拉很多次，中间要适当的延时（跟网速也有关系）。
                driver.execute_script("window.scrollBy(0,40000)")
                time.sleep(1)

                elements = my_selenium.wait_until_exists('//div[@class="comment-list"]//p[@class="text"]')
                for e in elements:
                    try:
                        text = e.text
                        if text not in text_list:
                            print(text)
                            handle_text(text, 'BilibiliComments.txt')
                            text_list.append(text)
                        else:
                            pass
                    except Exception as e:
                        print(e)

                elements = my_selenium.wait_until_exists('//a[@class="next"]') # and @href="javascript:;"]')
                driver.execute_script("arguments[0].click();", elements[0])

            text_list = []
            driver.close()

    def tearDown(self):
        print('down')

if __name__ == "__main__":
    unittest.main()
