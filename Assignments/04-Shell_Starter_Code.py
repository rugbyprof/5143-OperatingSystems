"""
@Program Name: Yo-Shell V1 Starter Code
@Author: Dr. Griffin

@Description:
    This code is a barebones snippet to get your shell up and running. It provides the following classes (each of which is not fully implemented):
      historyManager
      parserManager
      commandManager
      driver
"""

import os
import sys

class historyManager(object):
    def __init__(self):
        self.command_history = []

    def push_command(self,cmd):
        self.command_history.append(cmd)

    def get_commands(self):
        return self.command_history

    def number_commands(self):
        return len(self.command_history)


class parserManager(object):
    def __init__(self):
        self.parts = []

    def parse(self,cmd):
        self.parts = cmd.split(" ")
        return self.parts

class commandManager(parserManager):
    def __init__(self):
        self.command = None

    def run_command(self,cmd):
        self.command = cmd
        self.command = self.parse(self.command)
        return self.command

    def ls(dir):
        for dirname, dirnames, filenames in os.walk('.'):
            # print path to all subdirectories first.
            for subdirname in dirnames:
                print(os.path.join(dirname, subdirname))
    
        # print path to all filenames.
        for filename in filenames:
            print(os.path.join(dirname, filename))
    
    def cat(file):
        f = open(file,'r')
        print(f.read())

class driver(object):
    def __init__(self):
        self.history = historyManager()
        self.commands = commandManager()
        self.number_commands = 0

    def runShell(self):
        number_commands = 0
        while True:
            self.input = input("parser-$ ")         # get command
            self.history.push_command(self.input)   # put in history
            parts = self.commands.run_command(self.input)
            print(parts)


if __name__=="__main__":
    d = driver()
    d.runShell()
