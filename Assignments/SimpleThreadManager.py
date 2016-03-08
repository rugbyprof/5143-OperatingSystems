## Thread Manager

This is not a hard assignment, it's really just a homework. You should be able to write this in one sitting:

- Create a folder called `Threading` and place it in your `5143_Opsys` folder.
- Create a file called `threadManager.py` and put that in the `Threading` folder.
- In your file, create a class called: `threadManager` that extends `threading.Thread` and has the following functionality:
    - Method to **add** a thread which will give it a name and id (then don't run it until explicitly invoked using name or id)
    - Method to **run** a thread based on name, or id (once run, remove it from the class).
    - Method to **run all** threads being managed (that have not been run yet).  
- Each thread will run the same function for ease of implementation right now.

```python
def fun(self):
    time.sleep(random.randint(self.min,self.max)
    return
    
```

Remember the code we played with in class:

```python
import threading
import time
import random

class MyThread(threading.Thread):

    def run(self):
        time.sleep(5)
        return

    @staticmethod
    def enumerate():
        return threading.enumerate()

if __name__ == '__main__':
    t = []
    for i in range(3):
        t.append(MyThread())
        t[-1].start()

    print(MyThread.enumerate())
```

You don't need to implement any static methods, I simply put the code in here as a jumping off point. 
