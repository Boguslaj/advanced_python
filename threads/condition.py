import threading
import time


def even_c(ev, od):
    val = 0
    with ev:
        ev.wait()
        while val <= 100:
            print(str(val))
            val += 2
            time.sleep(0.5)
            with od:
                od.notifyAll()
            if val <= 100:
                ev.wait()


def odd_c(ev, od):
    val = 1
    with od:
        od.wait()
        while val < 100:
            print(str(val))
            val += 2
            time.sleep(0.5)
            with ev:
                ev.notifyAll()
            if val < 100:
                od.wait()


def launch(cv):
    with cv:
        cv.notifyAll()


if __name__ == '__main__':
    condition_e = threading.Condition()
    condition_o = threading.Condition()

    cs1 = threading.Thread(name='even', target=even_c, 
                           args=(condition_e, condition_o,))
    cs2 = threading.Thread(name='odd', target=odd_c, 
                           args=(condition_e, condition_o,))
    launcher = threading.Thread(name='Launch', 
                                target=launch, args=(condition_e,))

    cs1.start()
    time.sleep(0.1)
    cs2.start()
    time.sleep(0.1)
    launcher.start()
