#coding=utf-8
import unittest
from selenium import webdriver
import time
class Channel(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Ie()
        self.driver.get("https://192.168.4.163/")
        time.sleep(30)
        self.channelsum2 = []
    def test_channelnum(self):
        u'''检查监控频道all个数'''
        channelsum3 = 0
        self.driver.get("https://192.168.4.163/monitor/channelAction!index")
        channelsum=self.driver.find_element_by_xpath("//div[@class='pad-lr pull-left full-width sl']/span[@class='pull-right']/a").text
        channelsum=int(channelsum.encode("utf-8"))
        channellist = self.driver.find_elements_by_xpath('//div[@id="mCSB_5_container"]/li/div/span[@class="text-center number pull-right round absolute js-num"]')
        for channelnum in channellist:
            cnumber=int(channelnum.text.encode("utf-8"))
            self.channelsum2.append(cnumber)
            channelsum3=channelsum3+cnumber
        print (self.channelsum2)
        if channelsum==channelsum3:
            print("ALL(数量)与频道数总和相等")
        else:
            print("ALL(数量)与频道数总和不相等")
        print ("频道监控页频道数相加总和为:%d" % channelsum3)
        print ("-----------------------------------")
    def tearDown(self):
        self.driver.quit()
if  __name__=='__main__':
    suite=unittest.TestSuite()
    suite.addTest(Channel('test_channelnum'))
    runner=unittest.TextTestRunner()
    runner.run(suite)