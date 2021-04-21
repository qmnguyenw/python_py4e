OS Module in Python with Examples



The OS module in Python provides functions for interacting with the operating
system. OS comes under Python’s standard utility modules. This module provides
a portable way of using operating system-dependent functionality. The *os* and
*os.path* modules include many functions to interact with the file system.

## Handling the Current Working Directory

Consider **Current Working Directory(CWD)** as a folder, where the Python is
operating. Whenever the files are called only by their name, Python assumes
that it starts in the CWD which means that name-only reference will be
successful only if the file is in the Python’s CWD.

 **Note:** The folder where the Python script is running is known as the
Current Directory. This is not the path where the Python script is located.

 **Getting the Current working directory**

To get the location of the current working directory os.getcwd() is used.

  

  

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to explain os.getcwd() method

 

# importing os module 

import os 

 

# Get the current working 

# directory (CWD) 

cwd = os.getcwd() 

 

# Print the current working 

# directory (CWD) 

print("Current working directory:", cwd)   
  
---  
  
__

__

**Output:**

    
    
    Current working directory: /home/nikhil/Desktop/gfg

 **Changing the Current working directory**

To change the current working directory(CWD) os.chdir() method is used. This
method changes the CWD to a specified path. It only takes a single argument as
a new directory path.

 **Note:** The current working directory is the folder in which the Python
script is operating.

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to change the

# current working directory 

 

 

import os 

 

# Function to Get the current 

# working directory 

def current_path(): 

 print("Current working directory before") 

 print(os.getcwd()) 

 print() 

 

 

# Driver's code 

# Printing CWD before 

current_path() 

 

# Changing the CWD 

os.chdir('../') 

 

# Printing CWD after 

current_path()   
  
---  
  
__

__

**Output:**

    
    
    Current working directory before
    C:\Users\Nikhil Aggarwal\Desktop\gfg
    
    Current working directory after
    C:\Users\Nikhil Aggarwal\Desktop
    

## Creating a Directory

There are different methods available in the OS module for creating a
director. These are –

  

  

  * os.mkdir()
  * os.makedirs()

 **Using os.mkdir()**

os.mkdir() method in Python is used to create a directory named path with the
specified numeric mode. This method raise FileExistsError if the directory to
be created already exists.

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to explain os.mkdir() method

 

# importing os module 

import os 

 

# Directory 

directory = "GeeksforGeeks"

 

# Parent Directory path 

parent_dir = "D:/Pycharm projects/"

 

# Path 

path = os.path.join(parent_dir, directory) 

 

# Create the directory 

# 'GeeksForGeeks' in 

# '/home / User / Documents' 

os.mkdir(path) 

print("Directory '% s' created" % directory) 

 

# Directory 

directory = "Geeks"

 

# Parent Directory path 

parent_dir = "D:/Pycharm projects"

 

# mode 

mode = 0o666

 

# Path 

path = os.path.join(parent_dir, directory) 

 

# Create the directory 

# 'GeeksForGeeks' in 

# '/home / User / Documents' 

# with mode 0o666 

os.mkdir(path, mode) 

print("Directory '% s' created" % directory)   
  
---  
  
__

__

**Output:**

    
    
    Directory 'GeeksforGeeks' created
    Directory 'Geeks' created

 **Using os.makedirs()**

os.makedirs() method in Python is used to create a directory recursively. That
means while making leaf directory if any intermediate-level directory is
missing, os.makedirs() method will create them all.

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to explain os.makedirs() method

 

# importing os module 

import os 

 

# Leaf directory 

directory = "Nikhil"

 

# Parent Directories 

parent_dir = "D:/Pycharm projects/GeeksForGeeks/Authors"

 

# Path 

path = os.path.join(parent_dir, directory) 

 

# Create the directory 

# 'Nikhil' 

os.makedirs(path) 

print("Directory '% s' created" % directory) 

 

# Directory 'GeeksForGeeks' and 'Authors' will 

# be created too 

# if it does not exists 

 

 

 

# Leaf directory 

directory = "c"

 

# Parent Directories 

parent_dir = "D:/Pycharm projects/GeeksforGeeks/a/b"

 

# mode 

mode = 0o666

 

path = os.path.join(parent_dir, directory) 

 

# Create the directory 'c' 

 

os.makedirs(path, mode) 

print("Directory '% s' created" % directory) 

 

 

# 'GeeksForGeeks', 'a', and 'b' 

# will also be created if 

# it does not exists 

 

# If any of the intermediate level 

# directory is missing 

# os.makedirs() method will 

# create them 

 

# os.makedirs() method can be 

# used to create a directory tree   
  
---  
  
__

__

**Output:**

    
    
    Directory 'Nikhil' created
    Directory 'c' created
    

## Listing out Files and Directories with Python

 **os.listdir()** method in Python is used to get the list of all files and
directories in the specified directory. If we don’t specify any directory,
then list of files and directories in the current working directory will be
returned.

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to explain os.listdir() method

 

# importing os module 

import os 

 

# Get the list of all files and directories 

# in the root directory 

path = "/"

dir_list = os.listdir(path) 

 

print("Files and directories in '", path, "' :") 

 

# print the list 

print(dir_list)   
  
---  
  
__

__

**Output:**

    
    
    Files and directories in ' / ' :
    ['sys', 'run', 'tmp', 'boot', 'mnt', 'dev', 'proc', 'var', 'bin', 'lib64', 'usr', 
    'lib', 'srv', 'home', 'etc', 'opt', 'sbin', 'media']

## Deleting Directory or Files using Python

OS module proves different methods for removing directories and files in
Python. These are –

  * Using os.remove()
  * Using os.rmdir()

 **Using os.remove()**

os.remove() method in Python is used to remove or delete a file path. This
method can not remove or delete a directory. If the specified path is a
directory then OSError will be raised by the method.

 **Example:** Suppose the file contained in the folder are:

![](https://media.geeksforgeeks.org/wp-content/uploads/20191125183910/python-
os.remove-input.png)

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to explain os.remove() method

 

# importing os module 

import os 

 

# File name 

file = 'file1.txt'

 

# File location 

location = "D:/Pycharm projects/GeeksforGeeks/Authors/Nikhil/"

 

# Path 

path = os.path.join(location, file) 

 

# Remove the file 

# 'file.txt' 

os.remove(path) 

e)  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-content/uploads/20191125184203/python-
os.remove-output.png)

 **Using os.rmdir()**

os.rmdir() method in Python is used to remove or delete a empty directory.
OSError will be raised if the specified path is not an empty directory.

 **Example:** Suppose the directories are –

![](https://media.geeksforgeeks.org/wp-content/uploads/20191125192432/python-
os.rmdir-input.png)

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to explain os.rmdir() method

 

# importing os module 

import os 

 

# Directory name 

directory = "Geeks"

 

# Parent Directory 

parent = "D:/Pycharm projects/"

 

# Path 

path = os.path.join(parent, directory) 

 

# Remove the Directory 

# "Geeks" 

os.rmdir(path)   
  
---  
  
__

__

**Output:**

![](https://media.geeksforgeeks.org/wp-content/uploads/20191125192658/python-
os.rmdir-output.png)

## Commonly Used Functions

 **1\. os.name:** This function gives the name of the operating system
dependent module imported. The following names have currently been registered:
‘posix’, ‘nt’, ‘os2’, ‘ce’, ‘java’ and ‘riscos’

 __

 __  
 __

 __

 __  
 __  
 __

import os

 

print(os.name)  
  
---  
  
 __

 __

 **Output:**

    
    
    posix
    

**Note:** It may give different output on different interpreters, such as
‘posix’ when you run the code here.

 **2\. os.error:** All functions in this module raise OSError in the case of
invalid or inaccessible file names and paths, or other arguments that have the
correct type, but are not accepted by the operating system. os.error is an
alias for built-in OSError exception.

 __

 __  
 __

 __

 __  
 __  
 __

import os

 

 

try:

 # If the file does not exist,

 # then it would throw an IOError

 filename = 'GFG.txt'

 f = open(filename, 'rU')

 text = f.read()

 f.close()

 

# Control jumps directly to here if 

# any of the above lines throws IOError. 

except IOError:

 

 # print(os.error) will <class 'OSError'>

 print('Problem reading: ' + filename)

 

# In any case, the code then continues with 

# the line after the try/except  
  
---  
  
 __

 __

 **Output:**

    
    
    Problem reading: GFG.txt
    

**3\. os.popen():** This method opens a pipe to or from command. The return
value can be read or written depending on whether mode is ‘r’ or ‘w’.  
 **Syntax:**

    
    
     os.popen(command[, mode[, bufsize]])

Parameters mode & bufsize are not necessary parameters, if not provided,
default ‘r’ is taken for mode.

 __

 __  
 __

 __

 __  
 __  
 __

import os

fd = "GFG.txt"

 

# popen() is similar to open()

file = open(fd, 'w')

file.write("Hello")

file.close()

file = open(fd, 'r')

text = file.read()

print(text)

 

# popen() provides a pipe/gateway and accesses the file directly

file = os.popen(fd, 'w')

file.write("Hello")

# File not closed, shown in next function.  
  
---  
  
 __

 __

 **Output:**

    
    
    Hello
    

**Note:** Output for popen() will not be shown, there would be direct changes
into the file.

 **4\. os.close():** Close file descriptor fd. A file opened using open(), can
be closed by close()only. But file opened through os.popen(), can be closed
with close() or os.close(). If we try closing a file opened with open(), using
os.close(), Python would throw TypeError.

 __

 __  
 __

 __

 __  
 __  
 __

import os

 

 

fd = "GFG.txt"

file = open(fd, 'r')

text = file.read()

print(text)

os.close(file)  
  
---  
  
 __

 __

 **Output:**

    
    
    Traceback (most recent call last):
      File "C:\Users\GFG\Desktop\GeeksForGeeksOSFile.py", line 6, in 
        os.close(file)
    TypeError: an integer is required (got type _io.TextIOWrapper)
    

Note: The same error may not be thrown, due to non-existent of file or
permission privilege.

 **5\. os.rename():** A file old.txt can be renamed to new.txt, using the
function os.rename(). The name of the file changes only if, the file exists
and user has sufficient privilege permission to change the file.

 __

 __  
 __

 __

 __  
 __  
 __

import os

 

 

fd = "GFG.txt"

os.rename(fd,'New.txt')

os.rename(fd,'New.txt')  
  
---  
  
 __

 __

 **Output:**

    
    
    
    Traceback (most recent call last):
      File "C:\Users\GFG\Desktop\ModuleOS\GeeksForGeeksOSFile.py", line 3, in 
        os.rename(fd,'New.txt')
    FileNotFoundError: [WinError 2] The system cannot find the
    file specified: 'GFG.txt' -> 'New.txt'
    

**Understanding the Output:** A file name “GFG.txt” exists, thus when
os.rename() is used the first time, the file gets renamed. Upon calling the
function os.rename() second time, file “New.txt” exists and not “GFG.txt”  
thus Python throws FileNotFoundError.

This article is contributed by **Piyush Doorwar**. If you like GeeksforGeeks
and would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

