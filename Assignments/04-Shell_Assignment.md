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

We will break a sentence (string) into it's parts:

- command
- arguments
- flags


- Command - This is the part of the string that tells the interpreter what specific action it wants to perform. This is the first item in the string. 
- Arguments - This is one or more items that the command needs to perform it's action. They typically follow the command but they don't always have to. 


What we won't implement in Version 1:
- Autocompletion
- Piping 
- Input/Output redirection

Note:
> There are many libraries that you could use to make this easier to implement. For example `argparse`, `cmd`, `plumbum`,`cli` and many many others. If you import a library that does most of the work for you, I will not give you credit for writing your own parser. 



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
