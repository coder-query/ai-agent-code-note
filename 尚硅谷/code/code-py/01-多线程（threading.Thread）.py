import  threading
import time


# 任务： 需要完成的事情

def eating():
    print("在吃饭。。。")
    time.sleep(3)

def play_phone():
    print("在玩手机。。。")
    time.sleep(3)

def main():
    start_time = time.time()
    # eating()
    # play_phone()

    eating_task =  threading.Thread(target=eating)
    play_phone_task = threading.Thread(target=play_phone)
    eating_task.start()
    play_phone_task.start()
    eating_task.join()
    play_phone_task.join()


    end_time = time.time()
    print(f"总共耗时：{int(end_time - start_time)}秒")

if __name__ == '__main__':
    main()