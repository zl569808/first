import sys
#加载models目录
# sys.path.append("./models")
# #加载page_obj目录
# sys.path.append("./page_obj")
from models import myunit,function
from page_obj.loginPage import login
import random,time,unittest
class loginTest(myunit.myTest):
    #测试用户登录流程
    def user_login_verify(self,username='',passwd=''):
        login(self.driver).user_login(username,passwd)

    #账号密码为空
    def test_login1(self):
        po=login(self.driver)
        po.user_login()
        self.assertEqual(po.error_hint(),'抱歉，密码空或包含非法字符')
        function.insert_img(self.driver,'login_pwd_empty.png')

    #账号密码不匹配
    def test_login2(self):
        self.user_login_verify(username='随便输入的账号',passwd='qinghui')
        po=login(self.driver)
        self.assertIn('登录失败，您还可以尝试',po.error_hint())
        function.insert_img(self.driver,'login_user_pwd_error.png')

    #登陆成功
    def test_login_su(self):
        username='逆千凡'
        passwd='qinghui'
        self.user_login_verify(username=username,passwd=passwd)
        time.sleep(3)
        po=login(self.driver)
        self.assertEqual(po.user_login_success(),username)
        function.insert_img(self.driver,'login_success.png')
if __name__=='__main__':
    unittest.main()



