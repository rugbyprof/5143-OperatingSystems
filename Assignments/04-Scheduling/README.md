## Scheduling Project


## Problem

Design and implement a program (in python) that simulates 1) ***Job Scheduling***,  2) ***CPU scheduling***, with the use of 3) ***Semaphores*** to lock critical sections of an operating system.

## General Requirements

### Job Scheduling
- New jobs are put on the job scheduling queue which will be implemented as a priority queue. 
- The job scheduling algorithm is run when a job arrives or terminates. 
- Job scheduling allows as many jobs to enter the ready state as possible given the following restriction: 
    - *a job cannot enter the ready state if there is not enough free memory to accommodate that job's memory requirement.* 
- Do not start a job unless it is the first job on the job scheduling queue. 
- When a job terminates, its memory is released, which may allow one or more waiting jobs to enter the ready state.

### Memory Management

- A job can only run if it requires less than or equal to the system's main memory capacity. 
- The system has a total of ***`N blocks`*** of usable memory. This value can change depending on simulation parameters. 
- If a new job arrives needing more than ***`N blocks`***, it is rejected by the system with an appropriate error message. 
- Rejected jobs do not factor into the final statistics (described below).

> **Note that all jobs in the ready state must fit into available main memory.**

### Process Scheduling Overview
- Process scheduling is managed as a [Multilevel Feedback Queue](http://pages.cs.wisc.edu/~remzi/OSTEP/cpu-sched-mlfq.pdf). 
- The queue has levels: ***`L`***<sub>***`N-1`***</sub>,***`L`***<sub>***`N-2`***</sub>`,...,` ***`L`***<sub>***`0`***</sub>.
- Each Queue is `FIFO`, and use `Round Robin` scheduling. 
- New jobs are put on the first level: ***`L`***<sub>***`N-1`***</sub> when arriving in the ready state. 
- When a job from ***`L`***<sub>***`N-1`***</sub> is given access to the CPU, it is allowed a quantum of ***`T`*** time units.
    - Where `T = ((N-1)-L + 1) * 50`
    - So:
        - Etc.
        - ***`L`***<sub>***`2`***</sub> = 150 
        - ***`L`***<sub>***`1`***</sub> = 100 
        - ***`L`***<sub>***`0`***</sub> = 50
- If it exceeds that time quantum, it is preempted and moves to ***`L`***<sub>***`(N-1)-1`***</sub> .

- For scheduling, the scheduler always starts picking up processes from the head of the highest level queue. 
- Only if the highest level queue has become empty will the scheduler take up a process from the next lower level queue. 
- The same policy is implemented for picking up in the subsequent lower level queues. 
- Meanwhile, if a process comes into any of the higher level queues, it will preempt a process in the lower level queue.
- Process scheduling decisions are made whenever any process leaves the CPU for any reason (e.g., expiration of a quantum or job termination). 
- When a job terminates, do job scheduling first, then process scheduling. 
    - (e.g. Move a job down to another queue if it used all its time slice, before scheduling next process on cpu).
- Also, give preference to first level jobs 
    - (i.e., if a job from the second level of the ready queue is running, and a new job enters the first level, the running job is preempted to the second level in favor of the first level job).

#### I.O
While executing on the CPU, a job may require I/O, which preempts it to the I/O wait queue for the duration of its I/O burst.

#### Critical Sections
While executing on the CPU, a job may perform a semaphore operation. Assume there are five semaphores shared among all jobs running in the system, numbered 0 through 4, each initialized to 1. If a job must wait because of a semaphore, it goes onto the appropriate wait queue until it is signaled. There is a separate wait queue for each semaphore.

#### Finished Jobs
When a job completes, put it on a finished list for later processing.

## Process States
| State Diagram |
|:-------------:|
| ![](https://d3vv6lp55qjaqc.cloudfront.net/items/3y2V3g3f1y303f463u2L/states.gif?X-CloudApp-Visitor-Id=1094421) |

| State  | Description | 
|:-------------|:----------|
| NEW | The process is being created, and has not yet begun executing. |
| READY | The process is ready to execute, and is waiting to be scheduled on a CPU. |
| RUNNING | The process is currently executing on a CPU. |
| WAITING | The process has temporarily stopped executing, and is waiting on an I/O request to complete. |
| TERMINATED | The process has completed. |

## CPU Scheduler Invocation

- There are four events which will cause the simulator to invoke schedule():

| Method  | Description | 
|:-------------|:----------|
| yield() | A process completes its CPU operations and yields the processor to perform an I/O request. |
| wake_up() | A process that previously yielded completes its I/O request, and is ready to perform CPU operations. |
| wake_up() | is also  called when a process in the NEW state becomes runnable. |
| preempt() | When using a Round-Robin or Static Priority scheduling algorithm, a CPU-bound process may be preempted before it completes its CPU operations. |
| terminate() | A process exits or is killed. |

http://pages.cs.wisc.edu/~remzi/OSTEP/cpu-sched-mlfq.pdf
