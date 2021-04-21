Python | os.remove() method



 **OS module** in Python provides functions for interacting with the operating
system. OS comes under Python’s standard utility modules. This module provides
a portable way of using operating system dependent functionality.

All functions in os module raise **OSError** in the case of invalid or
inaccessible file names and paths, or other arguments that have the correct
type, but are not accepted by the operating system.

 _ **os.remove()**_ method in Python is used to remove or delete a file
path. This method can not remove or delete a directory. If the specified path
is a directory then **OSError** will be raised by the method.
_**os.rmdir()**_ can be used to remove directory.

>  ** _Syntax:_** os.remove(path, *, dir_fd = None)
>
>  ** _Parameter:_**  
>  **path** : A path-like object representing a file path. A path-like object
> is either a string or bytes object representing a path.  
>  **dir_fd** (optional) : A file descriptor referring to a directory. The
> default value of this parameter is None.  
> If the specified path is absolute then dir_fd is ignored.
>
>  
>
>
>  
>
>
>  **Note:** The ‘*’ in parameter list indicates that all following parameters
> (Here in our case ‘dir_fd’) are keyword-only parameters and they can be
> provided using their name, not as positional parameter.
>
>  ** _Return Type:_** This method does not return any value.

 **Code #1:** Use of os.remove() method to remove a file

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

file = 'file.txt'

 

# File location

location = "/home/User/Documents"

 

# Path

path = os.path.join(location, file)

 

# Remove the file

# 'file.txt'

os.remove(path)

print("%s has been removed successfully" %file)  
  
---  
  
 __

 __

 **Output:**

    
    
    file.txt has been removed successfully
    

**Code #2:** If the specified path is a directory

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

 

# Path

path = "/home/User/Documents/ihritik"

 

# Remove the specified

# file path

os.remove(path)

print("% s has been removed successfully" % file)

 

# if the specified path 

# is a directory then 

# 'IsADirectoryError' error

# will raised 

 

# Similarly if the specified

# file path does not exists or 

# is invalid then corresponding

# OSError will be raised  
  
---  
  
 __

 __

 **Output:**

    
    
    Traceback (most recent call last):
      File "osremove.py", line 11, in 
        os.remove(path)
    IsADirectoryError: [Errno 21] Is a directory: '/home/User/Documents/ihritik'
    

**Code #3:** Handling error while using os.remove() method

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

 

# path

path = '/home/User/Documents/ihritik'

 

# Remove the specified 

# file path

try:

 os.remove(path)

 print("% s removed successfully" % path)

except OSError as error:

 print(error)

 print("File path can not be removed")  
  
---  
  
 __

 __

 **Output:**

    
    
    [Errno 21] Is a directory: '/home/User/Documents/ihritik'
    File path can not be removed
    

**Reference:** https://docs.python.org/3/library/os.html

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

