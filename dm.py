from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import requests
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait

url = "https://copyai.cn/creativestage"
# 设置Chrome浏览器选项

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('disable-info bars')
options.add_argument('--disable-extensions')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
options.add_argument('--remote-debugging-port=9527')
options.add_experimental_option("debuggerAddress", "127.0.0.1:9527")

# 实例化浏览器驱动
driver = webdriver.Chrome(options=options)


for i in range(1,80):
    driver.get("https://www.pixiv.net/tags/%E6%98%8E%E6%97%A5%E6%96%B9%E8%88%9F/illustrations")
    time.sleep(3)
    element = driver.find_element(By.XPATH, f'//*[@id="root"]/div[2]/div/div[2]/div/div[6]/div/section[2]/div[2]/ul/li[{i}]/div/div[1]/div/a/div[1]/img')
    element.click()
    time.sleep(2)
    element=driver.find_element(By.XPATH,f'//*[@id="root"]/div[2]/div/div[2]/div/div[1]/main/section/div[1]/div/figure/div[1]/div[1]/div/a/img')
                                        f'//*[@id="root"]/div[2]/div/div[2]/div/div[1]/main/section/div[1]/div/figure/div/div[2]/div/a/img'

                                        f'//*[@id="root"]/div[2]/div/div[2]/div/div[1]/main/section/div[1]/div/figure/div[1]/div[1]/div/a/img'
                                        f'//*[@id="root"]/div[2]/div/div[2]/div/div[1]/main/section/div[1]/div/figure/div[1]/div[1]/div/a/img'
    time.sleep(2)
    img_resp = requests.get(element.get_attribute('src'))
    with open(f'illustration/{list[i]}' + '%d' % i + '.jpg', mode="wb") as f:
        f.write(img_resp.content)  # 图片内容写入文件
    time.sleep(15)


# 关闭浏览器
driver.quit()

