#The order these packages are included matter.
import sys, os
sys.path.append(os.path.dirname(os.path.realpath(__file__))+'/components')

def my_str(obj):
    """A quick dump of any object

    A function to dynamically create a '__str__' function in which all non-methods (non-callables)
    is turned into a string and returned to calling object. Probably could be cleaner but not
    interested right now in improving it.

    Args:
        obj (object): The "self" portion of an object to be printed

    Returns:
        string: Representation of object

    """

    names = []
    vals = []
    for value in dir(obj):
        if not value.startswith('__') and not callable(obj.__getattribute__(value)):
            vals.append(obj.__getattribute__(value))
            names.append(value)
    string = "["+obj.__class__.__name__ + ":\n    ["
    for name in names:
        string += str(name) + ': %s, \n     '
    string = string[:-2]
    string += " ]\n]"
    return string % tuple(vals)


def load_process_file(file_name,return_type='List'):
    """
    Read the process data from given file name.
    Data format:
        Event   Time    Job     Memory  Run-Time
        ----    ----    ---     ------  --------
        A       131     5       513     64
        D       361

        Event   Time    IO-Burst-Time
        -----   ----    -------------
        I       214     85

        Event   Time    Semaphore
        -----   ----    ---------
        S       7183    2
        W       7287    3

        A = new process enters system
        D = Display status of simulator
        I = Process currently on cpu performs I/O
        S = Semaphore signal (release)
        W = Semaphore wait (acquire)
    - **Args**:
        - file_name (string) : file to get simulation commands from
    - **Returns**:
        - tuple (list,dict) : returns a list version and dict version. Dict version 
                              uses arrival time as key.
    """
    jobs_list = []
    jobs_dict = {}
    with open(file_name, 'r') as f:
        data = f.read()
    data = data.split('\n')
    for j in data:
        j = j.split()
        if len(j) > 0:
            d = build_process_dict(j)
            jobs_list.append(d)
            jobs_dict[d['time']] = d
    if return_type == 'List':
        return jobs_list
    else:
        return jobs_dict              


def build_process_dict(vals=[]):
    """Builds a kwargs dict for a new process initialization.
    - **Args**:
        - vals (list) : values from one line in input file
    - **Returns**:
        - dictionary or list 
        - [{'event': 'D', 'time': '592'},....{'event': 'D', 'time': '592'}]
        - {'592':{'event': 'D', 'time': '592'},...,
    """
    labels_dict = {}
    labels_dict['A'] = ['event', 'time', 'pid', 'mem_required', 'burst_time']
    labels_dict['I'] = ['event', 'time', 'ioBurstTime']
    labels_dict['W'] = ['event', 'time', 'semaphore']
    labels_dict['S'] = ['event', 'time', 'semaphore']
    labels_dict['D'] = ['event', 'time']    
    process_dict = {}
    labels = labels_dict[vals[0]]
    for i, item in enumerate(vals):
        process_dict[labels[i]] = vals[i].strip()
    return process_dict

from accounting import Accounting
from accounting import SystemAccounting
from process import Process
from clock import Clock
from cpu import Cpu
from fifo import Fifo
from memory import Memory
from semaphore import Semaphore
from semaphore import SemaphorePool


#Import test functions
from clock import test_class_clock
from cpu import test_cpu_class

from memory import test_memory_class
from process import test_process_class
from semaphore import test_semaphore_class