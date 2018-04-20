#加载models目录
# sys.path.append("./models")
# #加载page_obj目录
# sys.path.append("./page_obj")
from page_obj.sendArtPage import SendArt
from models import myunit,function
import random,time,unittest
class sendArtTest(myunit.myTest):
    def send_art_verify(self,title='',article=''):
        SendArt(self.driver).send_article_all(title=title,article=article)
    #测试标题或者文章为空
    def test_send1(self):
        title=''
        article=''
        self.send_art_verify(title,article)
        po=SendArt(self.driver)
        self.assertEqual('抱歉，您尚未输入标题或内容',po.error_hint())
        function.insert_img(self.driver,'send_empty.png')
    #测试字数过长
    def test_send2(self):
        title='啥啥啥'*100
        article='初来乍到'
        self.send_art_verify(title,article)
        po=SendArt(self.driver)
        self.assertIn('您的帖子长度不符合要求。',po.error_hint())
        function.insert_img(self.driver,'send_too_long.png')
    #发帖成功
    def test_send3(self):
        title='初来乍到'
        article='请问一下有没有一样新来的朋友。有时间约一下'
        self.send_art_verify(title,article)
        #必须强制等待
        time.sleep(3)
        self.assertIn(title, self.driver.page_source)
        self.assertIn(article,self.driver.page_source)
        function.insert_img(self.driver,'send_success.png')
if __name__=='__main__':
    unittest.main()



