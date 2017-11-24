#coding=utf-8
import unittest
import time
import HTMLTestRunner
from sendemail import Email
class AllTest(object):
    def createsuite(self):  #创建套件
        list = ".\\test_case"
        suite=unittest.TestSuite()
        discover=unittest.defaultTestLoader.discover(list,pattern="*.py",top_level_dir=None)
        for test_suit in discover:
            for test_case in test_suit:
                suite.addTest(test_suit)
                print (suite)
        return suite

    def report(self):  #生成报告
        now = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
        filename = u"C:\\Users\\xxchen\\Desktop\\天蝎\\report\\" + now + "result.html"
        fp = open(filename, 'wb')
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"天蝎测试报告", description=u"执行用例情况")
        runner.run(self.createsuite())
        fp.close()
if  __name__=='__main__':
    alltest=AllTest()
    alltest.report()
    email=Email()
    email.sendreport()


