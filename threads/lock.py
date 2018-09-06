import threading
import time


class NumThread (threading.Thread):
    
    thread_lock = threading.Lock()
    
    def __init__(self, name, position):
        threading.Thread.__init__(self)
        self.name = name
        self.position = position
    
    def run(self):
        number_print(self.name, self.position)


def number_print(thread_name, position):
    top_val = 100
    while position <= top_val:
        NumThread.thread_lock.acquire()
        print(thread_name + ': ' + str(position))
        position += 2
        time.sleep(0.1)
        NumThread.thread_lock.release()
        time.sleep(0.1)
        

if __name__ == '__main__':
    print ('Launched')
    
    threads = (NumThread('T1', 0),
               NumThread('T2', 1))
    
    for t in threads:
        t.start()
    for t in threads:
        t.join()
        
    print ('Finished')
 
