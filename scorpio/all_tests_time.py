#coding=utf-8
import time
from all_tests import AllTest
from sendemail import Email
'''控制什么时间执行脚本'''
while True:
    times=time.strftime("%H:%M",time.localtime(time.time()))
    if times == "14:19":
        print (u"开始跑脚本")
        alltest = AllTest()
        alltest.report()
        email = Email()
        email.sendreport()
        print(u"脚本结束")
        break
    else :
        time.sleep(5)
        print (times)

