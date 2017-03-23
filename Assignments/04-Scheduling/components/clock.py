#!/usr/bin/env python3
from sim_components import *
import threading
import random


# === Class: Clock===

class Clock(object):
    """Simulated system clock.

    A singleton clock class so that any and all instances (objects) declared within the scope of 
    this file will all reference the same instance (hence all have the same values).

    - **Attributes**:
        - clock (int)      : Current value of clock
        - total_ticks (int): Total number of ticks the clock as accumulated (time run)
    """
    __shared_state = {}
    def __init__(self, start_time=0):
        """Clock constructor

        - **Args:**
            - start_time (int): Initial value of the clock

        - **Returns:**
            - None

        """
        self.__dict__ = self.__shared_state
        if len(self.__shared_state.keys()) == 0:
            self.lock = threading.Lock()
            self.clock = start_time
            self.total_ticks = 0

    def add(self, val):
        """Calls thread safe overloaded method

        - **Args:**
            - val (int): Value to add to the clock.
        - **Returns:**
            - None
        """
        return self.__iadd__(val)

    def current_time(self):
        """Returns the current value of the clock.

        - **Args:**
            - None
        - **Returns:**
            - (int): The current value of the clock.
        """
        return int(self.clock)

    def hard_reset(self,start=0):
        """Reset clock to some given value.

        Since this is a singleton object in a simulation evironment, I created 
        a method to "reset" or re-initialize the clock.

        - **Args:**
            - start (int): Value to reset clock to.
        - **Returns:**
            - None
        """
        self.clock = start
        self.total_ticks = 0

    def __iadd__(self, val):
        """Overloaded add method

        - This overloaded method allows something similar to:
            - c1 = Clock()
            - c1 += 1         # Will add 1 to the clock value 

        - **Args:**
            - val (int): Value to add to the clock.
        - **Returns:**
            - None
        """
        self.lock.acquire()
        self.clock += val
        self.total_ticks += 1
        self.lock.release()
        return self

    def __str__(self):
        """Visual dump of class state.

        - **Args:**
            - None
        - **Returns:**
            - None
        """
        return my_str(self)

def test_class_clock():
    print("Running Clock class test.....\n")

    print("Creating 3 clocks with different start times...")
    print("This will show that the clock class is a singleton and all instances refer to same single instance")

    # - init clock to 0 ticks (this clock is the clock each other instance will refer to.
    # - init clock to 2000 ticks
    # - init clock to 5000 ticks
    clocks = [Clock(0), Clock(2000), Clock(5000)]

    print("Random ticks between 50 and 100...")
    random_ticks = random.randint(50, 100)

    print("Running %d clock ticks:" % random_ticks)
    for i in range(random_ticks):
        index = random.randrange(0,len(clocks))
        print("adding to clock %d" % index)
        clocks[index] += 1

    print("Clock 1:")
    print(clocks[0])
    print("Clock 2:")
    print(clocks[1])
    print("Clock 3:")
    print(clocks[2])

# === Clock Test Code ===

if __name__=='__main__':
    test_class_clock()
