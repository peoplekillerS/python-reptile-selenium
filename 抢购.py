from selenium.webdriver import Chrome
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests

# chrome.exe --remote-debugging-port=9527 --user-data-dir=“D:\AutomationProfile”
# 1、创建浏览器对象
opt = Options()
# opt.add_argument('--disable-gpu')
# opt.add_argument('--headless')
opt.add_experimental_option("debuggerAddress", "127.0.0.1:9527")
# opt.add_experimental_option('excludeSwitches', ['enable-automation'])
# opt.add_experimental_option("useAutomationExtension", False)  # 去掉开发者警告
# opt.add_argument("--disable-blink-features")
# opt.add_argument("--disable-blink-features=AutomationControlled")
web = Chrome(options=opt)
# web.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
#     "source": """
#     Object.defineProperty(navigator, 'webdriver', {
#       get: () => undefined
#     })
#   """
# })

# 2、打开一个网站
web.get("https://miaosha.jd.com/")



