from .showArtPage import showArt
from selenium.webdriver.common.by import By
from time import sleep
class replyArt(showArt):
    #该测试page继承于查看贴子
    '''首先定位元素'''
    # 输入回复
    input_reply_loc = (By.TAG_NAME, 'textarea')
    #发表回复
    click_reply_loc=(By.ID,'fastpostsubmit')
    '''定义操作函数'''
    # 滚动条下拉
    def replyScroll(self):
        self.scroll(2500)
    # 输入回复
    def input_reply(self,value):
        self.send_keys(self.input_reply_loc,value)
    #点击回复
    def click_reply(self):
        return self.find_element(self.click_reply_loc).click()
    #统一
    def reply_art(self,body=''):

        #进入帖子
        self.show_art()
        #回帖
        self.replyScroll()
        self.input_reply(body)
        self.click_reply()
    #错误
    error_loc=(By.CLASS_NAME,'pc_inner')
    def error_hint(self):
        return self.find_element(self.error_loc,presence=True).text




