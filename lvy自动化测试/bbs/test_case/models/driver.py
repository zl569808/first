from selenium.webdriver import Remote
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
def browser():
   # lists={
   #     'http://127.0.0.1:4444/wd/hub':'chrome',
   #     'http://127.0.0.1:5555/wd/hub':'chrome',
   #     # 'http://192.168.0.109:5555/wd/hub':'chrome',
   #     # 'http://192.168.0.112:5555/wd/hub':'chrome',
   #     # 'http://192.168.0.114:5555/wd/hub':'chrome',
   #  }
   # for host,browser in lists.items():
   #     driver= Remote(command_executor=host,
   #                    desired_capabilities={'platform':'ANY',
   #                                     'browserName':browser,
   #                                     'version': '',
   #                                     'javascriptEnabled':True
   #                                    }
   #                )
    # return driver
   driver=webdriver.Chrome()
   return driver
if __name__=='__main__':
    driver=browser()
    driver.get('http://home.lvy.cn/')
    driver.quit()

