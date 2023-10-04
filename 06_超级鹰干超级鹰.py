import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from chaojiying import Chaojiying_Client

web=Chrome()

web.get("https://www.chaojiying.com/user/login/")

# 处理验证码
img = web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/div/img').screenshot_as_png
chaojiying = Chaojiying_Client('superpqs', '2432376957', '944125')
dic=chaojiying.PostPic(img,1902)
verify_code=dic['pic_str']

# 向页面填入验证码
web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input').send_keys("superpqs")
web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input').send_keys("2432376957")
web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input').send_keys(verify_code)
# 点击登录
web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input').click()

time.sleep(5)













