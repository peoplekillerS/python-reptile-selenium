import time
import asyncio


#
# def func():
#     print("我爱黎明")
#     time.sleep(3)  # 让当前线程处于足鳃状态 CPU不是为我工作的
#     print("我真的爱黎明")
#
#
# if __name__ == '__main__':
#     func()


# input() 也是线程阻塞
# request。get（bilibili） 在网络请求返回数据之前 程序也是处于阻塞状态
# 一般情况下。当程序处于 io操作的时候 线程都会处于阻塞状态

# 协程：当程序遇到了IO操作 可以选择性的切换到其他任务上
# 在微观上是一个任务一个任务的进行切换，切换条件一般就是IO操作
# 多任务异步操作

# 上方所讲的一切，都是单线程的条件下

# async def func():
#     print("你好啊 我是千石")
#
#
# if __name__ == '__main__':
#     g=func() # 此时的函数是异步协程函数，此时函数执行得到的是一个协程对象
#     # print(g)
#     asyncio.run(g) # 协程程序运行需要asyncio模块支持
#
#
# async def func1():
#     print("你好啊 猪大肠")
#     # time.sleep(3) # 当程序出现了同步操作的时候 异步就中断了
#     await asyncio.sleep(3) # 异步操作代码
#     print("你好啊 猪大肠")
# async def func2():
#     print("你好啊 猪小肠")
#     # time.sleep(2)
#     await asyncio.sleep(2) # 异步操作代码
#     print("你好啊 猪小肠")
# async def func3():
#     print("你好啊 猪腰子")
#     # time.sleep(4)
#     await asyncio.sleep(4) # 异步操作代码
#     print("你好啊 猪腰子")
#
# # if __name__ == '__main__':
# #     f1=func1()
# #     f2=func2()
# #     f3=func3()
# #     tasks={
# #         f1,f2,f3
# #     }
# #     t1 = time.time()
# #     # 一次性启动多个任务（协程）
# #     asyncio.run(asyncio.wait(tasks))
# #     t2 = time.time()
# #     print(t2-t1)
#
# async def main():
#     # 第一种写法
#     # f1= func1()
#     # await f1 #  一般await挂起操作放在协程对象前面
#     # 第二种写法
#     tasks={
#         func1(),
#         func2(),
#         func3()
#     }
#     await asyncio.wait(tasks)
#
#
# if __name__ == '__main__':
#     t1 = time.time()
#     # 一次性启动多个任务（协程）
#     asyncio.run(main())
#     t2 = time.time()
#     print(t2 - t1)
#

# 在爬虫中运用
async def download(url):
    print("准备开始下载")
    await asyncio.sleep(2)  # 网络请求
    print("下载完成")


async def main():
    urls = [
        "http://www.baidu.com",
        "http://www.bilibili.com",
        "http://www.163.com"
    ]
    task = []
    for url in urls:
        d = download(url)
        task.append(asyncio.create_task(d))


if __name__ == '__main__':
    asyncio.run(main())
