# YO-Shell.v.1 (Your Own Shell) 
Due: TBD

# Not COMPLETE

## Overview

Your going to write your own command line interpreter using python. Your interpreter will implement a subset of the existing bash
commands that we use. We could do this in pretty much any language, in fact, "C" would be the language of choice if this were to 
be something that we would release to market, however, Python is a pretty stout language and will simplify the implementation of your
own Shell. This first version we will only implement a basic shell which sits a waits for commands. When the `enter` key is pressed, your shell will "parse" the command and execute it based on the name of the command and any additional flags included on the command line. Of course your shell should not "crash" if things don't go as expected, so you will need to handle all kinds of bad input. 

What we won't be implementing in this version is "autocompletion" or a "history" that allows a previous command to be loaded and then executed again. We will however provide a "history" command that simply shows the previous commands.

We also won't be implementing "piping" or input/output redirection. Those will come later.

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
