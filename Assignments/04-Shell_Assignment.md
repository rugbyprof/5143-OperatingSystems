# YO-Shell.v.1 (Your Own Shell) 
Due: TBD

# Not COMPLETE

## Overview

Your going to write your own command line interpreter using python. Your interpreter will implement a subset of the existing bash
commands that we use. We could do this in pretty much any language, in fact, "C" would be the language of choice if this were to 
be something that we would release to market, however, Python is a pretty stout language and will simplify the implementation of your
own Shell. 

This first version we will only implement a basic shell: which sits a waits for commands. When the `enter` key is pressed, your shell will "parse" the command and execute it based on the name of the command, parameters, and any additional flags included on the command line. Of course your shell should not "crash" if things don't go as expected, so you will need to handle all kinds of bad input. 

The definition of `parse` is: 
>- verb 
    - Analyze (a sentence) into its parts and describe their syntactic roles.
- noun (COMPUTING)
    - An act of or the result obtained by parsing a string or a text.

We will break a sentence (string) into it's parts: 1) command 2) arguments 3) flags

- Command:
    - This is the part of the string that tells the interpreter what specific action it wants to perform. 
    - This is the first item in the string. 
- Arguments:
    - This is one or more items that the command needs to perform it's action. 
    - They typically follow the command but they don't always have to. 
    - An example is: `cp file1.txt file2.txt` where `file1.txt` is the first argument and `file2.txt` is the second argument. 
    - If one of the mandatory arguments isn't present, your shell should handle this with an error message, and not crash.
- Flags:
    - These alter a command in specific ways. 
    - Flags should start with a `-` and should be followed by one or more "flags".
    - A flag could be a single letter like: `ls -l` where the `-l` specifies "long listing".
    - A flag can be multiple letters like: `ls -la` or `ls -l -a` which both perform "long listings of all files".
    - Sometimes a flag can be a word, but when words are used, it typically follows this format: `grep --color=always  abc  a_file.txt`.
    - We won't implement this type of flag.

What we won't implement in Version 1:
- Autocompletion
- Piping 
- Input/Output redirection

Note:
> There are many libraries that you could use to make this interpreter easier to implement. For example `argparse`, `cmd`, `plumbum`,`cli` and many many others. If you import a library that does most of the work for you, I will not give you credit for writing your own parser. We will however use **some** library support to give us access to the operating system. If you find a library and your not sure if you should use it, ask me.
>

### The os Library

Source: https://docs.python.org/2/library/os.html
This module provides a portable way of using operating system dependent functionality. If you just want to read or write a file see open(), if you want to manipulate paths, see the os.path module, and if you want to read all the lines in all the files on the command line see the fileinput module. For creating temporary files and directories see the tempfile module, and for high-level file and directory handling see the shutil module.



## Requirements

The following list of commands will be implemented:
- `cat` (list a file) [`cat filename`]
- `chmod` (change modify) [`chmod 777 filename`]
- `cd` (change directory) [`cd newDirectory`]
    - Options:
        - `..` (previous directory)
        - `~` (home directory)
- `cp` (copy file) [`cp file1 file2`]
- `history` (show command history) [`history`]
- `ls`  (file listing) [`ls -lt`] 
    - Flags:
        - No flag gives simple listing.
        - `-l` long listing
        - `-t` ordered by time

- `mv` (rename command) [`mv file1 to file2`]
- `rm` (remove a file) [`rm filename`] 
- `wc` (word count file) [`wc filename`]
    - Flags:
        - `-l` (number of lines) 
- ...


## Deliverables
