# Not Complete

Shell Project
=============

## Overview

How does the shell execute a user command? It interactively follows the steps given below:
- After start-up processing, your program repeatedly should perform these actions:
- Print to stdout a prompt consisting of a percent sign followed by a space.
- Read a line from stdin.
- Lexically analyze the line to form an array of tokens.
- Syntactically analyze (i.e. parse) the token array to form a command.
- It creates a child process by duplicating itself.
- The overloaded process receives all the remaining strings given from a keyboard input, and starts a command execution.

Your shell must support the following types of commands:

1. The internal shell command "exit" which terminates the shell.
    - Concepts: shell commands, exiting the shell
    - System calls: `exit()`
2. A command with no arguments
    - Example: `ls`
    - Details: Your shell must block until the command completes and, if the return code is abnormal, print out a message to that effect.
    - Concepts: Forking a child process, waiting for it to complete, synchronous execution
    - System calls: `fork()`, `execvp()`, `exit()`, `wait()`
1. A command with arguments
    - Example: `ls -l`
    - Details: Argument 0 is the name of the command
    - Concepts: Command-line parameters 
2. A command, with or without arguments, executed in the background using `&`.
    - For simplicity, assume that if present the `&` is always the last thing on the line.
    - Example: `xemacs &`
    - Details: In this case, your shell must execute the command and return immediately, not blocking until the command finishes.
    - Concepts: Background execution, signals, signal handlers, processes, asynchronous execution
    - System calls: `sigset()`
3. A command, with or without arguments, whose output is redirected to a file
    - Example: `ls -l > foo`
    - Details: This takes the output of the command and put it in the named file
    - Concepts: File operations, output redirection
    - System calls: `freopen()`
4. A command, with or without arguments, whose input is redirected from a file
    - Example: `sort < testfile`
    - Details: This takes the named file as input to the command
    - Concepts: Input redirection, more file operations
    - System calls: `freopen()`
5. A command, with or without arguments, whose output is piped to the input of another command.
    - Example: `ls -l | more`
    - Details: This takes the output of the first command and makes it the input to the second command
    - Concepts: Pipes, synchronous operation
    - System calls: `pipe()`

Note: You must check and correctly handle all return values. This means that you need to read the man pages for each function to figure out what the possible return values are, what errors they indicate, and what you must do when you get that error

## Commands To Implement

| Command	      | Meaning                                       |
|---------------|------------------------------------------------|
| `ls	`          | list files and directories                    |
| `ls -a`	        | list all files and directories                |
| `mkdir`	        | make a directory                              |
| `cd directory`	| change to named directory                     |
| `cd`	          | change to home-directory                      |
| `cd ~	`        | change to home-directory                      |
| `cd ..`	        | change to parent directory                    | 
| `pwd`	          | display the path of the current directory     |

| Command | Meaning                                  |
|---------|------------------------------------------|
| `cp file1 file2`    | copy file1 and call it file2 |
| `mv file1 file2`    | move or rename file1 to file2 |
| `rm file`           | remove a file |
| `rmdir directory`  | remove a directory |
| `cat file` | display a file |
| `less file` | display a file a page at a time |
| `head file` | display the first few lines of a file |
| `tail file` | display the last few lines of a file |
| `grep 'keyword' file` | search a file for keywords |
| `wc file` | count number of lines/words/characters in file |

| Command | Meaning |
|--------------------------|---------|
| `command > file`           | redirect standard output to a file |
| `command >> file`          | append standard output to a file |
| `command < file`           | redirect standard input from a file |
| `command1 | command2`      | pipe the output of command1 to the input of command2 |
| `cat file1 file2 > file0`  | concatenate file1 and file2 to file0 |
| `sort`                     | sort data |
| `who`                      | list users currently logged in |

| Command | Meaning |
|--------------------------|---------|
| `history`           | show a history of all your commands |
| `!x`                | this loads command `x` from your history so you can run it again |
| `chmod xxx`         | change modify permission | 

