import os
from concurrent.futures import ProcessPoolExecutor

import time


def eating():
    pid = os.getpid()
    ppid = os.getppid()
    print(f"在吃饭。。。,pid:{pid} ppid:{ppid}")
    time.sleep(3)

def play_phone():
    pid = os.getpid()
    ppid = os.getppid()
    print(f"在玩手机。。。,pid:{pid} ppid:{ppid}")
    time.sleep(3)


if __name__ == '__main__':
    start_time = time.time()
    # eating()
    # play_phone()

    process_pool = ProcessPoolExecutor(max_workers=2)
    process_pool.submit(eating)
    process_pool.submit(play_phone)

    end_time = time.time()
    print(f"总共耗时：{int(end_time - start_time)}秒")