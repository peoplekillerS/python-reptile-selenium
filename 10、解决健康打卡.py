# 能不能让我的程序 链接 浏览器 来完成各种复杂的操作我们只接受最终的结果
# selenium 自动化测试根据
# 可以 打开浏览器 让人一样取操作浏览器
# 程序员可以让selenium直接提起网页上的各种信息
# https://npm.taobao.org/mirrors/chromedriver

import requests as requests
# selenium 启动谷歌浏览器
from selenium.webdriver import Chrome
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# selenium 启动谷歌浏览器
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 1、创建浏览器对象

web =Chrome()
# 2、打开一个网站
web.get("https://sso.scut.edu.cn/cas/login?service=https%3A%2F%2Fenroll.scut.edu.cn%2Fdoor%2Findex_h5.html")
time.sleep(1)
web.find_element(By.XPATH,'//*[@id="un"]').send_keys("202130071190")
web.find_element(By.XPATH,'//*[@id="pd"]').send_keys("2432376957wbyPQS",Keys.ENTER)

time.sleep(1)
#web.switch_to.window(web.window_handles[-1]) # -1就是最后一个

web.set_window_size(500, 900)
web.find_element(By.XPATH,'//*[@id="container"]/div[5]/div[2]/div[3]/div[2]').click()
web.find_element(By.XPATH,'//*[@id="container"]/div[3]/div[5]/div[2]/div[1]/img').click()
web.find_element(By.XPATH,'//*[@id="container"]/div[7]/form/button').click()
web.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[3]/a[2]').click()

time.sleep(1)

web.close()























