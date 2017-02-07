#!/usr/bin/env python
from subprocess import call

def cat(file):
    print("cat")
    call(["cat", file])