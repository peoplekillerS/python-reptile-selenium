import time

from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
# 如果你的程序被识别出来是机器干的
# chrome版本小于88 在你启动浏览器的时候 没有加载任何内容 向页面嵌入js代码  去掉webdriver
# """""""


# 2、chrome版本大于88
option=Options()
option.add_argument('--disable-blink-features=AutomationControlled')

web = Chrome(options=option)

web.get("https://kyfw.12306.cn/otn/resources/login.html")
# time.sleep(1)
# web.find_element(By.XPATH,'//*[@id="J-btn-login"]').click()
# time.sleep(1)
web.find_element(By.XPATH, '//*[@id="J-userName"]').send_keys("13016068824")
web.find_element(By.XPATH, '//*[@id="J-password"]').send_keys("2432376957wbyPQS")
web.find_element(By.XPATH, '//*[@id="J-login"]').click()
# 点击登录
web.find_element(By.XPATH, '//*[@id="toolbar_Div"]/div[2]/div[2]/ul/li[1]/a').click()
time.sleep(5)
# 拖拽

btn=web.find_element(By.XPATH,'//*[@id="nc_1_n1z"]')
ActionChains(web).drag_and_drop_by_offset(btn,300,0).perform()
time.sleep(1)


