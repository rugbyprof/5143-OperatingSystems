#!/usr/bin/env python
from subprocess import call

def cat(file):
    call(["cat", file])