# https://boxnovel.baidu.com/boxnovel/wiseapi/chapterList?bookid=4306063500&pageNum=1&order=asc&site=
# https://boxnovel.baidu.com/boxnovel/content?gid=4306063500&data=%7B%22fromaction%22%3A%22dushu%22,%22fromaction_original%22%3A%22dushu%22%7D&cid=1569782244
import json
import aiofiles
import requests
import asyncio
import aiohttp


async def aiodownload(cid, b_id, title):
    data = {
        "book_id": "b_id",
        "cid": f"{b_id}|{cid}",
        "need_bookinfo": 1
    }
    data = json.dumps(data)
    url = f"http://dushu.baidu.com/api/pc/getChapterContent?data={data}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            dic = await resp.json()
            async with aiofiles.open(title, mode="w", encoding="utf-8") as f:
                await f.write(dic['data']['novel']['content'])


async def getCatalog(url):
    resp = requests.get(url)
    dic = resp.json()
    tasks = []
    for item in dic['data']['novel']['items']:  # item就是对应每一个章节的名称和cid
        title = item['title']
        cid = item['cid']
        # 准备异步任务
        tasks.append(asyncio.create_task(aiodownload(cid, b_id, title)))
        # print(cid,title)
    await asyncio.wait(tasks)


if __name__ == '__main__':
    b_id = "4306063500"
    url = 'http://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"' + b_id + '"}'
    asyncio.run(getCatalog(url))
