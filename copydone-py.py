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
list = ['玩具总动员','海底总动员','怪兽大学']
lt = []
time.sleep(1)


# 打开目标网页
driver.get(url)
# 使用正则表达式匹配元素ID的规律
pattern = re.compile(r'id="([a-z0-9]{8})"')
# 在页面源代码中查找匹配规律的元素ID
time.sleep(2)
# 在页面源代码中查找匹配规律的元素ID
match = pattern.search(driver.page_source)
# 获取copydone文案
for i in range(len(list)):
    # 找到第一个匹配的元素ID，并生成对应的XPath和CSS Selector 开始创作
    element_id = match.group(1)
    xpath = f'//*[@id="{element_id}"]/section/div[1]/div/button'
    css_selector = f'#{element_id} > section > div.arco-layout-sider.arco-layout-sider-light > div > button'
    # 使用DriverWait等待元素加载完成
    wait = WebDriverWait(driver, 5)
    # 使用XPath定位元素
    button = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    # 点击按钮
    button.click()
    time.sleep(3)

    # 公众号类型
    x1 = f'//*[@id="{element_id}"]/section/section/div[2]/section/div[1]/div/div[5]/div[2]/div[9]'
    button = wait.until(EC.presence_of_element_located((By.XPATH, x1)))
    button.click()
    time.sleep(4)
    x1 = f'//*[@id="{element_id}"]/section/section/div[2]/section/section/div[3]/div/div[2]/div[2]/div[2]/textarea'
    # 内容主题
    button = wait.until(EC.presence_of_element_located((By.XPATH, x1)))
    button.send_keys(f'电影《{list[i]}》的影评')
    time.sleep(2)
    # 文案场景
    x1 = f'//*[@id="{element_id}"]/section/section/div[2]/section/section/div[3]/div/div[2]/div[3]/span/input'
    button = wait.until(EC.presence_of_element_located((By.XPATH, x1)))
    button.click()
    time.sleep(2)
    x1 = f'//*[@id="{element_id}"]/section/section/div[2]/section/section/div[3]' \
         f'/div/div[2]/div[1]/div[2]/div/div/div/div/div[1]/ul/li[4]'
    button = wait.until(EC.presence_of_element_located((By.XPATH, x1)))
    button.click()
    time.sleep(2)
    # 内容描述
    x1 = f'//*[@id="{element_id}"]/section/section/div[2]/section' \
         f'/section/div[3]/div/div[2]/div[4]/div[2]/textarea'
    b1 = wait.until(EC.presence_of_element_located((By.XPATH, x1)))
    b1.send_keys(f'通过对其中人物形象，并用上剧中的台词，来对《{list[i]}》这部电影做出有强烈文艺感的影评')
    # 语言风格类型
    x2 = f'//*[@id="{element_id}"]/section/section/div[2]/section/section/div[3]/div/div[2]/div[5]/span/input'
    time.sleep(1)
    b2 = wait.until(EC.presence_of_element_located((By.XPATH, x2)))
    b2.click()
    time.sleep(1)
    x3 = f'//*[@id="{element_id}"]/section/section/div[2]/section/section/div[3]' \
         f'/div/div[2]/div[1]/div[3]/div/div/div/div/div[1]/ul/li[8]'
    b3 = wait.until(EC.presence_of_element_located((By.XPATH, x3)))
    b3.click()
    time.sleep(1)
    x5 = f'//*[@id="{element_id}"]/section/section/div[2]/section/section/div[3]/div/div[3]/button/span'
    b5 = wait.until(EC.presence_of_element_located((By.XPATH, x5)))
    b5.click()
    time.sleep(230)
    x6 = f'//*[@id="writing_content"]/ul/li/div[1]/div[2]'
    tx = driver.find_element(By.XPATH, x6).text
    time.sleep(4)
    lt.append(tx)
    time.sleep(1)
   # print(lt[i])
    # 打开目标网页
    driver.get(url)
    # 使用正则表达式匹配元素ID的规律
    pattern = re.compile(r'id="([a-z0-9]{8})"')
    # 在页面源代码中查找匹配规律的元素ID
    match = pattern.search(driver.page_source)
    time.sleep(2)


# for i in range(len(list)):
#     driver.get("https://movie.douban.com/")
#     time.sleep(4)
#     driver.find_element(By.XPATH, '//*[@id="inp-query"]').send_keys(list[i])
#     time.sleep(1)
#     driver.find_element(By.XPATH, '//*[@id="db-nav-movie"]/div[1]/div/div[2]/form/fieldset/div[2]/input').click()
#     time.sleep(2)
#     driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div[1]/div[1]/div[1]/div/div[1]/a').click()
#
#     time.sleep(2)
#     img_num = 1
#     # 点击
#     driver.find_element(By.XPATH, '//*[@id="mainpic"]/a/img').click()
#     driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/ul/li[1]/div[1]').click()
#     while img_num <= 5:
#         # 获取照片
#         element = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/div[2]/div/a[1]/img')
#         img_resp = requests.get(element.get_attribute('src'))
#         with open(f'img_movie/{list[i]}' + '%d' % img_num + '.jpg', mode="wb") as f:
#             f.write(img_resp.content)  # 图片内容写入文件
#         img_num = img_num + 1
#         time.sleep(3)
#         driver.find_element(By.XPATH, '//*[@id="next_photo"]').click()
#         time.sleep(2)


for i in range(len(list)):
    # 打开创作者界面
    driver.get('https://creator.xiaohongshu.com/creator/home')
    time.sleep(4)
    driver.find_element(By.XPATH, '//*[@id="page"]/div/main/div[1]/div/div[1]/a').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="publish-container"]/div/div[1]/div[2]/span').click()
    time.sleep(3)
    # 上传图片
    for j in range(1,6):
        element = driver.find_element(By.XPATH, '//*[@id="web"]/div/div[1]/div[2]/div[1]/div/input')
        ph = f'D:\python爬虫\AI-py\img_movie\{list[i]}%d' % j + '.jpg'
        element.send_keys(ph)  # 上传文件
    time.sleep(10)
    # 标题指明
    driver.find_element(By.XPATH, '//*[@id="web"]/div/div[2]/div[2]/div[2]/input').send_keys(list[i])
    # 添加标签
    driver.find_element(By.XPATH, '//*[@id="post-textarea"]').send_keys(lt[i])
    driver.find_element(By.XPATH, '//*[@id="topicBtn"]').click()
    driver.find_element(By.XPATH, '//*[@id="post-textarea"]').send_keys(f'{list[i]}')
    driver.find_element(By.XPATH, '//*[@id="post-textarea"]').send_keys(Keys.ENTER)
    driver.find_element(By.XPATH, '//*[@id="topicBtn"]').click()
    driver.find_element(By.XPATH, '//*[@id="post-textarea"]').send_keys('豆瓣好电影推荐')
    driver.find_element(By.XPATH, '//*[@id="post-textarea"]').send_keys(Keys.ENTER)
    driver.find_element(By.XPATH, '//*[@id="topicBtn"]').click()
    driver.find_element(By.XPATH, '//*[@id="post-textarea"]').send_keys('电影影评')
    driver.find_element(By.XPATH, '//*[@id="post-textarea"]').send_keys(Keys.ENTER)
    time.sleep(2)
    # 执行js，滑动到最底部
    js_button = 'document.documentElement.scrollTop=100000'
    driver.execute_script(js_button)
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="web"]/div/div[2]/div[2]/div[7]/button[1]/span').click()
    time.sleep(2)

# 关闭浏览器
driver.quit()
