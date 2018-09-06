import threading
import time


def magick(ev):
    ev.set()


def even(e, o):
    i = 0
    while i <= 100:
        while not e.is_set():
            print_even.wait(0.1)
        print(str(i))
        i += 2
        e.clear()
        magick(o)


def odd(e, o):
    i = 1
    while i < 100:
        while not o.is_set():
            print_odd.wait(0.1)
        print(str(i))
        i += 2
        o.clear()
        magick(e)


if __name__ == '__main__':
    print_even = threading.Event()
    print_odd = threading.Event()

    ev = threading.Thread(name='even', target=even,
                          args=(print_even, print_odd,))
    od = threading.Thread(name='odd', target=odd,
                          args=(print_even, print_odd,))

    magick(print_even)
    ev.start()
    time.sleep(0.1)
    od.start()
