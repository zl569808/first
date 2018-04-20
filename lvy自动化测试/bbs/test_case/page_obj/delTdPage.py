from .base import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
class delTd(Page):
    '''首先定位元素'''

    #点击我的动态
    my_td_loc=(By.LINK_TEXT,'我的动态')
    #点击删除
    del_sta_loc=(By.CSS_SELECTOR,'a[title="删除动态"]')
    #操作框
    alt_loc=(By.CLASS_NAME,'m_c')
    #确认删除
    accept_loc=(By.NAME,'feedsubmitbtn')
    #取消删除
    dismiss_loc=(By.CSS_SELECTOR,'a[title="关闭"]')
    #动态内容
    dt_text_loc=(By.CSS_SELECTOR,"li.cl >div.cl")

    '''定义操作函数'''
    #点击进入我的动态
    def click_mydt(self):
        self.find_element(self.my_td_loc).click()
        self.driver.implicitly_wait(30)
    #点击删除动态
    def del_dt(self):
        self.move_to_element(self.dt_text_loc)
        print(self.dt_text_loc)
        self.find_element(self.del_sta_loc).click()
    #确认操作框
    def accept(self):
        self.find_element(self.accept_loc,presence=True).click()
    #取消操作矿
    def dismiss(self):
        self.find_element(self.dismiss_loc,presence=True).click()
    # 返回动态文本
    def dt_hint(self):
        return self.find_element(self.dt_text_loc).text
    #统一操作
    def del_mydt(self,delete=True):
        self.open('/')
        self.add_cookies()
        self.click_mydt()
        # 操作前的内容
        old = self.dt_hint()
        # 操作
        self.del_dt()
        WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located(self.alt_loc))
        if delete:
            self.accept()
            self.driver.refresh()
        else:
            self.dismiss()
        # 操作后的内容
        new = self.dt_hint()
        return old,new

