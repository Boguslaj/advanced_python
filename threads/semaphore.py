from threading import Thread, Semaphore
import time


num_list = [i for i in range(0,101)]
num_list.reverse()


def print_even(es, os):
    while len(num_list) > 0:
        es.acquire()
        n = num_list.pop()
        print('e ' + str(n))
        os.release()


def print_odd(es, os):
    while 1:
        os.acquire()
        if not num_list:
            break
        n = num_list.pop()
        print('o ' + str(n))
        es.release()


if __name__ == '__main__':
    even_sem = Semaphore(1)
    odd_sem = Semaphore(0)

    ev = Thread(name='even', target=print_even, args=(even_sem, odd_sem))
    od = Thread(name='odd', target=print_odd, args=(even_sem, odd_sem))

    ev.start()
    time.sleep(0.1)
    od.start()
