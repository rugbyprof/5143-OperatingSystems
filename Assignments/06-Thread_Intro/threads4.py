'''
    threads4.py
    Jeff Ondich, 14 November 2013

    Threading example like threads2.py, but with a more explicit race condition.
'''

import threading

sharedNumber = 0

class ThreadClassA (threading.Thread):
    def __init__(self, lock):
        threading.Thread.__init__(self)
        self.lock = lock

    def run(self):
        global sharedNumber
        for k in xrange(10000000):
            #self.lock.acquire()
            sharedNumber = 1
            if sharedNumber != 1:
                print 'A: that was weird'
            #self.lock.release()
        print 'Goodbye from thread A'

class ThreadClassB (threading.Thread):
    def __init__(self, lock):
        threading.Thread.__init__(self)
        self.lock = lock

    def run(self):
        global sharedNumber
        for k in xrange(10000000):
            #self.lock.acquire()
            sharedNumber = 2
            if sharedNumber != 2:
                print 'B: that was weird'
            #self.lock.release()
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

