import os, sys

run = ['accounting.py','clock.py','cpu.py','fifo.py','memory.py','process.py','semaphore.py']


print(run)

for f in run:
    x = input("Running %s" % f)
    os.system('python3 '+str(f))