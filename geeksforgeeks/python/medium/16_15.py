Python | shutil.copyfile() method



 **Shutil module** in Python provides many functions of high-level operations
on files and collections of files. It comes under Python’s standard utility
modules. This module helps in automating process of copying and removal of
files and directories.

 _ **shutil.copyfile()**_ method in Python is used to copy the content of
_source_ file to _destination_ file. Metadata of the file is not copied.
_Source_ and _destination_ must represent a file and _destination_ must be
writable. If _destination_ already exists then it will be replaced with the
_source_ file otherwise a new file will be created.  
If _source_ and _destination_ represents the same file then _SameFileError_
exception will be raised.

>  ** _Syntax:_** shutil.copyfile(source, destination, *, follow_symlinks =
> True)
>
>  ** _Parameter:_**  
>  **source** : A string representing the path of the source file.  
>  **destination** : A string representing the path of the destination file.  
>  **follow_symlinks** (optional) : The default value of this parameter is
> True. If False and source represents a symbolic link then a new symbolic
> link will be created instead of copying the file.
>
>  **Note:** The ‘*’ in parameter list indicates that all following parameters
> (Here in our case ‘follow_symlinks’) are keyword-only parameters and they
> can be provided using their name, not as positional parameter.
>
>  
>
>
>  
>
>
>  ** _Return Type:_** This method returns a string which represents the path
> of newly created file.

 **Code #1:** Use of shutil.copyfile() method to copy file from source to
destination

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to explain shutil.copyfile() method

 

# importing os module 

import os

 

# importing shutil module 

import shutil

 

# path

path = '/home/User/Documents'

 

# List files and directories

# in '/home/User/Documents'

print("Before copying file:")

print(os.listdir(path))

 

 

# Source path

source = "/home/User/Documents/file.txt"

 

# Destination path

destination = "/home/User/Documents/file(copy).txt"

 

# Copy the content of

# source to destination

dest = shutil.copyfile(source, destination)

 

# List files and directories

# in "/home / User / Documents"

print("After copying file:")

print(os.listdir(path))

 

# Print path of newly 

# created file

print("Destination path:", dest)  
  
---  
  
 __

 __

 **Output:**

    
    
    Before copying file:
    ['hrithik.png', 'test.py', 'sample.txt', 'file.text', 'copy.cpp']
    After copying file:
    ['hrithik.png', 'test.py', 'sample.txt', 'file.text', 'file(copy).txt', 'copy.cpp']
    Destination path: /home/User/Documents/file(copy).txt
    

**Code #2:** Possible errors while using shutil.copyfile() method

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to explain shutil.copyfile() method

 

# importing shutil module 

import shutil

 

 

# If the source and destination

# represents the same file

# 'SameFileError' exception

# will be raised

 

# If the destination is

# is directory then

# 'IsADirectoryError' exception

# will be raised

 

# If the destination is

# not writable

# 'PermissionError' exception

# will be raised

 

 

# Source path

source = "/home/User/Documents/file.txt"

 

# Destination path

destination = "/home/User/Documents/file.txt"

 

# Copy the content of

# source to destination

shutil.copyfile(source, destintion)  
  
---  
  
 __

 __

 **Output:**

    
    
    Traceback (most recent call last):
      File "copy.py", line 31, in 
        shutil.copyfile(source, destination)
      File "/usr/lib/python3.6/shutil.py", line 104, in copyfile
        raise SameFileError("{!r} and {!r} are the same file".format(src, dst))
    shutil.SameFileError: '/home/User/Documents/file.txt' and '/home/User/Documents/file.txt'
    are the same file
    

**Code #3:** Handling errors while using shutil.copyfile() method

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to explain shutil.copyfile() method

 

# importing shutil module 

import shutil

 

# Source path

source = "/home/User/Documents/file.txt"

 

# Destination path

destination = "/home/User/Documents"

 

# Copy the content of

# source to destination

 

try:

 shutil.copyfile(source, destination)

 print("File copied successfully.")

 

# If source and destination are same

except shutil.SameFileError:

 print("Source and destination represents the same file.")

 

# If destination is a directory.

except IsADirectoryError:

 print("Destination is a directory.")

 

# If there is any permission issue

except PermissionError:

 print("Permission denied.")

 

# For other errors

except:

 print("Error occurred while copying file.")  
  
---  
  
 __

 __

 **Output:**

    
    
    Destination is a directory.
    

**Reference:** https://docs.python.org/3/library/shutil.html

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

