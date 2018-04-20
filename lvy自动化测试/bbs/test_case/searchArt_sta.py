#加载models目录
# sys.path.append("./models")
# #加载page_obj目录
# sys.path.append("./page_obj")
from page_obj.searchPage import search
from models import myunit,function
import random,time,unittest
class searchArtTest(myunit.myTest):
    def search_art_verify(self,keyword=''):
        search(self.driver).search_art(keyword)
    #测试搜索内容为空
    def test_search1(self):
        self.search_art_verify()
        url='http://bbs.lvy.cn/search.php?mod=forum'
        current_url=self.driver.current_url
        self.assertEqual(url,current_url)
        function.insert_img(self.driver,'search_empty.png')
    #测试搜索内容不存在
    def test_search2(self):
        keyword='哈卷三个多月卡进口国的情况'
        po=search(self.driver)
        po.search_art(keyword)
        self.assertEqual('对不起，没有找到匹配结果。',po.not_find())
        function.insert_img(self.driver,'search_not_find.png')
    #搜索成功
    def test_search3(self):
        keyword='三亚'
        self.search_art_verify(keyword)
        po = search(self.driver)
        self.assertEqual(keyword, po.success_keyword())
        function.insert_img(self.driver, 'search_success.png')
if __name__=='__main__':
    unittest.main()



