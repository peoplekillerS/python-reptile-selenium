from selenium.webdriver import Chrome, Keys
import time

from selenium.webdriver.common.by import By

web = Chrome()
web.get("http://lagou.com")

web.find_element(By.XPATH,'//*[@id="changeCityBox"]/p[1]/a').click()

web.find_element(By.XPATH,'//*[@id="search_input"]').send_keys("python",Keys.ENTER)

web.find_element(By.XPATH,'//*[@id="jobList"]/div[1]/div[1]/div[1]/div[1]/div[1]/a').click()

# 如何导入新窗口
# 注意，在selenium眼中 新窗口默认是不切换过来的
web.switch_to.window(web.window_handles[-1]) # -1就是最后一个

# 在新窗口中提取内容
job_detail=web.find_element(By.XPATH,'//*[@id="job_detail"]/dd[2]/div').text
print(job_detail)

# 关闭子窗口
web.close()
# 变更selenium的窗口视角 回到原来的窗口
web.switch_to.window(web.window_handles[0])


# 如果页面遇到了 iframe怎么处理
web.get("https://www.97dsja.com/p/45652-2-1.html")

iframe=web.find_element(By.XPATH,'//*[@id="playleft"]/iframe')
web.switch_to.frame(iframe)
web.switch_to.default_content() # 切回原来的页面




