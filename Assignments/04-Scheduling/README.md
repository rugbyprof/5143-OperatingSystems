## Cpu_Scheduling_Simulation_Project

Design and implement a program (in python) that simulates some of the job scheduling, CPU scheduling, and semaphore processing of an operating system. A large portion of the simulation is given to you already (if you choose to use it). An explanation of the code can be found [here](./components/README.md).

### New Jobs
- When jobs initially arrive in the system, they are put on the `job scheduling queue` which is maintained in FIFO order. 
- The `job scheduling algorithm` is run when a job arrives or terminates. 
- Job scheduling allows as many jobs to enter the ready state as possible given the following restriction: 
    - a job cannot enter the ready state if there is not enough free memory to accommodate that job's memory requirement. 
- Do not start a job unless it is the first job on the job scheduling queue. 
- When a job terminates, its memory is released, which may allow one or more waiting jobs to enter the ready state.

### Memory
- A job can only run if it requires less than or equal to the system's main memory capacity. 
- The system has a total of **512** blocks of usable memory. 
- If a new job arrives needing more than **512** blocks, it is rejected by the system with an appropriate error message. 
- Rejected jobs do not factor into the final statistics (described below).

***Note that all jobs in the ready state must fit into available main memory.***

### Process Scheduling
- Process scheduling is managed as a `multilevel feedback queue`. 
- The queue has two levels, each queue is organized as a `FIFO`, and both use a `round robin` scheduling technique. 
- New jobs are put on the first level when arriving in the ready state. 
- When a job from the first level is given access to the CPU, it is allowed a quantum of 100 time units. 
- If it exceeds that time quantum, it is preempted and moves to the second level.

- The jobs on the second level may only be allocated the CPU if there are no jobs on the first level. 
- When a job on the second level is given access to the CPU, it is allowed a quantum of 300 time units. 
- If it exceeds that, it is preempted and put back on the second level of the ready queue.

- Process scheduling decisions are made whenever any process leaves the CPU for any reason (e.g., expiration of a quantum or job termination). 
- When a job terminates, do job scheduling first, then process scheduling. 
- Also, give preference to first level jobs (i.e., *if a job from the second level of the ready queue is running, and a new job enters the first level, the running job is preempted to the second level in favor of the first level job*).

### IO Interrupts
- While executing on the CPU, a job may require I/O, which preempts it to the `I/O wait queue` for the duration of its I/O burst.

### Critical Section
- While executing on the CPU, a job may perform a semaphore operation. 
- Assume there are five semaphores shared among all jobs running in the system, numbered 0 through 4, each initialized to 1. 
- If a job must wait because of a semaphore, it goes onto the appropriate wait queue until it is signaled. 
- There is a separate wait queue for each semaphore.

- When a job completes, put it on a finished list for later processing.

### Instructions / Events
- The simulator is driven by the events read from standard input. Examples of possible events are given below. 
- The first field will be the first character of the line, and subsequent fields will be separated by one of more spaces or tabs. 
- The header of each field in the following examples does not appear in the input stream.

**A new job arrives:**

|Event |Time |Job |Memory |Run Time|
|------|-----|----|-------|--------|
|A     |140  |12  |24     |2720    |

*Interpretation: job 12 arrives at time 140, requires 24 blocks of memory and uses the CPU for a total of 2720 time units.*

**A job needs to perform I/O:**

|Event |Time |I/O Burst Time|
|------|-----|--------------|
|I     |214  |85           |

*Interpretation: the job currently running on the CPU will not finish its quantum because at time 214 it needs to perform I/O for a duration of 85 time units.*

**A job performs a wait on a semaphore:**

|Event |Time |Semaphore|
|------|-----|--------------|
|W     |550  |2           |

*Interpretation: the job currently running on the CPU performs a wait on semaphore number 2 which may or may not cause it to be preempted. Initialize each semaphore to 1.*

**A job performs a signal on a semaphore:**

|Event |Time |Semaphore|
|------|-----|--------------|
|S     |622  |2           |

*Interpretation: the job currently running on the CPU performs a performs a signal on semaphore number 2 which may allow a job to re-enter the ready state.*

**Display the status of the simulator:**

|Event |Time |
|------|-----|
|D     |214  |

*Interpretation: display the status of the simulator at time 214.*

- ***You may assume that events appear on the input stream in ascending time order and no two events happen at the same time.*** 
- However, realize that the events given in the input stream are not only events which your simulator must handle. For instance, a time quantum expiration is not an event given in the input stream, but it is an event which your simulator must handle. 
- Furthermore, an internal event, such as a time quantum expiration, not in the input stream, may occur at the same time as an event in the input stream (e.g., a new job arrival). Events in the input stream are external events.

- The following is a list of internal events (i.e., not given on the input stream) which your simulator must handle:

- I/O completion (C)
- time quantum expiration (E)
- job termination (T)

- Assume that context switching, semaphore operations, and displays take no simulator time (an unrealistic assumption in a real operating system).

### Status Display

- When a display is requested, print the contents of all queues as well as the job currently running on the CPU to standard output using only the format used in the sample output given below.

After processing all jobs, write the following to standard output (in this order, as shown on the sample output given below):

- `completion time` for each job (in order of completion),
- `average turnaround` time (where turnaround time is defined as completion time minus arrival time), and
- `average job scheduling wait time` (where wait time is defined as the number of time units spent in the job scheduling queue).

### Event Collisons

Often more than one event happen at the same time. Use the following rules to determine which events to process first:

- If an internal event (e.g., an event not on the input stream such as time slice expiration, I/O completion, or job termination) and an external event (i.e., an event given explicitly on the input stream) happen at the same time, process the internal event first.
- If a job is scheduled to come off the I/O wait queue at the same time a job is scheduled to come off the semaphore wait queue, take the job off the I/O wait queue first.


### Additional Requirements

- Your implementation must be distributed across more than one source code file, in some sensible manner which reflects the logical purpose of the various components of your design, to encourage problem decomposition and modular design. This is mostly done for you if you use the starter code, however you must use OOP concepts with any additional code you add. 
- Include a README.md file in your submission which contains:
    - Team Information
        - The team members names.
        - Which additional code is attributed to each team member.
        - Time each team member spent working on project.
    - Your participation should be visualized in a pie chart:
    
    ![](http://linux.activityworkshop.net/more_info/pie_google.png)
    
    - Files in project
        - A list showing the file structure of your code and which files are included in your project.
        
## Hints and notes

- I created a class for many of the components of the simulation. You should continue with by coding with a modular based design. 
- When debugging your simulator, you are advised to add extra display events to the sample input to trace the movement of jobs throughout the various queues of the system.
- You are advised to organize jobs on the I/O wait queue in the order in which they are scheduled to come off (i.e., make the I/O queue a priority queue) to obviate having to search the queue for the next job to come off of it everytime an I/O operation completes.
- You are advised to organize jobs on each of the 5 semaphore wait queues in FIFO order.
- If designed properly, the program required to solve this project should occupy no more than 1,000 lines of code (or less if you use built-in data structures or data structures from libraries).


### Test data: sample input and output streams

- (processes only) [processes.txt](https://github.com/rugbyprof/cpu_scheduler_sim/blob/master/input_data/processes.txt)
- (only events A & D, & E & T) [jobs_in_a.txt](https://github.com/rugbyprof/cpu_scheduler_sim/blob/master/input_data/jobs_in_a.txt) and [jobs_out_a.txt](https://github.com/rugbyprof/cpu_scheduler_sim/blob/master/input_data/jobs_out_a.txt)
- (only events A, I, & D, & E, C, & T) [jobs_in_b.txt](https://github.com/rugbyprof/cpu_scheduler_sim/blob/master/input_data/jobs_in_b.txt) and [jobs_out_b.txt](https://github.com/rugbyprof/cpu_scheduler_sim/blob/master/input_data/jobs_out_b.txt)
- (all events: A, I, W, S, & D, & E, C, & T) [jobs_in_c.txt](https://github.com/rugbyprof/cpu_scheduler_sim/blob/master/input_data/jobs_in_c.txt) and [jobs_out_c.txt](https://github.com/rugbyprof/cpu_scheduler_sim/blob/master/input_data/jobs_out_c.txt)

- Use the UNIX diff utility to compare your output to the correct output. For full credit, the output produced by your program must have zero differences, as defined by diff, with the output posted here.

## Deliverables

- All files should be on github in your assignments folder by Tuesday May 9<sup>th</sup>. by Midnight.
- Create a folder called `cpu_simulation` in your assignments folder to place all project files.
- Create a `README.md` file that fulfills the "Additional Requirements" stated above.
- Bring a hard copy of your code and readme and place it in my mailbox by 10:00am May 10<sup>th</sup>. 
- Code placed on github too late or hard copy delivered late will result in a 2 letter grade penalty.
- Code that does not run, will be assigned a grade of zero.
- Otherwise, see below for additional grading requirements.

## Evaluation

- 10% of your grade will be based on style and design.
- If your program produces this jobs_out_c.txt exactly when run on jobs_in_c.txt <br> (all events: A, I, W, S, & D, & T, E, & C), you can earn up to **90 points**.
- If your program produces this jobs_out_b.txt exactly when run on jobs_in_b.txt <br> (only events A, I, & D, & T, E, & C), you can only earn up to **65 points**.
- If your program produces this jobs_out_a.txt exactly when run on jobs_in_a.txt <br> (only events A & D, & T & E), you can only earn up to **40 points**.
- If your program does not produce this jobs_out_a.txt exactly when run on jobs_in_a.txt, **you will not earn any points**.
- If your program does not compile or execute without errors or warnings, **you will not earn any points**.

>Note: Depending on how you order the jobs on your I/O wait queue, your dump of the jobs waiting for I/O may not match our output exactly, and for just that queue, that is acceptable. For instance, you might organize your I/O wait queue as a priority queue where the job which comes off first is at the head, or you might maintain jobs on the I/O wait queue in the order in which they are put on and then search for the job to take off when the I/O is complete.

<sub>Source: Saverio Perugini http://academic.udayton.edu/SaverioPerugini/</sub>


Notes:
- upload zip file called `cpu_simulation_#.zip` that unzips to folder `cpu_simulation_(team#)`
- Comment code with blocks for each function / class and major comment block with names and sources
- remove any code you do not use
- references are a must 
- provide instructions on how to run. make sure to generate 3 output files (I should specify names).
