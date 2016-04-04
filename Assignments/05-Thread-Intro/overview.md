
# Not done

# CMPS 5143 Lab Exercise

Python's [threading module](http://docs.python.org/2/library/threading.html),
allows you to separate your program into [threads](http://en.wikipedia.org/wiki/Thread_(computing)). That
is, you break your program into pieces that you want to have run simultaneously on separate processors/cores, or that
you want to have take turns if you have only one processor.

A typical threading scenario is that you want to do a long-term computation in the background
(e.g. a large file download, or a complex search in a large database, or the on-going updating of the
map and characters in a simulation game with non-player characters), but you also want the user interface
to remain responsive. For example, suppose you want to start your long computation and present the
user with a progress bar with a Cancel button. Without threading, as soon as you start your
long computation, your Cancel button will be unresponsive until the computation is done. Alternatively,
you could build "check the Cancel button periodically" into your long computation. The former problem
would mean that there's no point in having a Cancel button at all, since it doesn't work. The latter
problem is better, but it means that you have to build user interface code into a computation that should
be independent of UI concerns.

But if you can say "do the computation in Thread A and wait for the Cancel button in Thread B", you get
the best of both worlds: clean code in the long computation combined with a responsive UI.

Often, threads need to share data or communicate with each other in some way. In the example above,
Thread B needs to update the progress bar based on the progress of Thread A, so they'll need to share
some sort of counter or percentage-done variable. Furthermore, Thread B will need a way to tell Thread A
to stop if the Cancel button gets clicked. It turns out, however, that sharing data between threads
causes weird behavior known as "race conditions", which typically yield badly corrupted data, and in
[at least one case, death](http://en.wikipedia.org/wiki/Therac-25).

The exercises below will show you, in Python, how to create multiple threads, how to induce them
to share data, and how to lock the data temporarily to prevent race conditions. This "concurrency" is a <em>very</em>
big and complex subject, but these exercises should get you started thinking about it.

- Read and run <a href="../programs/threads/threads1.py">threads1.py</a>. Make sure you
    understand the structure of the code and what's happening. If you don't, read the 
    <a href="http://docs.python.org/2/library/threading.html">documentation</a> or ask.
    
- By the way, if the program takes to long to run to completion, feel free to adjust the
    loop counter limits to speed things up a little bit--but you want it to take at least 5 seconds
    so you can see the interleaving of the threads.
    

- Read <a href="../programs/threads/threads2.py">threads2.py</a>. What do you expect to
    see that's different from before?

- Run <a href="../programs/threads/threads2.py">threads2.py</a>. Does it look right?
  (If you said yes, take a closer look at the end of your output. That's a race condition at work.)
  What do you think is going on?

- Read and run <a href="../programs/threads/threads3.py">threads3.py</a>. Does it fix
  the problems with <a href="../programs/threads/threads2.py">threads2.py</a>? What's the down-side?

- Try commenting out the join statements at the bottom of the program. What happens? What if you try to Ctrl-C out of the program because it's boring you?</p></li>

- Read and run <a href="../programs/threads/threads4.py">threads4.py</a>. This should generate
    a different and more ridiculous race condition. Try to come up with a concise explanation of what's happening
    to cause this bizarre behavior.

    <li><p>Uncomment the lock operations in <a href="../programs/threads/threads4.py">threads4.py</a>. Does
    that clear it up?</p></li>

    <li><p>What questions do you have about the code in these examples?</p></li>

    <li><p>What questions do you have about threading in general.</p></li>
</ol>

</div>
</body>
</html>

