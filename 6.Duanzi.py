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

urls = ["http://www.haoduanzi.com/category-1_{num}.html".format(num=str(num)) for num in range(1, 1050)]
text_list = []

class seleniumTest(unittest.TestCase):

    def setUp(self):
        pass

    def testEle(self):
        global urls, text_list
        for url in urls:
            my_selenium = Selenium(url)
            driver = my_selenium.driver

            # 让webdriver操纵当前页
            driver.switch_to.default_content()
            # 下拉滚动条，使浏览器加载出动态加载的内容，可能像这样要拉很多次，中间要适当的延时（跟网速也有关系）。
            driver.execute_script("window.scrollBy(0,40000)")
            time.sleep(1)

            elements = []
            elements += list(my_selenium.wait_until_exists('//div[contains(@id, "log")]/h3[@class="title"]/a'))

            for e in elements:
                try:
                    url = e.get_attribute("href")
                    my_selenium2 = Selenium(url)
                    driver2 = my_selenium2.driver

                    elements2 = list(my_selenium2.wait_until_exists('//div[@class="cont"]/p'))
                    for e2 in elements2:
                        try:
                            text = e2.text
                            if text not in text_list:
                                print(text)
                                text_list.append(e.text)
                                handle_text(text, 'DuanZi.txt')
                            else:
                                pass
                        except Exception as e:
                            print(e)
                except Exception as e:
                    print(e)
                driver2.close()

            driver.close()

    def tearDown(self):
        print('down')

if __name__ == "__main__":
    unittest.main()
