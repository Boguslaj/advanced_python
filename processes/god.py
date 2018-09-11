from multiprocessing import freeze_support
from multiprocessing import Lock
from multiprocessing import Process
import time


def count(num, key):
    while num <= 100:
        key.acquire()
        print(str(num))
        num += 2
        key.release()
        time.sleep(1)


if __name__ == '__main__':
    freeze_support()
    sceleton_key = Lock()
    proc_even = Process(target=count, args=(0, sceleton_key,))
    proc_odd = Process(target=count, args=(1, sceleton_key,))

    proc_even.start()
    time.sleep(0.5)
    proc_odd.start()
