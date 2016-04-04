'''
    threads1.py
    Jeff Ondich, 14 November 2013

    A simple example of threading for an in-class lab exercise.
'''

import threading

class ThreadClassA (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        for k in xrange(10000000):
            if k % 100000 == 0:
                print 'A:', k
        print 'Goodbye from thread A'

class ThreadClassB (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        for k in xrange(10000000):
            if k % 100000 == 0:
                print 'B:', k
        print 'Goodbye from thread B'

threadA = ThreadClassA()
threadB = ThreadClassB()

threadA.start()
threadB.start()

print 'Hello from the main program'

threadA.join()
threadB.join()

print 'Goodbye from the main program'

