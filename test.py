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
opt.add_experimental_option("debuggerAddress", "127.0.0.1:9527")
web = Chrome(options=opt)
list=['666']
lt=['777']


web.get('https://y.qq.com/')
time.sleep(1)
web.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/div/div[1]/div[1]/input').send_keys('钟无艳')
web.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/div/div[1]/div[1]/button/i').click()
time.sleep(1)
web.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div/div/div[4]/ul[2]/li[1]/div/div[2]/span/a/div/span').click()
time.sleep(1)
element=web.find_element(By.XPATH,'//*[@id="logo"]/img')
links = []
links.append(element.get_attribute('src'))

img_resp = requests.get(links[0])
img_resp.content  # 这里拿到的是字节
with open("img/"+'1.jpg', mode="wb") as f:
    f.write(img_resp.content)  # 图片内容写入文件








# for i in list:
#     j=0
#     web.get('https://creator.xiaohongshu.com/creator/home')
#     time.sleep(1)
#     web.find_element(By.XPATH,'//*[@id="page"]/div/main/div[1]/div/div[1]/a').click()
#     time.sleep(1)
#     web.find_element(By.XPATH,'//*[@id="publish-container"]/div/div[1]/div[2]/span').click()
#     time.sleep(2)
#     element = web.find_element(By.XPATH,'//*[@id="web"]/div/div[1]/div[2]/div[1]/div/input')  # 定位到上传文件框
#     element.send_keys(r'D:\作业\1.jpg')  # 上传文件
#     web.find_element(By.XPATH,'//*[@id="web"]/div/div[2]/div[2]/div[2]/input').send_keys(i)
#     web.find_element(By.XPATH,'//*[@id="post-textarea"]').send_keys(lt[j])
#     j=j+1
#     # 执行js，滑动到最底部
#     js_button = 'document.documentElement.scrollTop=100000'
#     web.execute_script(js_button)
#     time.sleep(2)
#     web.find_element(By.XPATH,'//*[@id="web"]/div/div[2]/div[2]/div[7]/button[1]/span').click()
#
#
