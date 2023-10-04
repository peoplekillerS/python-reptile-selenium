# 能不能让我的程序 链接 浏览器 来完成各种复杂的操作我们只接受最终的结果
# selenium 自动化测试根据
# 可以 打开浏览器 让人一样取操作浏览器
# 程序员可以让selenium直接提起网页上的各种信息
# https://npm.taobao.org/mirrors/chromedriver

# selenium 启动谷歌浏览器
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 1、创建浏览器对象
web =Chrome()
# 2、打开一个网站
web.get("https://www.baidu.com")
time.sleep(10)

print(web.title)





















