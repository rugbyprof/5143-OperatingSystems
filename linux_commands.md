
## List files

```
ls
```
The ls command ( lowercase L and lowercase S ) lists the contents of your current working directory.

```
ls -a
```
As you can see, ls -a lists files that are normally hidden.

```
ls -la
```
As you can see, ls -a lists files that are normally hidden and in a log form (shows permissions and ownership).

## Make Directory

```
mkdir dirname
```
Make a directory (folder)

## Changing Directory

```
cd dirname
```
Change into the directory dirname

```
cd .
```
Change directory into the current directory (the . represents "here")

```
cd ..
```
Change directory into the previous directory (the .. represents "one back")

```
cd 
```
By itself, `cd` means take me to my home directory

```
cd ~
```
Another way of changing to your home directory in an explicit way. So the `~` represents `home`.

## Print Working Directory

```
pwd
```
Print working directory (shows the path of your current location)

## Examples 1

```
ls ~   
```
List all files in my home directory

```
ls ~/..
```
List all files of the parent to my home directory

| Command	      | Meaning                                       |
|---------------|------------------------------------------------|
| ls	          | list files and directories                    |
| ls -a	        | list all files and directories                |
| mkdir	        | make a directory                              |
| cd directory	| change to named directory                     |
| cd	          | change to home-directory                      |
| cd ~	        | change to home-directory                      |
| cd ..	        | change to parent directory                    | 
| pwd	          | display the path of the current directory     |
