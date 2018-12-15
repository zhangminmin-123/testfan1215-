

#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import unittest
import HTMLTestRunner



class Baidu(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.baidu.com/"
        # self.verificationErrors = []
        # self.accept_next_alert = True

    # 百度搜索用例
    def test_baidu_search(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").send_keys("selenium")
        driver.find_element_by_id("su").click()
        time.sleep(2)


    # 百度设置用例
    def test_baidu_set(self):
        dr=self.driver
        dr.get(self.base_url)
        hover = dr.find_element_by_link_text("设置")
        ActionChains(dr).move_to_element(hover).perform()  ##鼠标悬停
        dr.find_element_by_link_text("搜索设置").click()
        time.sleep(2)

        dr.find_element_by_id("SL_1").click()
        dr.find_element_by_xpath("//select[@id='nr']/option[@value='50']").click()
        dr.find_element_by_xpath("//select[@id='issw1']/option[@value='2']").click()
        time.sleep(4)

        dr.find_element_by_link_text('保存设置').click()
        time.sleep(3)
        dr.switch_to.alert.accept()
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    # unittest.main()
    testunit=unittest.TestSuite()
    testunit.addTest(Baidu("test_baidu_search"))
    testunit.addTest(Baidu("test_baidu_set"))
    filename="BaiduResult.html"
    fp=open(filename,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title='百度测试报告',
    description='用例执行情况：')
    runner.run(testunit)