# Bash Assignment 1
Due: Wednesday February 10th by Class time.


### Prep Work

1. Login to **cs2.mwsu.edu** and change your password. Make sure it is secure. If I can run a script that breaks your password, you will get a 0 on this entire assignment.
2. Create a folder called `public_html` in your home directory. Set the permissions on this folder to be `755`.
3. Create a folder called `5143_Opsys` in your home directory. Set the permissions on this folder to be `755`.
4. All subsequent assignments for this course will be in this folder.


### Script 1

- Create a script called `command_args.sh` which will read in all command line arguments and print them out.
- For example `$ ./command_args.sh arg1 "hello" 44` would print out:

```
command_args.sh
(contents of arg1)
hello
44
```



### Script 2


- Create a script which will print a random word. There is a file containing a list of words on your system (usually /usr/share/dict/words or /usr/dict/words). Hint: Piping will be useful here.
- Name this script: `random.sh` and when run, should print out 1 random word to std out.

>Update!! Words are located at **`/usr/share/dict`** in a file called **`words`**

### Script 3 

- Create a script which will take a filename as its first argument and create a dated copy of the file. eg. if the file was named `file1.txt` it would create a copy such as `2016-01-28_file1.txt`. (To achieve this you will probably want to play with command substitution and the command date).
- Name this script `versiona.sh`.

### Script 4

- Using the script from `versiona.sh`, see if you can get it so that the date is after the name of the file (eg. file1_2016-01-28.txt (The command `basename` can be useful here.)
- Name this script `versionb.sh`. 
