#coding=utf-8
import smtplib
import os,time,datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
class Email:
    def sendmail(self,file_new): #发送邮件
        smtpserver = "smtp.163.com"
        sender = 'm13661182987@163.com'
        receiver = 'm13661182987@163.com'
        f=open(file_new,'rb')
        content=f.read()
        f.close()

        msg=MIMEText(content,_subtype="html",_charset="utf-8")  #定义邮件正文
        msg['Subject']=u'天蝎测试报告' #定义邮件标题
        msg['date']=time.strftime('%a, %d %b %Y %H:%M:%S %z')  #定义发送的时间

        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login("m13661182987@163.com","gongbo123")
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()
        print 'email has send out !'

    def sendreport(self):  #处理报告
        result_dir=u"C:\\Users\\xxchen\\Desktop\\天蝎\\report"
        lists=os.listdir(result_dir)
        lists.sort(key=lambda fn: os.path.getmtime(result_dir+"\\"+fn) if not os.path.isdir(result_dir+"\\"+fn) else 0)
        print (u'最新的文件为： '+lists[-2])
        file_new = os.path.join(result_dir,lists[-2])
        self.sendmail(file_new)



