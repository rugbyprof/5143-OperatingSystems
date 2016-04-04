# CMPS 5143 Lab Exercise

I found this on another professors website here: http://cs.carleton.edu/faculty/jondich/courses/cs257_f13/assignments/threads.html, and it just so happens that it guides you through the exact concepts that I would like to cover. 


## Assignment

Python's [threading module](http://docs.python.org/2/library/threading.html), allows you to separate your program into [threads](http://en.wikipedia.org/wiki/Thread_(computing)). That is, you break your program into pieces that you want to have run simultaneously on separate processors/cores, or that you want to have take turns if you have only one processor.

A typical threading scenario is that you want to do a long-term computation in the background (e.g. a large file download, or a complex search in a large database, or the on-going updating of the map and characters in a simulation game with non-player characters), but you also want the user interface to remain responsive. For example, suppose you want to start your long computation and present the user with a progress bar with a Cancel button. Without threading, as soon as you start your long computation, your Cancel button will be unresponsive until the computation is done. Alternatively, you could build "check the Cancel button periodically" into your long computation. The former problem would mean that there's no point in having a Cancel button at all, since it doesn't work. The latter problem is better, but it means that you have to build user interface code into a computation that should be independent of UI concerns.

But if you can say "do the computation in Thread A and wait for the Cancel button in Thread B", you get the best of both worlds: clean code in the long computation combined with a responsive UI.

Often, threads need to share data or communicate with each other in some way. In the example above, Thread B needs to update the progress bar based on the progress of Thread A, so they'll need to share some sort of counter or percentage-done variable. Furthermore, Thread B will need a way to tell Thread A to stop if the Cancel button gets clicked. It turns out, however, that sharing data between threads causes weird behavior known as "race conditions", which typically yield badly corrupted data, and in [at least one case, death](http://en.wikipedia.org/wiki/Therac-25).

The exercises below provide pre-written examples in Python that:
    - create threads
    - share data
    - pose race conditions
    - fix race conditions via locks and joins

Concurrency is a <em>very</em> big and complex subject, but these exercises should get you started thinking about it.

### Lab 

- Read and run [Threads1.py][1]. Make sure you understand the structure of the code and what's happening. If you don't, read the  <a href="http://docs.python.org/2/library/threading.html">documentation</a> along with any general python language references.
    
- If the program takes to long to run to completion, adjust the loop counter limits to speed things up, but make sure it runs for a minimum of 5 seconds.
    
- Before running [Threads2.py][2], read it and try to understand it before viewing the output. 

- Run [Threads2.py][2] and view the output.

- Read and run [Threads3.py][3]. Does it fix the problems that occured in [Threads2.py][2]? Think about what the down side might be.

- Comment out the join statements at the bottom of the program and run it again.

- What if you try to Ctrl-C out of the program before it terminates?

- Read and run [Threads4.py][4]. This should generate a different and more ridiculous race condition. 

- Uncomment the lock operations in [Threads4.py][4]. Does that clear it up?

### Deliverables
##### Due: Friday by 5:00 P.M

Upload a markdown file to your repository answering the following questions:

1. Explain the differences between Threads1 and Threads2 using lines from the code and a precise explanation.

2. After running Thread3.py does it fix the problems that occured in Threads2.py? What's the down-side?

3. Comment out the join statements at the bottom of the program and describe what happens.

4. What happens if you try to Ctrl-C out of the program before it terminates?

5. Read and run Threads4.py. This generates a different and more ridiculous race condition. Write concise explanation of what's happening to cause this bizarre behavior using lines from the code and precise explanation.

5. Does uncommenting the lock operations clear up the problem in question 5?

Include your name, date, and M# at the top of your assignment.

[1]: https://github.com/rugbyprof/5143-OperatingSystems/blob/master/Assignments/06-Thread_Intro/threads1.py  "Threads1"
[2]: https://github.com/rugbyprof/5143-OperatingSystems/blob/master/Assignments/06-Thread_Intro/threads2.py  "Threads2"
[3]: https://github.com/rugbyprof/5143-OperatingSystems/blob/master/Assignments/06-Thread_Intro/threads3.py  "Threads3"
[4]: https://github.com/rugbyprof/5143-OperatingSystems/blob/master/Assignments/06-Thread_Intro/threads4.py  "Threads4"
