#加载models目录
# sys.path.append("./models")
# #加载page_obj目录
# sys.path.append("./page_obj")
from page_obj.replyArtPage import replyArt
from models import myunit,function
import time,unittest
class replyArtTest(myunit.myTest):
    def reply_art_verify(self,body=''):
        replyArt(self.driver).reply_art(body=body)
    #测试回复内容为空
    def test_reply1(self):
        self.reply_art_verify()
        function.insert_img(self.driver, 'reply_emply.jpg')
        po = replyArt(self.driver)
        self.assertEqual(po.error_hint(),'您的帖子长度不符合要求。 当前长度: 0 字节 系统限制: 10 到 10000 字节')
    def test_reply2(self):
        body = '很羡慕这样的生活啊'
        self.reply_art_verify(body)
        time.sleep(1)
        self.assertIn(body,self.driver.page_source)
        function.insert_img(self.driver, 'reply_art.jpg')

if __name__=='__main__':
    unittest.main()



