import multiprocessing
import os

import time


# 任务： 需要完成的事情

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

    eat_process = multiprocessing.Process(target=eating)
    play_phone_process = multiprocessing.Process(target=play_phone)
    eat_process.start()
    play_phone_process.start()
    eat_process.join()
    play_phone_process.join()

    end_time = time.time()
    print(f"总共耗时：{int(end_time - start_time)}秒")