from .base import Page
from selenium.webdriver.common.by import By
from time import sleep
from random import randint
class showArt(Page):
    '''首先定位元素'''
    # 进入论坛
    click_in_bbs_loc = (By.CSS_SELECTOR, 'a[href="http://bbs.lvy.cn"]')
    #生成随机数以便随机选择文章
    rand=randint(0,25)
    #帖子链接
    art_link_loc=(By.CSS_SELECTOR,'td.fl_by a.xi2')
    #帖子标题
    art_title_loc=(By.ID,'thread_subject')
    '''定义操作函数'''
    # 点击进入论坛
    def click_bbs(self):
        self.find_element(self.click_in_bbs_loc).click()
        self.driver.implicitly_wait(30)
    #滚动条下拉
    def myScroll(self):
        self.scroll(1000)
    #点击前获取帖子标题
    def before_art_title(self):
        print('。。。下面为本次随机选取的文章。。。。')
        print(self.find_element(self.art_link_loc,more=True)[self.rand].text)
        return self.find_element(self.art_link_loc,more=True)[self.rand].text
    #点击进入帖子
    def click_art(self):
        self.find_element(self.art_link_loc,more=True)[self.rand].click()
        #self.driver.implicitly_wait(30)
    #点击后获取帖子标题
    def after_art_title(self):
        return self.find_element(self.art_title_loc).text

    #统一
    def show_art(self,status=''):
        self.open('/')
        self.add_cookies()

        self.click_bbs()
        self.myScroll()
        before=self.before_art_title()
        self.click_art()
        after=self.after_art_title()
        return before,after
