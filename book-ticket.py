from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import requests
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pickle  # 保存和读取cookie实现免登录的工具
from selenium.webdriver.support.wait import WebDriverWait
import os   # 操作文件的模块
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

# 大麦网主页
damai_url = "https://www.damai.cn/"
# 登录页
login_url = "https://passport.damai.cn/login?ru=https%3A%2F%2Fwww.damai.cn%2F"
# 抢票目标页
target_url = 'https://detail.damai.cn/item.htm?spm=a2oeg.home.card_0.ditem_1.591b23e1AELv62&id=709991612946'
# 初始化加载
class Concert:
    # 登录调用设置cookie
    def login(self):
        self.driver.get(target_url)

    def enter_concert(self):
        """打开浏览器"""
        print('###打开浏览器，进入大麦网###')
        # self.driver.maximize_window()           # 最大化窗口
        # 调用登陆
        self.login()  # 先登录再说
        self.driver.refresh()  # 刷新页面
        self.status = 2  # 登录成功标识
        print("###登录成功###")
        # 后续德云社可以讲
        if self.isElementExist('/html/body/div[2]/div[2]/div/div/div[3]/div[2]'):
            self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[3]/div[2]').click()

    def choose_ticket(self):
        if self.status == 2:  # 登录成功入口
            print("=" * 30)
            print("###开始进行日期及票价选择###")
            while self.driver.title.find('确认订单') == -1:  # 如果跳转到了订单结算界面就算这步成功了，否则继续执行此步
                try:
                    buybutton = self.driver.find_element_by_class_name('buybtn').text
                    if buybutton == "提交缺货登记":
                        # 改变现有状态
                        self.status = 2
                        self.driver.get(target_url)
                        print('###抢票未开始，刷新等待开始###')
                        continue
                    elif buybutton == "立即预定":
                        self.driver.find_element_by_class_name('buybtn').click()
                        # 改变现有状态
                        self.status = 3
                    elif buybutton == "立即购买":
                        self.driver.find_element_by_class_name('buybtn').click()
                        # 改变现有状态
                        self.status = 4
                    # 选座购买暂时无法完成自动化
                    elif buybutton == "选座购买":
                        self.driver.find_element_by_class_name('buybtn').click()
                        self.status = 5
                except:
                    print('###未跳转到订单结算界面###')
                title = self.driver.title
                if title == '选座购买':
                    # 实现选座位购买的逻辑
                    self.choice_seats()
                elif title == '确认订单':
                    while True:
                        # 如果标题为确认订单
                        print('waiting ......')
                        if self.isElementExist('//*[@id="container"]/div/div[9]/button'):
                            self.check_order()
                            break

    def choice_seats(self):
        while self.driver.title == '选座购买':
            while self.isElementExist('//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/img'):
                # 座位手动选择 选中座位之后//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/img 就会消失
                print('请快速的选择您的座位！！！')
            # 消失之后就会出现 //*[@id="app"]/div[2]/div[2]/div[2]/div
            while self.isElementExist('//*[@id="app"]/div[2]/div[2]/div[2]/div'):
                # 找到之后进行点击确认选座
                self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[2]/button').click()

    def check_order(self):
        if self.status in [3, 4, 5]:
            print('###开始确认订单###')
            try:
                # 默认选第一个购票人信息
                self.driver.find_element_by_xpath('//*[@id="container"]/div/div[2]/div[2]/div[1]/div/label').click()
            except Exception as e:
                print("###购票人信息选中失败，自行查看元素位置###")
                print(e)
            # 最后一步提交订单
            time.sleep(0.5)  # 太快会影响加载，导致按钮点击无效
            self.driver.find_element_by_xpath('//div[@class = "w1200"]//div[2]//div//div[9]//button[1]').click()

    def finish(self):
        self.driver.quit()


if __name__ == '__main__':
    try:
        con = Concert()             # 具体如果填写请查看类中的初始化函数
        con.enter_concert()         # 打开浏览器
        con.choose_ticket()         # 开始抢票

    except Exception as e:
        print(e)
        con.finish()

