# https://api.tinga88.com/?url=https://vip.lz-cdn9.com/20220513/9183_1cb47ae3/index.m3u8
import requests
import aiohttp
import aiofiles
import  asyncio
import os

str = "https://vip.lz-cdn9.com/20220513/9183_1cb47ae3/1000k/hls/"
def download_m3u8_file(url, name):
    resp=requests.get(url)
    with open(name,mode="wb") as f:
        f.write(resp.content)

async def download_ts(url,name,session):
    async with session.get(url) as resp:
        async with aiofiles.open(f"video2/{name}",mode="wb") as f:
            await f.write(await resp.content.read()) # 把下载的文件写入文件

    print(f"{name}下载完毕")


async def aio_download(str):
    tasks=[]
    async with aiohttp.ClientSession() as session: # 提前准备好session 传过去
        async with aiofiles.open("越狱第一集——first_m3u8.txt",mode="r",encoding='utf-8') as f:
            async for line in f:
                if line.startswith("#"):
                    continue
                # line就是xxxx。ts
                line=line.strip() # 去掉没有的空格和换行
                # 拼接真正的ts路径
                ts_url= str + line
                task = asyncio.create_task(download_ts(ts_url,line,session))
                tasks.append(task)

        await  asyncio.wait(tasks) #等待任务结束


def merge_ts():
    # mac:cat 1.ts 2.ts 3.ts > xxx.mp4
    # windows:copy /b 1.ts+2.ts+3.ts xxx.mp4
    list = []
    with open("越狱第一集——first_m3u8.txt",mode="r",encoding="utf-8") as f:
        for line in f:
            if line.startswith("#"):
                continue
            line = line.strip()
            list.append(f"video2/{line}")
    s=" ".join(list) # 1.ts 2.ts 3.ts
    os.system(f"copy /b {s} > movie.mp4")
    print("搞定！")

def main(url):
    # asyncio.run(aio_download(str))
    merge_ts()



if __name__ == '__main__':
    url = "https://vip.lz-cdn9.com/20220513/9183_1cb47ae3/1000k/hls/mixed.m3u8"
    main(url)
