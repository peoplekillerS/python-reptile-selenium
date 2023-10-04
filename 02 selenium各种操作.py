import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


web=Chrome()

web.get("http://lagou.com")
el1=web.find_element(By.XPATH,'//*[@id="changeCityBox"]/p[1]/a')
# 找到某个元素 点击时间
el1.click()

# 找到输入框框 输入python ==>输入回车
web.find_element(By.XPATH,'//*[@id="search_input"]').send_keys("python",Keys.ENTER)

li_list = web.find_elements(By.XPATH,'//*[@id="jobList"]/div[1]/div')
for li in li_list:
    job_name= li.find_element(By.XPATH, './div/div/div[1]/a').text
    job_price=li.find_element(By.XPATH,'./div/div/div[2]/span').text
    company_name = li.find_element(By.XPATH,'./div/div[3]/img').text
    print(company_name,job_name,job_price)














