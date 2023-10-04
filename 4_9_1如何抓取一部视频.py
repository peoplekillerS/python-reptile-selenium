#  用户上传 转码 然后弄成切片 ts
# 需要一个文件记录：1、视频播放路径 2视频播放顺序
# M3U8 txt json =》 文本
# 想要抓取一个视频
# 1、找到M3U8
# 2通过M3U8下载到ts文件
# 3、可以通过各种手段（不仅是编程手段）把ts文件合并为一个MP4文件
import requests
import re
# # http://www.91kanju.com/vod-play/54812-1-1.html
#
# obj =re.compile(r"url:'(?P<url>.*?)',",re.S)
# url = "https://www.97dsja.com/p/45652-2-1.html"
# resp=requests.get(url)
# # m3u8_url=obj.search(resp.text).group("url")
# m3u8_url = "https://vip.lzcdn2.com/20220705/14737_57b40aac/1200k/hls/mixed.m3u8"
# resp.close()
#
# resp2 = requests.get(m3u8_url)
# with open("哲仁王后.m3u8",mode="wb") as f:
#     f.write(resp2.content)
#
# resp2.close()
# print("下载完毕")
n=1
with open("哲仁王后.m3u8",mode="r",encoding="utf-8") as f:
    for line in f:
        line=line.strip()# 先去掉空格，空白，换行符
        if line.startswith("#"): # 如果以#开头 我不要
            continue
        # print(line)

        # 下载视频片段
        url2= "https://vip.lzcdn2.com/20220705/14737_57b40aac/1200k/hls/"
        url3=url2+line
        resp3 = requests.get(url3)
        f = open(f"video/{n}.ts",mode="wb")
        f.write(resp3.content)
        f.close()
        resp3.close()
        n+=1
        print(f"完成了{n}")






















