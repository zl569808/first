from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.utils import parseaddr, formataddr
import smtplib
import unittest
import time, os, sys
#截图
def insert_img(driver,filename):
    #拼接报告截图路径
    path=os.path.dirname(__file__)
    img_path=str(path).replace('\\','/').replace('test_case','report').replace('models','images')
    img_path=img_path+'/'+filename
    #截图
    driver.get_screenshot_as_file(img_path)
'''邮件发送'''
#设计一个函数_format_addr()来格式化一个邮件地址，注意不能简单地传入name <addr@example.com>，因为如果包含中文，需要通过Header对象进行编码。
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))
#取的最新报告
def new_file(test_dir):
    #列举test_dir目录下的所有文件，结果以列表形式返回。
    lists=os.listdir(test_dir)
    #sort按key的关键字进行排序，lambda的入参fn为lists列表的元素，获取文件的最后修改时间
    #最后对lists元素，按文件修改时间大小从小到大排序。
    lists.sort(key=lambda fn:os.path.getmtime(test_dir+'\\'+fn))
    #获取最新文件的绝对路径
    file_path=os.path.join(test_dir,lists[-1])
    return file_path
#发送邮件
def send_email(newfile):
    # 输入SMTP服务器地址:
    smtp_server = 'smtp.126.com'
    # 输入Email地址和口令:
    from_addr = 'zhanglei290035@126.com'
    password = 'zhanglei123'
    # 输入收件人地址:
    to_addr = '1057014556@qq.com'
    with open(newfile,"rb") as f:
        mail_body=f.read()
    #定义邮件格式
    msg= MIMEText (mail_body,'html','utf-8')
    msg['From'] = Header('测试人员<%s>'% from_addr, 'utf-8')
    #msg['To'] = to_addr
    msg['To'] = _format_addr('接收者 <%s>' % to_addr)
    msg['Subject']=Header('测试报告','utf-8')

    smtp=smtplib.SMTP(smtp_server,25)
    smtp.set_debuglevel(1)
    smtp.helo(smtp_server)
    smtp.ehlo(smtp_server)
    smtp.login(from_addr,password)

    smtp.sendmail(from_addr,to_addr,msg.as_string())
    smtp.quit()
    print('邮件已发送！')