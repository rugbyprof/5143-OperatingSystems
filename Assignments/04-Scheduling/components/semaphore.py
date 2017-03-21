#!/usr/bin/env python3
# === Class: Semaphore===
import sys, os
sys.path.append(os.path.dirname(os.path.realpath(__file__))+'/components')
class Semaphore(object):
    """A class to simulate a semaphore.
    - **Methods**:
        - acquire() : Attempt to acquire copy of semaphore
        - release() : Relinquish semaphore

    - **Attributes**:
        - max_count   : Number of copies available for this instance
        - current     : Current value of semaphore
    """
    def __init__(self, count=1):
        self.acquired_dict = {}

        for i in range(count):
            self.acquired_dict[i] = None

    def acquire(self, obj_id):
        """Acquiring of the semaphore.

        - **Args:**
            - None
        - **Returns:**
            - (bool) : True if copy acquired / False otherwise.
        """
        next_sem = self.available()
        if next_sem is not None:
            self.acquired_dict[next_sem] = str(obj_id)
            return True
        else:
            return False


    def release(self, obj_id):
        """Releasing of the semaphore.

        - **Args:**
            - None
        - **Returns:**
            - (bool) : True if copy released / False otherwise.
        """
        for i, sem in self.acquired_dict.items():
            if str(sem) == str(obj_id):
                self.acquired_dict[i] = None
                return True
        return False

    def available(self):
        """Check if semaphore slot is available. And returns it.

        - **Args:**
            - None
        - **Returns:**
            - (int , None) : Int if spot available, None if not.
        """
        for i, sem in self.acquired_dict.items():
            if sem is None:
                return i

        return None

    def __str__(self):
        return "Semaphore State: %s" % str(self.acquired_dict)

###################################################################################################

# === Class: SemaphorePool===

class SemaphorePool(object):
    """A class to simulate a semaphore .
    - **Methods**:
        - acquire(obj_id) -> (int,None) : Attempt to acquire semaphore, success = value that is not None.
        - release(obj_id) -> (int,None) : Attempt to release semaphore, success = value that is not None.
    - **Attributes**:
        - sem_dict  : List of fake semaphores

    """
    __shared_state = {}
    def __init__(self, num_sems=5, count=1):
        self.__dict__ = self.__shared_state

        if len(self.__shared_state.keys()) == 0:
            self.sem_dict = {}
            self.sem_owner = []
            for i in range(num_sems):
                self.sem_dict[i] = Semaphore(count)
                self.sem_owner.append(None)

    def acquire(self, obj_id=None):
        """Acquire a semaphore from pool.
        - **Args:**
            - obj_id (int) : Id of object (or some process id) requesting the semaphore
        - **Returns:**
            - (int , None) : Int if a semaphore was acquired, or None if no semaphore was available
        """
        if obj_id is None:
            raise Exception("Need object id to acquire semaphore.")
        for i in self.sem_dict:
            if not self.sem_dict[i].available() is None:
                self.sem_dict[i].acquire(obj_id)
                self.sem_owner[i] = obj_id
                return i

    def release(self, obj_id=None):
        """Release a semaphore from pool.

        - **Args:**
            - obj_id (int) : Id of object (or some process id) requesting the semaphore
        - **Returns:**
            - (int , None) : Int if a semaphore was released, None if 'obj_id' was not in dict
        """
        if obj_id is None:
            raise Exception("Need object id to acquire semaphore.")
        try:
            # Is object id in owner list?
            i = self.sem_owner.index(obj_id)
        except:
            # If it is not, return None
            return None

        # If it is, relase the semaphore
        self.sem_dict[i].release(obj_id)
        self.sem_owner[i] = None
        return i

    def __str__(self):
        string = ""
        for i, sem in self.sem_dict.items():
            string += "%s: %s\n" % (i,str(sem))
        return string

class dummy:pass

def test_semaphore_class():
    print("Creating semaphore with value of 3")
    S = Semaphore(3)
    print("semaphore state: ",S.acquired_dict)
    print()

    # Create 5 dummy classes to acquire and release semaphores
    d1 = dummy()
    d2 = dummy()
    d3 = dummy()
    d4 = dummy()
    d5 = dummy()
    d6 = dummy()

    print("d1 Attempt to acquire ... (should work)")
    print(S.acquire(id(d1)))
    print(S)
    print()

    print("d2 Attempt to acquire ...(should work)")
    print(S.acquire(id(d2)))
    print(S)
    print()

    print("d3 Attempt to acquire ...(should work)")
    print(S.acquire(id(d3)))
    print(S)
    print()

    print("d4 Attempt to acquire ...(should work)")
    print(S.acquire(id(d4)))
    print(S)
    print()

    print("d5 Attempt to acquire ...(should fail - none left)")
    print(S.acquire(id(d5)))
    print(S)
    print()

    print("d5 Attempt to release ... (should fail - never got a copy)")
    print(S.release(id(d5)))
    print(S)
    print()

    print("d3 Attempt to release ... (should work)")
    print(S.release(id(d3)))
    print(S)
    print()

    print("Creating a semaphore pool with 5 semaphores with a start value of 1")
    SP = SemaphorePool()
    print(SP)

    print("d1 Attempt to acquire ... (should work)")
    print(SP.acquire(id(d1)))
    print(SP)

    print("d2 Attempt to acquire ... (should work)")
    print(SP.acquire(id(d2)))
    print(SP)

    print("d3 Attempt to acquire ... (should work)")
    print(SP.acquire(id(d3)))
    print(SP)

    print("d4 Attempt to acquire ... (should work)")
    print(SP.acquire(id(d4)))
    print(SP)

    print("d5 Attempt to acquire ... (should work)")
    print(SP.acquire(id(d5)))
    print(SP)

    print("d6 Attempt to acquire ... (should fail - none left)")
    print(SP.acquire(id(d6)))
    print(SP)


    print("d6 Attempt to release ... (should fail - never got copy)")
    print(SP.release(id(d6)))
    print(SP)

    print("d2 Attempt to release ... (should work)")
    print(SP.release(id(d2)))
    print(SP)


if __name__=='__main__':
    test_semaphore_class()
