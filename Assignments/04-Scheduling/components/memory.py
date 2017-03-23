#!/usr/bin/env python3
from sim_components import *
import time 


# === Class: Memory===

class Memory(object):
    """A singleton object that Manages the simulated memory.
    - **Methods**:
        - allocate(pid) -> dict : Attempt to allocate memory for a process
        - deallocate(pid) -> dict : Remove process from memory if process exists
        - available(blks) -> bool : Is memory available >= "blks" size
        - __calc_available(process) -> None : Total up allocated memory
    - **Attributes**: 
        - mem_size   : Total memory size in "blocks"
        - blks_avail : Blocks currently available
        - blks_used  : Blocks allocated to processes
        - pid_list   : List of process in memory
    """
    __shared_state = {}
    def __init__(self, size=512):
        """

        """
        self.__dict__ = self.__shared_state

        if len(self.__shared_state.keys()) == 0:
            self.mem_size = size
            self.blks_avail = size
            self.blks_used = 0
            self.process_table = {}

    def allocate(self, process):
        """Allocate chunk of memory.

        - **Args:**
           - process (Process): process being allocated memory.
        - **Returns:**
           - dict: {'success':True}
           - dict: {'success':False, 'error':"Not enough memory available"}
        """
        if self.fits(process['mem_required']):
            self.process_table[int(process['process_id'])] = process
            self.__calc_available()
            return {'success':True}
        else:
            return {'success':False, 'error':"Not enough memory available",
                    'requested':process.mem_required, 'available':self.blks_avail}

    def deallocate(self, pid):
        """Deallocate chunk of memory.

        - **Args:**
           - process (Process): The process to be removed from memory.
        - **Returns:**
           - (dict): {'success':True}
           - (dict): {'success':False, 'error':"Process id did not exist"}
        """
        if int(pid) in self.process_table:
            del self.process_table[int(pid)]
            self.__calc_available()
            return {'success':True}
        else:
            return {'success':False, 'error':"Process id did not exist"}


    def fits(self, blks=None):
        """Check to see how mucn memory is available.

        - **Args:**
           - blks (int): Blocks needed to allocate.
        - **Returns:**
           - (bool): The return value. True for success, False otherwise.
        """
        if blks is None:
            raise Exception("Block size needed missing as a parameter.")
        return int(self.blks_avail) >= int(blks)

    def available(self):
        """Check to see how mucn memory is available.

        - **Args:**
           - None
        - **Returns:**
           - (int): The total available blocks remaining.
        """
        return int(self.blks_avail)

    def __calc_available(self):
        """Calculate available memory, if any.

        This private method sums all allocated memory using processes in the process table
        and calculates the "blks_available".

        - **Args:**
           - None
        - **Returns:**
           - None
        """
        self.blks_used = 0
        for pid, pvals in self.process_table.items():
            self.blks_used += int(pvals.mem_required)
        self.blks_avail = self.mem_size - self.blks_used

    def __eq__(self,rhs):
        """Checks to see if two mem instances are same.

        Used for testing to see if memory instances are actually equal.
        
        - Usage: 
            - mem1 = Memory(1024)
            - mem2 = Memory(2048)
            - print(mem1 == mem2)  
            - prints True because mem2 doesn't actually create a new instance it simply creates a different reference to mem1
        """
        return self.mem_size == rhs.mem_size and self.blks_avail == rhs.blks_avail and \
               self.blks_used == rhs.blks_used and len(self.process_table) == len(rhs.process_table)

    def __str__(self):
        """Visual dump of class state.

        - **Args:**
            - None
        - **Returns:**
            - None
        """
        return my_str(self)

def test_memory_class():
    mem_size = 512
    # Read in a bunch of process data from our test file
    processes = load_process_file(os.path.dirname(os.path.realpath(__file__))+'/../input_data/processes.txt')
    for i in range(len(processes)):
        processes[i] = Process(**processes[i])

    print("############################################################")
    print("Running Memory class test.....\n")

    print("Allocating memory of size: %d ...." % int(mem_size))
    #time.sleep(.1)
    mem = Memory(mem_size)

    for subp in processes:
        time.sleep(.1)
        print("Registering process ....")
        avail = mem.available()
        print("  Available: %d" % avail)
        need = subp['mem_required']
        print("  Needed   : %s" % need)
        res = mem.allocate(subp)
        print(res)
    #time.sleep(.1)
    print("Memory snapshot ...")
    print(mem)

    #time.sleep(.1)
    print("Removing processes from memory ....")
    print(mem.deallocate(2))
    print(mem.deallocate(3))

    print("Removing non existing processes from memory ....")
    print(mem.deallocate(9))

    #time.sleep(.1)
    print("Memory snapshot ...")
    print(mem)

    print("Allocating another memory instance with double the size")
    mem2 = Memory(mem_size*2)

    print("Printing the new memory instances, shows that it refers to the single instance allowed")
    print(mem2)

    print("Does mem1 == mem2")
    print(mem == mem2)
   

if __name__=='__main__':
    test_memory_class()