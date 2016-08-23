'''
    threads2.py
    Jeff Ondich, 14 November 2013

    Threading example like threads1.py, but with a shared variable.
'''

import threading

sharedCounter = 0

class ThreadClassA (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global sharedCounter
        for k in xrange(10000000):
            if k % 100000 == 0:
                print 'A:', k, sharedCounter
            sharedCounter += 1
        print 'Goodbye from thread A'

class ThreadClassB (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global sharedCounter
        for k in xrange(10000000):
            if k % 100000 == 0:
                print 'B:', k, sharedCounter
            sharedCounter += 1
        print 'Goodbye from thread B'

threadA = ThreadClassA()
threadB = ThreadClassB()

threadA.start()
threadB.start()

print 'Hello from the main program'

threadA.join()
threadB.join()

print 'Goodbye from the main program'

