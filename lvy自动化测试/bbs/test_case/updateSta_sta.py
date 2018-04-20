#加载models目录
# sys.path.append("./models")
# #加载page_obj目录
# sys.path.append("./page_obj")
from page_obj.updateStaPage import updateSta
from models import myunit,function
import time,unittest
class updateStaTest(myunit.myTest):
    def update_sta_verify(self,status=''):
        updateSta(self.driver).update_sta(status)
    #测试发送空状态
    def test_update1(self):
        po= updateSta(self.driver)
        po.open('/')
        po.add_cookies()
        # 原来的状态
        old=po.show_text()
        #点击发布
        po.click_send_sta()
        #新的状态
        new=po.show_text()
        self.assertEqual(old,new)
        function.insert_img(self.driver,'update_empty.png')
    # #测试字数过长
    def test_update2(self):
        status1='啥啥'*100
        status2='初来乍到'
        self.update_sta_verify(status1+status2)
        po=updateSta(self.driver)
        self.assertNotIn(status2,po.show_text())
        function.insert_img(self.driver,'update_too_long.png')
    #发送状态成功
    def test_update3(self):
        status='今天天气真好，是个出游的好日子'
        self.update_sta_verify(status)
        po=updateSta(self.driver)

        self.assertEqual(status,po.show_text())
        function.insert_img(self.driver,'update_success.png')
if __name__=='__main__':
    unittest.main()



