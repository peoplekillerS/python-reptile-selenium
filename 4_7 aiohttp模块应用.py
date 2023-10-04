# request.get() 同步的代码-》异步操作 aiohttp
#
import aiohttp
import asyncio

urls = [
    "http://kr.shanghai-jiuxin.com/file/2020/0902/d1a98285ac8bb2f4c36f0021ef917911.jpg",
    "http://kr.shanghai-jiuxin.com/file/2020/1031/191468637cab2f0206f7d1d9b175ac81.jpg",
    "http://kr.shanghai-jiuxin.com/file/2020/1031/774218be86d832f359637ab120eba52d.jpg"
]


async def aiodownload(url):
    # with open("cba.csv",) as f:
    #     f.write()
    name = url.rsplit("/", 1)[1]
    async with aiohttp.ClientSession() as session:  # 相当于request
        async with session.get(url) as resp:  # resp=request。get()
            # 请求回来了 写入文件
            # 可以自己去学习一个模块 aiofiles
            with open(name, mode="wb") as f:  # 创建文件
                f.write(await resp.content.read())  # 读取内容是异步的 所以要挂起来
    print(name, "搞定")


async def main():
    tasks = []
    for url in urls:
        tasks.append(asyncio.create_task(aiodownload(url)))
    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())
