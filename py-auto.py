import time
import selenium
from selenium import driver
from selenium.driver.common.by import By
from selenium.driver.support.ui import DriverWait
from selenium.driver.support import expected_conditions as EC
from selenium.driver.common.keys import Keys
import re

url = "https://copyai.cn/creativestage"
# 设置Chrome浏览器选项
options = driver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
options.add_argument('--remote-debugging-port=9527')
options.add_experimental_option("debuggerAddress", "127.0.0.1:9527")

# 实例化浏览器驱动
driver = driver.Chrome(options=options)
# 打开目标网页
driver.get(url)

# 使用正则表达式匹配元素ID的规律
pattern = re.compile(r'id="([a-z0-9]{8})"')
# 在页面源代码中查找匹配规律的元素ID
match = pattern.search(driver.page_source)

list = ["千与千寻", "盗梦空间", "楚门的世界", "星际穿越", "三杀大闹好莱坞", "忠犬八公的故事", "海上钢琴师","机器人总动员","疯狂动物城","熔炉","触不可及"]
lt = []

driver.get("https://chat.forchange.cn/")
time.sleep(1)
oo=1
for i in list:

    time.sleep(1)
    space = driver.find_element(By.XPATH, '//*[@id="AI-EDU"]/div/div[1]/main/div[2]/form/div/div[2]/textarea')
    space.clear()
    space.send_keys("帮我写一下经典电影《" + i + "》的影评，要求500字")
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="AI-EDU"]/div/div[1]/main/div[2]/form/div/div[2]/button').click()
    time.sleep(50)
    pth='//*[@id="AI-EDU"]/div/div[1]/main/div[1]/div/div/div/div['+ '%d' % (2 * oo) + ']/div/div[2]/div/p'
    # print(pth)
    tx = driver.find_element(By.XPATH,pth).text
    lt.append(tx)
    time.sleep(2)
    oo = oo+1

j = 0
time.sleep(2)






for i in range(len(list)):
    # 找到第一个匹配的元素ID，并生成对应的XPath和CSS Selector
    element_id = match.group(1)
    xpath = f'//*[@id="{element_id}"]/section/div[1]/div/button'
    css_selector = f'#{element_id} > section > div.arco-layout-sider.arco-layout-sider-light > div > button'
    # 使用DriverWait等待元素加载完成
    wait = DriverWait(driver, 5)
    # 使用XPath定位元素
    button = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    # 点击按钮
    button.click()
    time.sleep(3)
    x1=f'//*[@id="{element_id}"]/section/section/div[2]/section/section/div[3]/div/div[2]/div[2]/div[2]/textarea'
    b1=wait.until(EC.presence_of_element_located((By.XPATH, x1)))
    b1.send_keys(f'通过对其中人物形象，并用上剧中的台词，来对{list[i]}这部电影做出有强烈文艺感的影评,要求800字')
    x2=f'//*[@id="{element_id}"]/section/section/div[2]/section/section/div[3]/div/div[2]/div[5]/span/input'
    time.sleep(1)
    b2 = wait.until(EC.presence_of_element_located((By.XPATH, x2)))
    b2.click()
    time.sleep(1)
    x3=f'//*[@id="{element_id}"]/section/section/div[2]/section/section/div[3]/div/div[2]/div[1]/div[' \
       f'4]/div/div/div/div/div/ul/li[4]'
    b3 = wait.until(EC.presence_of_element_located((By.XPATH, x3)))
    b3.click()
    x4=f'//*[@id="{element_id}"]/section/section/div[2]/section/section/div[3]/div/div[2]/div[6]/span/span[2]/input'
    b4 = wait.until(EC.presence_of_element_located((By.XPATH, x4)))
    for ii in range(8):
         b4.send_keys(Keys.BACK_SPACE)
    b4.send_keys('豆瓣top电影',Keys.ENTER)
    b4.send_keys(f'{list[i]}',Keys.ENTER)
    time.sleep(1)
    x5=f'//*[@id="{element_id}"]/section/section/div[2]/section/section/div[3]/div/div[3]/button'
    b5 = wait.until(EC.presence_of_element_located((By.XPATH, x5)))
    b5.click()
    x6=f'//*[@id="writing_HpSGtEwv"]/span'
    time.sleep(100)
    tx = driver.find_element(By.XPATH,x6).text
    lt.append(tx)
    print(lt[0])
    driver = driver.Chrome(options=options)
    # 打开目标网页
    driver.get(url)
    # 使用正则表达式匹配元素ID的规律
    pattern = re.compile(r'id="([a-z0-9]{8})"')
    # 在页面源代码中查找匹配规律的元素ID
    match = pattern.search(driver.page_source)






for i in list:
    k = 19
    driver.get('https://creator.xiaohongshu.com/creator/home')
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="page"]/div/main/div[1]/div/div[1]/a').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="publish-container"]/div/div[1]/div[2]/span').click()
    time.sleep(3)
    element = driver.find_element(By.XPATH, '//*[@id=""]/div/div[1]/div[2]/div[1]/div/input')  # 定位到上传文件框
    ph=r'D:\python爬虫\第五章\img_movie\%d' % j + '.jpg'
    element.send_keys(ph)  # 上传文件
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id=""]/div/div[2]/div[2]/div[2]/input').send_keys(
        '分享100部好电影---第' + '%d' % k + '部:' + i)
    driver.find_element(By.XPATH, '//*[@id="post-textarea"]').send_keys(lt[j])
    driver.find_element(By.XPATH, '//*[@id="post-textarea"]').send_keys('#豆瓣好电影推荐#好看电影推荐')
    time.sleep(2)

    j = j + 1
    # 执行js，滑动到最底部
    js_button = 'document.documentElement.scrollTop=100000'
    driver.execute_script(js_button)
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id=""]/div/div[2]/div[2]/div[7]/button[1]/span').click()
    time.sleep(2)






# 关闭浏览器
driver.quit()
