from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
class Page(object):
    start_url='http://home.lvy.cn'
    def __init__(self,selenium_driver,url=start_url,parent=None):
        self.driver=selenium_driver
        self.url=url
        self.timeout=30
        self.parent=parent
    #根据url判断是否正确打开
    def on_page(self,url):
        return self.driver.current_url == url
    #打开网页
    def open(self,url):
        url=self.url+url
        print(url)
        self.driver.get(url)
        self.driver.implicitly_wait(30)
        assert self.on_page(url),'页面未打开'+str(url)
    #元素定位
    def find_element(self,loc,more=False,presence=False):
        #print(loc)
        try:
            if presence:
                WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(loc))
            else:
                WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc))
            if more:
                return self.driver.find_elements(*loc)
            else:
                return self.driver.find_element(*loc)
        except AttributeError :
            print('元素未找到',loc)

    def send_keys(self,loc,value,clear=True,click=True):
        try:
            if click:
                self.find_element(loc).click()
            if clear:
                self.find_element(loc).clear()
            self.find_element(loc).send_keys(value)
        except AttributeError:
            print('元素未找到',loc)

    #进入frame
    def switch_frame(self,ref=None):
        if ref:
            self.driver.switch_to.frame(ref)
        else:
            self.driver.switch_to.default_content()

    # 切换窗口
    def switch_window(self, close=True):
        now = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        if close:
            self.driver.close()
        for handle in all_handles:
            if handle != now:
                self.driver.switch_to.window(handle)

    #鼠标悬浮
    def move_to_element(self,loc):
        element=self.find_element(loc)
        ActionChains(self.driver).move_to_element(element).perform()
    #设置cookie
    def add_cookies(self):
        self.driver.delete_all_cookies()
        with open('cookies.txt', 'r') as f:
            cookies = json.load(f)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        #sleep(1)
        self.driver.refresh()
        #self.driver.implicitly_wait(30)
    #滚动条
    def scroll(self,top):
        js='var q=document.documentElement.scrollTop='+str(top)
        self.driver.execute_script(js)






