#coding=utf-8
from selenium import webdriver
import unittest
import pymssql
import time
class Home(unittest.TestCase):
    def setUp(self):
        self.host = '192.168.2.9'
        self.user = 'fb_new'
        self.password = 'Aa123456'
        self.database = 'scorpio_system'
        self.charset = 'utf8'

        self.driver = webdriver.Ie()
        self.driver.get("https://192.168.4.163/")
        time.sleep(30)
    def test_homepagechannel(self):
        u'''检查首页监控频道个数'''
        self.driver.get("https://192.168.4.163/system/userAction!index")
        homechannel = int(self.driver.find_element_by_xpath('//div[@id="mCSB_4_container"]//a[@class="channelCount"]//span[@class="redFont channel-count"]').text.encode("utf-8"))
        conn = pymssql.connect(host=self.host, user=self.user, password=self.password, database=self.database,charset=self.charset)
        cur=conn.cursor()
        cur.execute("SELECT count(*) FROM fb_business.dbo.channel_info WHERE project_id in (SELECT DISTINCT project_id FROM scorpio_system.dbo.project_user WHERE user_id=3267 and is_delete=0) AND deleted=0 AND parent_channel_id is NOT NULL AND user_id=3267")
        sqlchannelnum=cur.fetchone()[0]
        print ("首页：%d"%homechannel)
        print ("数据库查询个数为：%d"%sqlchannelnum)
        if homechannel==sqlchannelnum:
            print ("首页显示的监控频道个数正确")
        else:
            print ("首页显示的监控频道个数不正确")
        cur.close()
        conn.close()
        print ("-----------------------------------")
    def test_homepagepeople(self):
        u'''检查首页监控人数'''
        self.driver.get("https://192.168.4.163/system/userAction!index")
        homepeople = int(self.driver.find_element_by_xpath('//div[@id="mCSB_4_container"]//a[@class="monitorCount"]//span[@class="redFont monitor-count"]').text.encode("utf-8"))
        conn = pymssql.connect(host=self.host, user=self.user, password=self.password, database=self.database,charset=self.charset)
        cur = conn.cursor()
        cur.execute("SELECT count(*) FROM fb_business.dbo.channel_monitor WHERE user_id=3267 and deleted=0 and channel_id IN( SELECT channel_id FROM fb_business.dbo.channel_info WHERE project_id in (SELECT DISTINCT project_id FROM scorpio_system.dbo.project_user WHERE user_id=3267 and is_delete=0) AND deleted=0)")
        sqlpeoplenum = cur.fetchone()[0]
        print ("首页：%d" % homepeople)
        print ("数据库查询人数为：%d" % sqlpeoplenum)
        if homepeople == sqlpeoplenum:
            print ("首页显示的监控人数正确")
        else:
            print ("首页显示的监控人数不正确")
        cur.close()
        conn.close()
        print ("-----------------------------------")
    def test_homepagedeeper(self):
        u'''检查首页深度分析个数'''
        self.driver.get("https://192.168.4.163/system/userAction!index")
        homedeeper = int(self.driver.find_element_by_xpath('//div[@id="mCSB_4_container"]//a[@class="analysisCount"]//span[@class="redFont analysis-count"]').text.encode("utf-8"))
        self.driver.get("https://192.168.4.163/analysis/analysisJobAction!index?status=2")
        deepernum = int(self.driver.find_element_by_xpath('//div[@class="task-title"]/span[@class="badge yellow js-tasknum"]').text.encode("utf-8"))
        print ("首页：%d"%homedeeper)
        print ("深度分析：%d"%deepernum)
        if homedeeper==deepernum:
            print ("首页深度分析数量与任务原理页显示一致")
        else:
            print ("首页深度分析数量与任务原理页显示不一致" )
        print ("-----------------------------------")
    def test_homepagealarm(self):
        #暂时不能测
        u'''检查首页告警个数'''
        alarmsum=0
        self.driver.get("https://192.168.4.163/system/userAction!index")
        homealarm=int(self.driver.find_element_by_xpath('//div[@id="mCSB_4_container"]//a[@class="alarmCount"]//span[@class="redFont alarm-count"]').text.encode("utf-8"))
        self.driver.get("https://192.168.4.163/system/messageAction!toMeassageCenter")
        alarmlist = self.driver.find_elements_by_xpath('//div[@id="mCSB_4_container"]/li/span[class="pull-right news-information round"]')
        for alarmnum in alarmlist:
            alarmsum=alarmsum+int(str(alarmnum.text.encode("utf-8")).split('/')[1])
        print ("首页：%d"%homealarm)
        print ("告警页：%d"%alarmsum)
        if homealarm==alarmsum:
            print ("首页告警数量与告警页显示一致")
        else:
            print ("首页告警数量与告警页显示不一致" )
        print ("-----------------------------------")
    def test_homepagework(self):
        #工作区素材，没有解决
        u'''检查首页工作区数量'''
        self.driver.get("https://192.168.4.163/system/userAction!index")
        homework=int(self.driver.find_element_by_xpath('//li[@class="pull-left itemIcon"]/span').text.encode("utf-8"))
    def test_homepagetheme(self):
        u'''检查首页协作数量'''
        self.driver.get("https://192.168.4.163/system/userAction!index")
        hometheme=int(self.driver.find_element_by_xpath('//li[@class="pull-left coopIcon"]/span').text.encode("utf-8"))
        self.driver.get("https://192.168.4.163/workspace/workShareAction!index")
        themenum=len(self.driver.find_elements_by_xpath('//div[@id="mCSB_4_container"]/ul[@class="cols-ul js-share-cols-ul"]/li[@class="clearfix white coop transition"]'))
        print ("首页：%d"%hometheme)
        print ("工作区：%d"%themenum)
        if hometheme==themenum:
            print ("首页协作数量与协作页显示一致")
        else:
            print ("首页协作数量与协作页显示不一致")
        print ("-----------------------------------")
    def test_homepagetask(self):
        u'''检查首页任务数量'''
        self.driver.get("https://192.168.4.163/system/userAction!index")
        hometask = int(self.driver.find_element_by_xpath('//li[@class="pull-left printIcon"]/span').text.encode("utf-8"))
        self.driver.get("https://192.168.4.163/workspace/workTaskAction!index")
        tasknum = len(self.driver.find_elements_by_xpath('//div[@id="mCSB_4_container"]/ul[@class="cols-ul"]/li[@class="clearfix white finsh transition"]'))
        print ("首页：%d" % hometask)
        print ("工作区-任务：%d" % tasknum)
        if hometask == tasknum:
            print ("首页任务数量与工作区-任务页显示一致")
        else:
            print ("首页任务数量与工作区-任务页显示不一致")
        print ("-----------------------------------")
    def tearDown(self):
        self.driver.quit()
if __name__=='__main__':
    suite=unittest.TestSuite()
    suite.addTest(Home('test_homepagechannel'))
    suite.addTest(Home('test_homepagepeople'))
    suite.addTest(Home('test_homepagedeeper'))
    suite.addTest(Home('test_homepagealarm'))
    suite.addTest(Home('test_homepagework'))
    suite.addTest(Home('test_homepagetheme'))
    suite.addTest(Home('test_homepagetask'))
    runner=unittest.TextTestRunner()
    runner.run(suite)