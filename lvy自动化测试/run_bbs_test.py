
from HTMLTestRunner import HTMLTestRunner
import unittest
import time
# import sys
# #加载models目录
# sys.path.append("./bbs")
from bbs.test_case.models import function
if __name__=="__main__":
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename='./bbs/report/'+now+'result.html'
    with open(filename,'w',encoding='utf-8') as f:
        runner = HTMLTestRunner(stream=f,title='驴友网自动化测试报告',description='环境：windows7 浏览器：chrome')
        discover=unittest.defaultTestLoader.discover('./bbs/test_case',pattern='*_sta.py')
        runner.run(discover)
    file_path= function.new_file("./bbs/report/")
    function.send_email(file_path)