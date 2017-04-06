#!/usr/bin/python3 
import sys, os
sys.path.append(os.path.dirname(os.path.realpath(__file__))+'/components')
import random
import time

from sim_components import *


"""
This is a starter pack for a cpu scheduling project. The code / classes provided are to give you a
head start in creating the scheduling simulation. Obviously this is a simulation, so the majority
of the concepts are "simulated". For example, process "burst times" and "IO times" are known
a-priori (not so in real world). Things like memory are abstracted from addressable locations and
page tables to total "blocks" needed.
"""


###################################################################################################

# === Class: MLFQ===

class MLFQ(object):
    """Multi-Level Feedback Queue

    - Some general requirements for a MLFQ:
        - Each queue needs its own scheduling algorithm (typically Fcfs).
        - The method used to determine when to upgrade a process to a higher-priority queue.
        - The method used to determine when to demote a process to a lower-priority queue.
        - The method used to determine which queue a process will enter when that process needs
        service.

    - Rule 1: If Priority(A) > Priority(B), A runs (B doesn't).
    - Rule 2: If Priority(A) = Priority(B), A & B run in RR.
    - Rule 3: When a job enters the system, it is placed at the highest priority (the topmost
              queue).
    - Rule 4: Once a job uses up its time allotment at a given level (regardless of how many times
              it has given up the CPU), its priority is reduced (i.e., it moves down one queue).
    - Rule 5: After some time period S, move all the jobs in the system to the topmost queue.

    - **Attributes**:
        - self.num_levels
        - self.queues
    """
    def __init__(self, num_levels=2):
        self.num_levels = num_levels
        self.queues = []

        for i in range(self.num_levels):
            self.queues.append(Fcfs())

    def new(self):
        """This method admits a new process into the system.

        - **Args:**
            - None
        - **Returns:**
            - None
        """
        pass

    def __str__(self):
        """Visual dump of class state.

        - **Args:**
            - None
        - **Returns:**
            - None
        """
        return MyStr(self)

###################################################################################################

# === Class: Scheduler===

class Scheduler(object):
    """
    New:        In this status, the Process is just made or created.
    Running:    In the Running status, the Process is being executed.
    Waiting:    The process waits for an event to happen for example an input from the keyboard.
    Ready:      In this status the Process is waiting for execution in the CPU.
    Terminated: In this status the Process has finished its job and is ended.
    """
    def __init__(self, *args, **kwargs):
        self.clock = Clock()
        self.memory = Memory()                  
        self.cpu = Cpu()
        self.accounting = SystemAccounting()
        self.semaphore = SemaphorePool(num_sems=5, count=1)
        self.job_scheduling_queue = Fifo()


    def new_process(self,job_info):
        """New process entering system gets placed on the 'job_scheduling_queue'.
        - **Args**:
            - job_info (dict): Contains new job information.
        - **Returns**:
            - None
        """
        self.job_scheduling_queue.add(Process(**job_info))
        print(self.job_scheduling_queue)

    def perform_io(self,info):
        """Current process on cpu performs io
        """
        print(info)

    def sem_acquire(self,info):
        """Acquire one of the semaphores
        """
        print(info)

    def sem_release(self,info):
        """Release one of the semaphores
        """
        print(info)

###################################################################################################

# === Class: Simulator===

class Simulator(object):
    """
    Not quite sure yet
    """
    def __init__(self, **kwargs):

        # Must have input file to continue
        if 'input_file' in kwargs:
            self.input_file = kwargs['input_file']
        else:
            raise Exception("Input file needed for simulator")
        
        # Can pass a start time in to init the system clock.
        if 'start_clock' in kwargs:
            self.input_file = kwargs['start_clock']
        else:
            self.start_clock = 0

        # Read jobs in apriori from input file.
        self.jobs_dict = load_process_file(self.input_file,return_type="Dict")

        # create system clock and do a hard reset it to make sure
        # its a fresh instance. 
        self.system_clock = Clock()
        self.system_clock.hard_reset(self.start_clock)

        # Initialize all the components of the system. 
        self.scheduler = Scheduler()    
        self.memory = Memory()
        self.cpu = Cpu()
        self.accounting = SystemAccounting()

        # This dictionary holds key->value pairs where the key is the "event" from the input
        # file, and the value = the "function" to be called.
        # A = new process enters system             -> calls scheduler.new_process
        # D = Display status of simulator           -> calls display_status
        # I = Process currently on cpu performs I/O -> calls scheduler.perform_io 
        # S = Semaphore signal (release)            -> calls scheduler.sem_acquire
        # W = Semaphore wait (acquire)              -> calls scheduler.sem_release
        self.event_dispatcher = {
            'A': self.scheduler.new_process,
            'D': self.display_status,
            'I': self.scheduler.perform_io,
            'W': self.scheduler.sem_acquire,
            'S': self.scheduler.sem_release
        }


        # Start processing jobs:
        
        # While there are still jobs to be processed
        while len(self.jobs_dict) > 0:
            # Events are stored in dictionary with time as the key
            key = str(self.system_clock.current_time())
            # If current time is a key in dictionary, run that event.
            if key in self.jobs_dict.keys():
                event_data = self.jobs_dict[key]
                event_type = event_data['event']

                # Call appropriate function based on event type
                self.event_dispatcher[event_type](event_data)

                # Remove job from dictionary
                del self.jobs_dict[key]
            self.system_clock += 1

    def display_status(self,info):
        print(info)

    def __str__(self):
        """
        Visual dump of class state.
        """
        return my_str(self)


###################################################################################################
# Test Functions
###################################################################################################

def run_tests():
    print("############################################################")
    print("Running ALL tests .....\n")

    test_process_class()
    test_class_clock()
    test_cpu_class()
    test_memory_class()
    test_semaphore_class()


if __name__ == '__main__':

    file_name1 = os.path.dirname(os.path.realpath(__file__))+'/input_data/jobs_in_c.txt'
    file_name2 = os.path.dirname(os.path.realpath(__file__))+'/input_data/jobs_in_test.txt'
    S = Simulator(input_file=file_name1)


