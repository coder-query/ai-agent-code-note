import asyncio
import time
from turtledemo.penrose import start


async def do_task(str):
    print(f"开始执行任务{str}")
    time.sleep(1)
    print(f"任务{str}执行完成")

async def main():
    start_time = time.time()
    str_list = [
        "----------任务集合list01",
        "----------任务集合list02"
        "----------任务集合list03"
    ]
    async_tasks = [asyncio.create_task(do_task(s)) for s in str_list]
    await asyncio.gather(*async_tasks)
    end_time = time.time()
    print(f"总共耗时：{int(end_time - start_time)}秒")

if __name__ == '__main__':
    asyncio.run(main())