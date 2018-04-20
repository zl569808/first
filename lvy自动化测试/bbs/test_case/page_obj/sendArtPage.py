from .base import Page
from selenium.webdriver.common.by import By
from time import sleep
import json
class SendArt(Page):
    '''首先定位元素'''
    #进入论坛
    click_in_bbs_loc=(By.CSS_SELECTOR,'a[href="http://bbs.lvy.cn"]')
    #点击进入发帖界面
    click_quick_send_loc=(By.CLASS_NAME,'ubtn_fastpost')
    #选择板块
    click_block1_loc=(By.LINK_TEXT,'驴友户外活动')
    click_block2_loc=(By.LINK_TEXT,'自驾骑行')
    click_block3_loc=(By.LINK_TEXT,'骑行吧')
    #点击发贴
    click_send_loc=(By.ID,'postbtn')
    #标题输入框
    title_loc=(By.ID,'subject')
    #frame定位
    ref_id='e_iframe'
    #文章输入框
    article_loc=(By.TAG_NAME,'body')
    #输入文章后应退出frame
    #点击发表帖子
    sendArt_loc=(By.ID,'postsubmit')

    '''定义操作函数'''
    #点击进入论坛
    def click_bbs(self):
        self.find_element(self.click_in_bbs_loc).click()
        self.driver.implicitly_wait(30)
    #点击快速发帖
    def click_quick_send(self):
        try:
            self.driver.find_element_by_link_text('关闭').click()
            self.find_element(self.click_quick_send_loc).click()
        except:
            self.find_element(self.click_quick_send_loc).click()
    #点击选择板块
    def click_block(self):
        self.find_element(self.click_block1_loc).click()
        self.find_element(self.click_block2_loc).click()
        self.find_element(self.click_block3_loc).click()
    #点击发帖
    def click_send(self):
        self.find_element(self.click_send_loc).click()
        self.driver.implicitly_wait(30)
    #输入标题
    def input_title(self,title):
        self.send_keys(self.title_loc,title)
    #输入文章
    def input_article(self,article):
        self.switch_frame(self.ref_id)
        self.send_keys(self.article_loc,article)
        self.switch_frame()
    #发表帖子
    def send_article(self):
        self.find_element(self.sendArt_loc).click()
    #统一
    def send_article_all(self,title='',article=''):
        self.open('/')
        self.add_cookies()

        self.click_bbs()
        #进入发帖
        # sleep(10)
        self.click_quick_send()
        self.click_block()
        self.click_send()
        #发帖
        self.input_title(title)
        self.input_article(article)
        self.send_article()

    #定位错误提示
    error_loc=(By.CLASS_NAME,'pc_inner')

    # 返回错误信息文本
    def error_hint(self):
        return self.find_element(self.error_loc).text
