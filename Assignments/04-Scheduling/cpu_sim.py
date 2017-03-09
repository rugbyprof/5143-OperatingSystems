"""
THIS CODE IS NOT COMPLETE!!!!!
This is a starter pack for a cpu scheduling project. The code / classes provided are to give you a head start
in creating the scheduling simulation. Obviously this is a simulation, so some of the concepts are "simulated".
For example, process "burst times" and "IO times" are known a-priori (not so in real world). Things like "memory
info" are abstracted to total "blocks" needed, instead of addresses, page tables and such. 
"""

"""
Cheater global design pattern so we can globally assign
process id's 
"""
class pid:pass

class Cpu(object):
    def __init__(self):
        pass

class Memory(object):
    def __init__(self):
        pass

class Accounting(object):
    def __init__(self):
        self.total_burst_time = 0
        self.turnaround_time = 0

class Pcb(object):
    """
    process_id       (int)  - Unique identification for each of the process in the operating system. 
    Process State    (enum) - The current state of the process [New, Ready, Running, Waiting, Terminated] .
    process_priority       - This is required to allow/disallow access to system resources.
    IO_status_info         - This includes a list of I/O devices allocated to the process.
    accounting_info        - This includes the amount of CPU used for process execution, time limits, execution ID etc.
    memory_info            - Memory requirements (in blocks) for the process. 

    *** Not Used***
    Pointer                       - A pointer to parent process.
    Program Counter               - Program Counter is a pointer to the address of the next instruction to be executed for this process.
    CPU registers                 - Various CPU registers where process need to be stored for execution for running state.
    CPU Scheduling Information    - Process priority and other scheduling information which is required to schedule the process.
    Memory management information - This includes the information of page table, memory limits, Segment table depending on memory used by the operating system.
    """

    pid.val = 0

    def __init__(self,*args, **kwargs):
        self.state = 'New'                  # All new processes are in the 'New' state
        self.IO_status_info = []                    # No IO devices are allocated 

        if 'pid' in kwargs:
            self.pid = kwargs['pid']  # Int value, if not present, one will be created
        else:
            self.pid = pid.val 
            pid.val += 1

        if 'priority' in kwargs:
            self.priority = kwargs['priority']

    def __str__(self):
        return "[Pid: %d, State: %s, IOstat: %s, Priority: %d]" % (self.pid,self.state,self.IO_status_info,self.priority)

class Process(Pcb):
    """
    New: In this status, the Process is just made or created.
    Running: In the Running status, the Process is being executed.
    Waiting: The process waits for an event to happen for example an input from the keyboard.
    Ready: In this status the Process is waiting for execution in the CPU.
    Terminated: In this status the Process has finished its job and is ended. 
    """
    def __init__(self,*args,**kwargs):
        super(Process,self).__init__(*args, **kwargs)

if __name__=='__main__':
    c1 = Cpu()
    p1 = Process(priority=3)
    p2 = Process(priority=4)
    p3 = Process(priority=2)
    print(p1)
    print(p2)
    print(p3)
