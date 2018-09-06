from threading import Thread
from threading import Timer
import time


class TimerThread(Thread):

    def __init__(self, timer, function, position):
        Thread.__init__(self)
        self.timer = timer
        self.function = function
        self.position = position
        self.thread = Timer(self.timer, self.run_function)

    def run_function(self):
        if self.position <= 100:
            self.function(self.position)
            self.position += 2
            self.thread = Timer(self.timer, self.run_function)
            self.thread.start()
        else:
            self.cancel()

    def start(self):
        self.thread.start()

    def cancel(self):
        self.thread.cancel()


def number_print(position):
    print(str(position))


if __name__ == '__main__':
    t1 = TimerThread(5, number_print, 0)
    t2 = TimerThread(5, number_print, 1)

    t1.start()
    time.sleep(2.5)
    t2.start()
