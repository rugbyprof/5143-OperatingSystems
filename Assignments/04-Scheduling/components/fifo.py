#!/usr/bin/env python3
from sim_components import *



# === Class: FCFS===

class Fifo(list):
    def __init__(self,init=[]):
        """***init***: Constructor for FCFS class.

        - **Args:**
            - init (list): A possible list of processes to be added to class. 
        - **Returns:**
            - None
        """
        self.Q = []
        if len(init) > 0:
            for i in init:
                self.add(i)

    def add(self,proc):
        """***add***: Add process to rear of queue.

        - **Args:**
            - proc (Process): Process to be added to queue
        - **Returns:**
            - None
        """

        if not isinstance(proc,Process):
            raise Exception("Queue requires items added to be of type 'Process'")
        self.Q.append(proc)

    def remove(self):
        """***remove***: Returns first item in the queue.

        - **Args:**
            - None
        - **Returns:**
            - (Process): Process removed from queue
        """
        return self.Q.pop(0)

    def empty(self):
        """***empty***: Boolean test if queue empty.

        - **Args:**
            - None
        - **Returns:**
            - (Bool): True if queue empty False otherwise.
        """
        return len(self.Q) == 0

    def first(self,key=None):
        """***first***: Copy of first item in the queue.

        Returns a process that is a copy (reference to) the first 
        process in the queue without altering the queue. If a key 
        is present, it will return the value of that key. 

        - **Args:**
            - key (string) : Key of value to be returned
        - **Returns:**
            - (mixed,Process): A copy of the first process in the queue, or a value 
                               from the first process in the queue. 
        """
        if key is None:
            return self.Q[0]
        else:
            return self.Q[0][key]            

    def last(self,key=None):
        """***last***: Copy of last item in the queue.

        Returns a process that is a copy (reference to) the last 
        process in the queue without altering the queue. If a key 
        is present, it will return the value of that key. 

        - **Args:**
            - key (string) : Key of value to be returned
        - **Returns:**
            - (mixed,Process): A copy of the last process in the queue, or a value 
                               from the last process in the queue. 
        """
        if key is None:
            return self.Q[-1]
        else:
            return self.Q[-1][key]   

    def __str__(self):
        """***str***: Visual dump of class state.

        - **Args:**
            - None
        - **Returns:**
            - None
        """
        return my_str(self)

    def __iter__(self):
        """***iter***: Creates an "iterator" so this class can act like a container class.

        - **Args:**
            - None
        - **Yields:**
            - A generator which can be used to iterate over.
        """
        for elem in self.Q:
            yield elem

if __name__=='__main__':
    pass
