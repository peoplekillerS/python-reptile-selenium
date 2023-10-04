#1提取单个页面的数据
#2上线程池 多个页面同时抓取
#
import requests
from lxml import etree
from concurrent.futures import  ThreadPoolExecutor

dict={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
}
def download_one_page(url):
    # 拿到页面源代码
    resp=requests.get(url,headers=dict)
    html=etree.HTML(resp.text)
    print(resp.text)
    table=html.xpath("//*[@id='bbs']/div/div/div/div[4]/div[1]/div/table")
    trs=table.xpath("./tr")
    for tr in trs:
        txt=tr.xpath("./td/text()")
        # 对数据做简单处理
        txt=(item.replace("\\","").replace("/","")for item in txt)
        print(list(txt))



    resp.close()


if __name__=='__main__':
    # for i in range(1,14870): 效率低下
    #     download_one_page("http://www.xinfadi.com.cn/getPriceData.html")

    # 创建线程池
    with ThreadPoolExecutor(50) as t:
        for i in range(1,200):
            # 下载任务交给线程池
            t.submit(download_one_page,f"http://www.xinfadi.com.cn/getPriceData.html")




