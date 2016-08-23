'''
    threads3.py
    Jeff Ondich, 14 November 2013

    Threading example like threads1.py, with a shared variable and a lock.
'''

import threading

sharedCounter = 0

class ThreadClassA (threading.Thread):
    def __init__(self, lock):
        threading.Thread.__init__(self)
        self.lock = lock

    def run(self):
        global sharedCounter
        for k in xrange(10000000):
            self.lock.acquire()
            if k % 100000 == 0:
                print 'A:', k, sharedCounter
            sharedCounter += 1
            self.lock.release()
        print 'Goodbye from thread A'

class ThreadClassB (threading.Thread):
    def __init__(self, lock):
        threading.Thread.__init__(self)
        self.lock = lock

    def run(self):
        global sharedCounter
        for k in xrange(10000000):
            self.lock.acquire()
            if k % 100000 == 0:
                print 'B:', k, sharedCounter
            sharedCounter += 1
            self.lock.release()
        print 'Goodbye from thread B'

lockForSharedCounter = threading.Lock()
threadA = ThreadClassA(lockForSharedCounter)
threadB = ThreadClassB(lockForSharedCounter)

threadA.start()
threadB.start()

print 'Hello from the main program'

threadA.join()
threadB.join()

print 'Goodbye from the main program'

