Python os.chdir() method



 **OS module** in Python provides functions for interacting with the operating
system. OS, comes under Python’s standard utility modules. This module
provides a portable way of using operating system dependent functionality.

 **os.chdir()** method in Python used to change the current working
directory to specified path. It takes only a single argument as new directory
path.

>  **Syntax:** os.chdir(path)
>
>  **Parameters:**  
>  **path:** A complete path of directory to be changed to new directory path.
>
>  **Returns:** Doesn’t return any value
>
>  
>
>
>  
>

 **Code #1:** Use chdir() to change the directory

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to change the

# directory of file using os.chdir() method

 

# import os library

import os

 

# change the current directory

# to specified directory

os.chdir(r"C:\Users\Gfg\Desktop\geeks")

 

print("Directory changed")  
  
---  
  
 __

 __

 **Output:**

    
    
    Directory changed

  
**Code #2:** Use of os.getcwd()  
To know the current working directory of the file, getcwd() method can be
used. After changing the path, one can verify the path of current working
directory using this method.

 __

 __  
 __

 __

 __  
 __  
 __

# import os module

import os

 

# change the current working directory 

# to specified path

os.chdir('c:\\gfg_dir')

 

# varify the path using getcwd()

cwd = os.getcwd()

 

# print the current directory

print("Current working directory is:", cwd)  
  
---  
  
 __

 __

 **Output:**

    
    
    Current working directory is: c:\\gfg_dir

  
**Code #3:** Handling the errors while changing the directory

 __

 __  
 __

 __

 __  
 __  
 __

# importing all necessary libraries

import sys, os

 

# initial directory

cwd = os.getcwd()

 

# some non existing directory

fd = 'false_dir / temp'

 

# trying to insert to flase directory

try:

 os.chdir(fd)

 print("Inserting inside-", os.getcwd())

 

# Caching the exception 

except:

 print("Something wrong with specified\

 directory. Exception- ", sys.exc_info())

 

# handling with finally 

finally:

 print("Restoring the path")

 os.chdir(cwd)

 print("Current directory is-", os.getcwd())  
  
---  
  
 __

 __

 **Output:**

    
    
    Inserting inside- c:\gfg_dir\gfg
    Something wrong with specified directory. Exception- 
    Restoring the path
    Current directory is- c:\gfg_dir\gfg

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

