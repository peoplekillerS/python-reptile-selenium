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
list = ["习惯失恋", "必杀技", "不浪漫是罪名", "沉默是金"]
lt = ['22']
# ["男儿当自强","感动","我的宣言","友情岁月","暗里着迷","无赖","真的爱你","七友","护花使者","记得忘记","红日","寒舍","情意结","大地","苦瓜","酷爱","樱花树下","烂泥"]

for i in range(len(list)):
    web.get('https://y.qq.com/')
    time.sleep(1)
    web.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/div[1]/div[1]/input').send_keys(list[i])
    time.sleep(0.5)
    web.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/div[1]/div[1]/button/i').click()
    time.sleep(1)
    web.find_element(By.XPATH,
                     '//*[@id="app"]/div/div[3]/div/div/div[4]/ul[2]/li[1]/div/div[2]/span/a/div/span').click()
    time.sleep(1)
    element = web.find_element(By.XPATH, '//*[@id="logo"]/img')
    links = []
    links.append(element.get_attribute('src'))
    img_resp = requests.get(links[0])
    img_resp.content  # 这里拿到的是字节
    with open(r"C:\Users\pqs-xsz-xia\Desktop\pic" + '%d' % i + '.jpg', mode="wb") as f:
        f.write(img_resp.content)  # 图片内容写入文件

web.get("https://chat.forchange.cn/")
time.sleep(1)
oo = 1
for i in list:

    time.sleep(1)
    space = web.find_element(By.XPATH, '//*[@id="AI-EDU"]/div/div[1]/main/div[2]/form/div/div[2]/textarea')
    space.clear()
    space.send_keys("帮我写一下粤语歌曲《" + i + "》的乐评")
    time.sleep(2)
    web.find_element(By.XPATH, '//*[@id="AI-EDU"]/div/div[1]/main/div[2]/form/div/div[2]/button').click()
    time.sleep(40)
    tx = web.find_element(By.XPATH,
                          '//*[@id="AI-EDU"]/div/div[1]/main/div[1]/div/div/div/div[2]/div/div[' + '%d' % (2 * oo) + ']/div/p').text

    lt.append(tx)
    print(lt[oo-1])
    time.sleep(2)
    oo = oo + 1

for i in list:
    j = 0
    web.get('https://creator.xiaohongshu.com/creator/home')
    time.sleep(2)
    web.find_element(By.XPATH, '//*[@id="page"]/div/main/div[1]/div/div[1]/a').click()
    time.sleep(2)
    web.find_element(By.XPATH, '//*[@id="publish-container"]/div/div[1]/div[2]/span').click()
    time.sleep(2)
    element = web.find_element(By.XPATH, '//*[@id="web"]/div/div[1]/div[2]/div[1]/div/input')  # 定位到上传文件框
    time.sleep(1)
    path=r'C:\Users\pqs-xsz-xia\Desktop\pic\%d' % j + '.jpg'
    element.send_keys(path)  # 上传文件
    # element.send_keys(r'D:\作业\1.jpg')  # 上传文件
    time.sleep(1)
    web.find_element(By.XPATH, '//*[@id="web"]/div/div[2]/div[2]/div[2]/input').send_keys(i)
    web.find_element(By.XPATH, '//*[@id="post-textarea"]').send_keys(lt[j])
    time.sleep(3)
    j = j + 1
    # 执行js，滑动到最底部
    js_button = 'document.documentElement.scrollTop=100000'
    web.execute_script(js_button)
    time.sleep(3)
    web.find_element(By.XPATH, '//*[@id="web"]/div/div[2]/div[2]/div[7]/button[1]/span').click()
    time.sleep(2)



# web.close()

