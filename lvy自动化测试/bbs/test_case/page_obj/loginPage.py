from .base import Page
from selenium.webdriver.common.by import By
from time import sleep
import json
class login(Page):
    '''首先定位元素'''
    #点击进入登陆界面
    click_login_loc=(By.LINK_TEXT,'登录')
    #账号输入框
    username_loc=(By.CSS_SELECTOR,'input[id^="username_L"]')
    #密码输入框
    password_loc=(By.CSS_SELECTOR,'input[id^="password3_L"]')
    #点击立即登录
    submit_loc=(By.CSS_SELECTOR,'button[name="loginsubmit"] strong')

    #定位错误提示
    error_loc=(By.CLASS_NAME,'pc_inner')

    '''定义操作函数'''
    #点击进入登陆
    def click_login(self):

        self.find_element(self.click_login_loc).click()
    #输入用户名
    def input_user(self,username):
        self.send_keys(self.username_loc,username)
    #输入密码
    def input_passwd(self,passwd):
        self.send_keys(self.password_loc,passwd)
    #登陆提交
    def submit_login(self):
        self.find_element(self.submit_loc).click()
    #统一
    def user_login(self,username='',passwd=''):
        self.open('/')
        self.click_login()
        self.driver.implicitly_wait(30)
        self.input_user(username)
        self.input_passwd(passwd)
        self.submit_login()
        sleep(1)

    #返回错误信息文本
    def error_hint(self):
        return self.find_element(self.error_loc).text

    #登陆成功后
    login_success_loc=(By.CSS_SELECTOR,'.status_loginned a')
    def user_login_success(self):
        sleep(3)
        #保存cookie
        cookies=self.driver.get_cookies()
        with open('cookies.txt','w') as f:
            json.dump(cookies,f)
        return self.find_element(self.login_success_loc).text
