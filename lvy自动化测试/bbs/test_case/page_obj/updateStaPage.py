from .base import Page
from selenium.webdriver.common.by import By
from time import sleep
class updateSta(Page):
    '''首先定位元素'''
    #动态输入框
    input_loc=(By.ID,'mood_message')
    #点击发布
    click_send_loc=(By.CLASS_NAME,'moodfm_btn')
    #发布成功显示处
    status_loc=(By.ID,'mood_mystatus')

    '''定义操作函数'''
    #输入状态
    def input_sta(self,status=''):
        self.send_keys(self.input_loc,status)
    #点击发布
    def click_send_sta(self):
        self.find_element(self.click_send_loc).click()
        sleep(3)
    #统一发送
    def update_sta(self,status=''):
        self.open('/')
        self.add_cookies()

        self.input_sta(status=status)
        self.click_send_sta()
    #发布成功的显示文本
    def show_text(self):
        return self.find_element(self.status_loc).text
