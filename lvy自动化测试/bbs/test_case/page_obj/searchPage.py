from .base import Page
from selenium.webdriver.common.by import By
from time import sleep

class search(Page):
    '''首先定位元素'''
    #进入论坛
    click_in_bbs_loc=(By.CSS_SELECTOR,'a[href="http://bbs.lvy.cn"]')
    #搜索框
    search_loc=(By.CLASS_NAME,'key')
    #搜索按钮
    click_search_loc=(By.CLASS_NAME,'submit')
    #搜索成功后关键字，多元素查找
    keyword_loc=(By.TAG_NAME,'font')
    #搜索不成功后提示信息
    not_find_loc=(By.CLASS_NAME,'xg2')

    '''定义操作函数'''
    #点击进入论坛
    def click_bbs(self):
        self.find_element(self.click_in_bbs_loc).click()
        self.driver.implicitly_wait(30)
    #输入搜索内容
    def input_search_keys(self,keyword=''):
        self.send_keys(self.search_loc,keyword)
    #点击搜索
    def click_search(self):
        self.find_element(self.click_search_loc).click()
        self.driver.implicitly_wait(30)
    #统一
    def search_art(self,keyword=''):
        self.open('/')
        self.add_cookies()

        self.click_bbs()
        self.input_search_keys(keyword)
        self.click_search()
        self.switch_window()

    # 搜索成功后返回的关键字
    def success_keyword(self):
        return self.find_element(self.keyword_loc).text

    # 搜索内容不存在时返回的text
    def not_find(self):
        return self.find_element(self.not_find_loc).text
