import random

class Queue(object):
  def __init__(self):
    self.Q = []
    
  def __str__(self):
    return ', '.join(map(str, self.Q))

  def push(self,val):
    self.Q.append(val)
    
    
  def pop(self):
      return self.Q.pop(0)
      
  def empty(self):
    return len(self.Q) == 0
  
  
Q1 = Queue()

Q1.push(45)
for i in range(15):
  Q1.push(random.randint(5,494))
print(Q1)
