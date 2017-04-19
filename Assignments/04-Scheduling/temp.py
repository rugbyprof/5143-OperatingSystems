 #!/usr/bin/python3 
import sys, os
sys.path.append(os.path.dirname(os.path.realpath(__file__))+'/components')
import random
import time

from sim_components import *
 
p = load_process_file(os.path.dirname(os.path.realpath(__file__))+'/./input_data/processes.txt')
processes = {}
count = 0
for i in range(len(p)):
    print(p[i])
    processes[p[i]['pid']] = Process(**p[i])

m = Memory()
    
tot_mem_required = 0
for k,p in processes.items():
    tot_mem_required += int(p['mem_required'])
    if m.fits(p['mem_required']):
        m.allocate(p)
    else:
        break
print(m)
print(tot_mem_required)
