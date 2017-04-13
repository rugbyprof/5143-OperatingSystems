#!/usr/bin/env python3
import random
from sim_components import *


# === Class: Process===

class Process(object):
    """Represents a single process.
    - Classes:

        Pcb              : Process Control Block Included in process class
        SystemAccounting : Accounting class

    - Methods:

        __str__    : Prints a string representation of the object
        __setitem__: Allows user to use [] to set a value within the object.
                     (e.g. p1['priority'] = 2)
        __getitem__: Allows user to use [] to get a value from an object.

    - **Attributes**:
        - burst_time      (int)   : CPU Burst time
        - io_status_info  (list)  : This includes a list of I/O devices allocated to the process.
        - mem_required    (int)   : Total memory required (in blocks)
        - priority        (int)   : Priority of process
        - process_id      (int)   : Unique identification for each of the process in the operating
                                    system.
        - state           (enum)  : The current state of the process [New, Ready, Running,
                                                                      Waiting, Terminated]

    """

    def __init__(self, **kwargs):
        """
        Params: (dict)
            kwargs should contain everyting it the attributes list above.
        """
        #print(kwargs)
        # Either pid or process_id need be present in kwargs otherwise, error
        if 'process_id' not in kwargs and 'pid' not in kwargs:
            raise Exception("Need a process id to initialize a process!")

        # if pid is the arg, then set process_id (preferred arg)
        if 'pid' in kwargs:
            kwargs['process_id'] = kwargs['pid']


        self.state = 'New'                                # All new processes are in the 'New' state
        self.io_status_info = []                          # No IO devices are allocated
        self.acct = Accounting()                          # Instance of an Accounting Block
        self.mem_required = 0
        self.burst_time = 0
        self.priority = 0
        self.process_id = 0

        if 'priority' in kwargs:
            self.priority = kwargs['priority']
        if 'mem_required' in kwargs:
            self.mem_required = kwargs['mem_required']
        if 'burst_time' in kwargs:
            self.burst_time = kwargs['burst_time']
        if 'num_bursts' in kwargs:
            self.num_bursts = kwargs['num_bursts']
        if 'priority' in kwargs:
            self.priority = kwargs['priority']
        if 'process_id' in kwargs:
            self.process_id = kwargs['process_id']


    def __setitem__(self, key, val):
        """
        "setitem" allows the '[]' brackets to be used to set a data member. I used this as a
        shortcut to access the many data members used by this class, especially since it is
        composed of a 'Pcb' and 'Accounting' class.
        """
        if hasattr(self, key):
            setattr(self, key, val)
        elif hasattr(self.acct, key):
            setattr(self.acct, key, val)
        else:
            setattr(self, key, val)

    def __getitem__(self, key):
        if hasattr(self, key):
            return getattr(self, key)
        elif hasattr(self.acct, key):
            return getattr(self.acct, key)
        else:
            return None

    def __str__(self):
        """
        Visual dump of class state.
        """
        return "[process_id: %s, state: %s, io_status_info: %s, mem_required: %s, burst_time: %s, priority: %s]" % (self.process_id,
                                                                              self.state,
                                                                              self.io_status_info,
                                                                              self.mem_required,
                                                                              self.burst_time,
                                                                              self.priority)

def test_process_class():
    """Run tests for Process class.
    """
    processes = load_process_file(os.path.dirname(os.path.realpath(__file__))+'/../input_data/processes.txt')
    for i in range(len(processes)):
        processes[i] = Process(**processes[i])

    print("Running Process class test.....\n")

    for p in processes:
        print(p)
        print('Get process state:',p['state'])
        print('Get mem_required:',p['mem_required'])
        print('Get some unknown value:',p['unkownn'])
        print("==================================\n")

    

if __name__ == '__main__':
    test_process_class()
