#加载models目录
# sys.path.append("./models")
# #加载page_obj目录
# sys.path.append("./page_obj")
from page_obj.delTdPage import delTd
from models import myunit,function
import time,unittest
# class updateStaTest(myunit.myTest):
#     def del_dt_verify(self,delete=True):
#         return delTd(self.driver).del_mydt(delete=delete)
#     #取消删除
#     def test_del1(self):
#         old,new=self.del_dt_verify(delete=False)
#         self.assertEqual(new,old)
#         function.insert_img(self.driver,'del_dt_dismiss.png')
#     #确认删除
#     def test_del1(self):
#         old,new=self.del_dt_verify(delete=True)
#         self.assertNotEqual(new,old)
#         function.insert_img(self.driver,'del_dt_accept.png')

if __name__=='__main__':
    unittest.main()



