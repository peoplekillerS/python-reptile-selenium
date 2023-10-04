from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
# 设置Chrome浏览器选项
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
options.add_argument('--remote-debugging-port=9527')
options.add_experimental_option("debuggerAddress", "127.0.0.1:9527")

# 实例化浏览器驱动
driver = webdriver.Chrome(options=options)

# 打开网页
driver.get("https://chat.openai.com/chat")
time.sleep(10)

# 绕过人机检验
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
driver.execute_script("window.navigator.chrome = {runtime: {},  };")
driver.execute_script("window.navigator.userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'")
driver.execute_script("window.navigator.languages = ['en-US', 'en']")

# 定位到问题输入框
input_box = driver.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div[2]/main/div[2]/form/div/div[2]/textarea')

# 预设问题列表
questions = ["请从专业的电影艺术家的角度，通过对其中人物形象和拍摄手法，人物特征，并用上许多成语和剧中的台词，来对霸王别姬这部电影做出有强烈文艺感的影评", "你是谁", "你喜欢什么颜色", "你的工作是什么"]

# 循环遍历问题列表并发送
for question in questions:
    # 输入问题
    input_box.send_keys(question)
    time.sleep(2)

    # 提交问题
    submit_button = driver.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div[2]/main/div[2]/form/div/div[2]/button')
    submit_button.click()
    time.sleep(150)

    # 定位到回答元素并获取文本
    response_element = driver.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div[2]/main/div[1]/div/div/div/div['
                                                    '2]/div/div[2]/div[1]/div/div')
    response_text = response_element.text
                                                    #'//*[@id="__next"]/div[2]/div[2]/main/div[1]/div/div/div/div[4]/div/div[2]/div[1]/div/div'
    # 打印回答
    print(f"Question: {question}")
    print(f"Response: {response_text}")
    print("=" * 50)

    # 将对话记录写入文件
    with open("ChatGPT对话记录.txt", "a", encoding="utf-8") as f:
        f.write(f"Question: {question}\n")
        f.write(f"Response: {response_text}\n")
        f.write("=" * 50 + "\n")

    # 清空输入框
    input_box.clear()

# 关闭浏览器驱动
driver.quit()
