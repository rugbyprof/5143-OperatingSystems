import sys

def promptUser():
    var = input('% ')
    return var.split('|')
    
    
class commands(object):
    def __init__(self):
        self.Commands = {}
        
    def __str__(self):
        string = "("
        for k,v in self.Commands.items():
            string += "["+str(k)+":"+str(v)+"]"
        return string
        
    def addCommand(self,cmd,desc):
        self.Commands[cmd] = desc

    def delCommand(self,cmd):
        del self.Commands[cmd]
        

print("hello world")

L = []

L.append(4)
L.append(5)
L.append(99)
L.append("hello world")
L.append([1,2,3])
print(L)



for i in L:
    print(i)
    
L = L[::-1]
print()    
for i in range(len(L)):
    print(L[i])
    
Commands = {}

Commands['ls'] = "listing"
Commands['pwd'] = "print working directory"
Commands['cat'] = "dump file to std out"

print(Commands)

"""
for i in Commands:
    print(i)
    
for k,v in Commands.items():
    print(str(k) + "," + str(v))
"""

p1 = (23,45)
x,y = p1

print(x)
print(y)

cmd = "ls -lah | wc -l"

print(cmd)

cmd = cmd.split('|')

print(cmd)

#print(promptUser())

C = commands()
C.addCommand('ls','listing')
C.addCommand('pwd','print working directory')
C.addCommand('grep','find text in files')
print(C)
    
