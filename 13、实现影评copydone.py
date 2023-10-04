from selenium.webdriver import Chrome
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
# chrome.exe --remote-debugging-port=9527 --user-data-dir=“D:\AutomationProfile”
opt = Options()
opt.add_experimental_option("debuggerAddress", "127.0.0.1:9527")
web = Chrome(options=opt)
list = ["千与千寻", "盗梦空间", "楚门的世界", "星际穿越", "三杀大闹好莱坞", "忠犬八公的故事", "海上钢琴师","机器人总动员","疯狂动物城","熔炉","触不可及"]
lt = []
# for i in range(len(list)):
#     web.get('https://movie.douban.com/')
#     time.sleep(1.5)
#     web.find_element(By.XPATH, '//*[@id="inp-query"]').send_keys(list[i])
#     time.sleep(1)
#     web.find_element(By.XPATH, '//*[@id="db-nav-movie"]/div[1]/div/div[2]/form/fieldset/div[2]/input').click()
#     time.sleep(2)
#     web.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div[1]/div[1]/div[1]/div/div[1]/a').click()
#     time.sleep(2)
#     element = web.find_element(By.XPATH, '//*[@id="mainpic"]/a/img')
#     links = []
#     links.append(element.get_attribute('src'))
#     img_resp = requests.get(links[0])
#     img_resp.content  # 这里拿到的是字节
#     with open("img_movie/" + '%d' % i + '.jpg', mode="wb") as f:
#         f.write(img_resp.content)  # 图片内容写入文件


oo=1
for i in list:
    web.get("https://copyai.cn/creationPage")
    time.sleep(5)
    web.find_element(By.XPATH,'//*[@id="1grrpma8"]/section/section/div[2]/section/div[1]/div/div[5]/div[2]/div[2]').click()
    time.sleep(1)
    space = web.find_element(By.XPATH, '//*[@id="1grrp10l"]/section/section/div[2]/section/section/div[3]/div/div[2]/div[2]/div[2]/textarea')
    space.send_keys("经典电影《" + i + "》的影评")
    time.sleep(0.5)
    web.find_element(By.XPATH, '//*[@id="1grrp10l"]/section/section/div[2]/section/section/div[3]/div/div[2]/div[5]/span/input').click()
    time.sleep(1)
    web.find_element(By.XPATH,'//*[@id="1grrp10l"]/section/section/div[2]/section/section/div[3]/div/div[2]/div[1]/div[4]/div/div/div/div/div/ul/li[4]').click()
    time.sleep(0.5)
    web.find_element(By.XPATH,'//*[@id="1grrp10l"]/section/section/div[2]/section/section/div[3]/div/div[3]/button').click()
    time.sleep(40)


    time.sleep(2)
    oo = oo+1

j = 0
time.sleep(2)

for i in list:
    k = 19
    web.get('https://creator.xiaohongshu.com/creator/home')
    time.sleep(1)
    web.find_element(By.XPATH, '//*[@id="page"]/div/main/div[1]/div/div[1]/a').click()
    time.sleep(2)
    web.find_element(By.XPATH, '//*[@id="publish-container"]/div/div[1]/div[2]/span').click()
    time.sleep(3)
    element = web.find_element(By.XPATH, '//*[@id="web"]/div/div[1]/div[2]/div[1]/div/input')  # 定位到上传文件框
    ph=r'D:\python爬虫\第五章\img_movie\%d' % j + '.jpg'
    element.send_keys(ph)  # 上传文件
    time.sleep(1)
    web.find_element(By.XPATH, '//*[@id="web"]/div/div[2]/div[2]/div[2]/input').send_keys(
        '分享100部好电影---第' + '%d' % k + '部:' + i)
    web.find_element(By.XPATH, '//*[@id="post-textarea"]').send_keys(lt[j])
    web.find_element(By.XPATH, '//*[@id="post-textarea"]').send_keys('#豆瓣好电影推荐#好看电影推荐')
    time.sleep(2)
    j = j + 1
    js_button = 'document.documentElement.scrollTop=100000'
    web.execute_script(js_button)
    time.sleep(3)
    web.find_element(By.XPATH, '//*[@id="web"]/div/div[2]/div[2]/div[7]/button[1]/span').click()
    time.sleep(2)

# web.close()
