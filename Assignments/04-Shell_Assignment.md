# YO-Shell.v.1 
**(Your Own Shell)** 

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
    - `ls`  (directory listing) [`ls -lt`] 
        - Flags:
            - No flag gives simple listing.
            - `-l` long listing (one file per row and shows size , permissions, and  creation date)
            - `-s` ordered by size (one file per row and shows size, permission, atime, mtime and ctime)
            - `-a` ordered by atime (one file per row and shows size, permission, atime, mtime and ctime)
            - `-m` ordered by mtime (one file per row and shows size, permission, atime, mtime and ctime)
            - `-c` ordered by ctime (one file per row and shows size, permission, atime, mtime and ctime)
    - `mv` (rename command) [`mv file1 to file2`]
    - `rm` (remove a file) [`rm filename`] 
    - `wc` (word count file) [`wc filename`]
        - Flags:
            - `-l` (number of lines) 
    - ...

### Example Outputs

**cp**
```
$ cp file1.mp3 file2.mp3
Copy successful.
$ 
```

**ls**
```
$ ls

File Listing 
-----------
Office_Ins.pkg 	    VS2013_RTM.iso 	Win10_Engl.iso 	en_visio_p.iso 	en_windows.iso 	texas-late.osm 	
us_roads2.mssql 	vs2015.com.iso 	Office_Ins.pkg 
-----------
$
```
**ls -l**
```
$ ls -l
File Name   Size    Permissions Accessed                    Modified                Changed
---------   -----   ----------- --------------------        --------------------    --------------------
Office_Ins 	1.02G 	640 		Feb:04:2016 04:29:56 		Nov:10:2015 09:30:20 	Jan:24:2016 11:50:19
VS2013_RTM 	2.76G 	777 		Feb:11:2016 04:09:25 		Jan:14:2016 03:47:10 	Feb:18:2016 12:32:22
Win10_Engl 	3.8G 	644 		Jan:12:2016 09:02:08 		Jul:31:2015 09:35:42 	Nov:06:2015 10:10:17
en_visio_p 	2.26G 	644 		Jan:08:2016 01:58:01 		Jan:08:2016 02:06:30 	Jan:08:2016 02:06:30
en_windows 	2.66G 	644 		Jan:13:2016 12:28:12 		Jan:13:2016 12:38:38 	Jan:13:2016 12:38:38
texas-late 	4.32G 	640 		Dec:16:2015 04:11:37 		Nov:10:2015 06:27:53 	Nov:11:2015 04:37:05
us_roads2. 	972.12M 640 		Jan:19:2016 10:56:22 		Nov:19:2015 03:17:29 	Nov:19:2015 03:17:29
vs2015.com 	3.69G 	644 		Feb:16:2016 03:11:49 		Jan:07:2016 10:54:22 	Jan:07:2016 10:54:22
$
```
- **ls -a** = same as `ls -l` but sorted by accessed time.
- **ls -m** = same as `ls -l` but sorted by modified time.
- **ls -c** = same as `ls -c` but sorted by changed time.


- You may work by yourself, or in a group of 2 - 3.  


## Deliverables

- Create a folder called `YO-Shell.v.1` in your home directory.
- Create a file called `shell.py` inside this folder.
- Place all necessary code in `shell.py` to fulfill the requirements. 
- Push your code to your github repository.  
- If in a group, all members need to have the code in thier repository.
- I won't grade projects that are not both on the server, and github. 
-  ...
