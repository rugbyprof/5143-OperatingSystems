# YO-Shell.v.1 
### (Your Own Shell) 
Due: TBD

# Not COMPLETE

## Overview

Your going to write your own command line interpreter using python. Your interpreter will implement a subset of the existing bash
commands that we use. We could do this in pretty much any language, in fact, "C" would be the language of choice if this were to 
be something that we would release to market, however, Python is a pretty stout language and will simplify the implementation of your
own Shell. 

A command line interpreter contains a key component: ***The Parser***. This is the backbone of every "shell" or "cli". 

The definition of `parse` is: 
>- verb 
    - Analyze (a sentence) into its parts and describe their syntactic roles.
- noun (COMPUTING)
    - An act of or the result obtained by parsing a string or a text.

Basically `YO-Shell` will break a sentence (string) into it's main components: **1)** command **2)** arguments **3)** flags

#### Command:

- This is the part of the string that tells the interpreter what specific action it wants to perform. 
- This is the first item in the string. 

#### Arguments:

- This is one or more items that the command needs to perform it's action. 
- They typically follow the command but they don't always have to, meaning a 'flag' be be in front of the arguments (e.g. `mkdir -p /new/stuff/dir`)
- An example is: `cp file1.txt file2.txt` where `file1.txt` is the first argument and `file2.txt` is the second argument. 
- If one of the mandatory arguments isn't present, your shell should handle this with an error message, and not crash.

#### Flags:
- These alter a command in specific ways. 
- Flags should start with a `-` and should be followed by one or more "flags".
- A flag could be a single letter like: `ls -l` where the `-l` specifies "long listing".
- A flag can be multiple letters like: `ls -la` or `ls -l -a` which both perform "long listings of all files".
- Sometimes a flag can be a word, but when words are used, it typically follows this format: `grep --color=always  abc  a_file.txt`.
- We won't implement this type of flag.

For `YO-Shell` version 1 we will implement the following: 

1. Provide a prompt and wait for a command to be entered. 
2. When the `enter` key is pressed, you will "parse" the command into its parts.
3. Then based on the "command", its arguments, and any additional flags included on the command line, it will be executed. 
4. Of course your shell should not "crash" if things don't go as expected, so you will need to handle bad input:
    - Missing arguments
    - Misspelled commands
    - Unknown flags
    - Badly formatted commands

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

- You will write a command line interpreter (Shell) that will allow a user to excecute the following commands:
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
- You may work by yourself, or in a group of 2 - 3.  


## Deliverables

- Create a folder called `YO-Shell.v.1` in your home directory.
- Create a file called `parser.py` inside this folder.
- Place all necessary code in `parser.py` to fulfill the requirements. 
- Push your code to your github repository.  
- If in a group, all members need to have the code in thier repository.
- I won't grade projects that are not both on the server, and github. 
-  ...
