#加载models目录
# sys.path.append("./models")
# #加载page_obj目录
# sys.path.append("./page_obj")
from page_obj.showArtPage import showArt
from models import myunit,function
import time,unittest
class showArtTest(myunit.myTest):
    def show_art_verify(self):
        return showArt(self.driver).show_art()
    #测试点击前和点击后文章标题一致
    def test_show1(self):
        before,after=self.show_art_verify()
        before=before.split()[0]
        self.assertIn(before,after)
        function.insert_img(self.driver,'show_art.png')

if __name__=='__main__':
    unittest.main()



