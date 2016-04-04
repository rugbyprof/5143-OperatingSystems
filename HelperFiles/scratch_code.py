import sys

class Stack:
    def __init__(self):
         self.list = []
         self.empty = True
         self.size = 0
         
    def empty(self):
         return self.empty
         
    def push(self,val):
        self.list[size] = val
        self.size +=1 
        self.empty = False
    
    def pop(self):
        val =  self.list[size-1]
        self.size -= 1
        
        if self.size == 0:
            self.empty = True
            
        return val
        


array = [x for x in range(10)]

for i in range(10):
    array[i] = [x for x in range(20)]
    
NUMS = [3,4,5,3,7,6,8,7,8,9,7,6,5,4,-1,5,6,7,5]


i = 0
while NUMS[i] > 0:
    print NUMS[i]
    i += 1
    

       

def calcProduct(m,n):
    prod = 1
    for i in range(n,m+1):
        prod *= i
        
    return prod

print calcProduct(6,3)


def average(banana):
    total = 0.0
    for i in banana:
        total += i
    
    return total / len(banana)

def average2D(tDArray):
    pass

n = 5

for x in range(n):
    for j in range(x+1):
        sys.stdout.write('*')
    print
    

L = [x for x in range(10,50,5)]

print average(L)







