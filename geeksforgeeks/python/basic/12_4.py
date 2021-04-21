Python | os.path.relpath() method



 **OS module** in Python provides functions for interacting with the operating
system. OS comes under Python’s standard utility modules. This module provides
a portable way of using operating system dependent functionality. **os.path**
module is sub module of **OS module** in Python used for common path name
manipulation.

 _ **os.path.relpath()**_ method in Python is used to get a relative
filepath to the given path either from the current working directory or from
the given directory.

 **Note:** This method only computes the relative path. The existence of the
given path or directory is not checked.

>  ** _Syntax:_** os.path.relpath(path, start = os.curdir)
>
>  ** _Parameter:_**  
>  **path** : A path-like object representing the file system path.  
>  **start** (optional): A path-like object representing the file system path.  
> The relative path for given path will be computed with respect to the
> directory indicated by start. The default value of this parameter is
> os.curdir which is a constant string used by the operating system to refer
> to the current directory.
>
>  
>
>
>  
>
>
> A path-like object is either a _string_ or _bytes_ object representing a
> path.
>
>  ** _Return Type:_** This method returns a string value which represents the
> relative file path to given path from the start directory.

 **Code :** Use of os.path.relpath() method

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to explain os.path.relpath() method

 

# importing os module 

import os

 

# Path

path = "/home / User / Desktop / file.txt"

 

# Path of Start directory

start = "/home / User"

 

# Compute the relative file path

# to the given path from the 

# the given start directory.

relative_path = os.path.relpath(path, start)

 

# Print the relative file path

# to the given path from the 

# the given start directory.

print(relative_path)

 

 

 

# Path

path = "/home / User / Desktop / file.txt"

 

# Compute the relative file path

# to the given path from the 

# the current directory.

 

# if we do not specify the start

# parameter it will default to

# os.curdir i.e current directory 

relative_path = os.path.relpath(path)

 

# Print the relative file path

# to the given path from the 

# the given start directory.

print(relative_path)

 

 

# Path

path = "/home / User / Desktop / file.txt"

 

# Path of Start directory

start = "GeeksForGeeks / home"

 

# Compute the relative file path

# to the given path from the 

# the given start directory.

relative_path = os.path.relpath(path, start)

 

# Print the relative file path

# to the given path from the 

# the given start directory.

print(relative_path)

 

 

# Path

path = "/home / User / Desktop / file.txt"

 

# Path of Start directory

start = "/home / User / ihritik / file.txt"

 

# Compute the relative file path

# to the given path from the 

# the given start directory.

relative_path = os.path.relpath(path, start)

 

# Print the relative file path

# to the given path from the 

# the given start directory.

print(relative_path)  
  
---  
  
 __

 __

 **Output:**

    
    
    Desktop/file.txt
    ../User/Desktop/file.txt
    ../../../User/Desktop/file.txt
    ../../Desktop/file.txt
    

**Reference:** https://docs.python.org/3/library/os.path.html

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

