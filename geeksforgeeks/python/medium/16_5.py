Python | os.write() method



 **OS module** in Python provides functions for interacting with the operating
system. OS comes under Python’s standard utility modules. This module provides
a portable way of using operating system dependent functionality.

 _ **os.write()**_ method in Python is used to write a bytestring to the
given file descriptor.

A _file descriptor_ is small integer value that corresponds to a file that has
been opened by the current process. It is used to perform various lower level
I/O operations like read, write, send etc.

 **Note** : _**os.write()**_ method is intended for low-level operation and
should be applied to a file descriptor as returned by _**os.open()**_ or
_**os.pipe()**_ method.

>  ** _Syntax:_** os.write(fd, str)
>
>  
>
>
>  
>
>
>  ** _Parameter:_**  
>  **fd** : The file descriptor representing the target file.  
>  **str** : A bytes-like object to be written in the file.
>
>  ** _Return Type:_** This method returns an integer value which represents
> the number of bytes actually written.

 **Code:** Use of os.write() method to write a bytestring to a given file
descriptor

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to explain os.write() method

 

# importing os module 

import os

 

# File path 

path = "/home / ihritik / Documents / GeeksForGeeks.txt"

 

 

# Open the file and get

# the file descriptor associated

# with it using os.open() method

fd = os.open(path, os.O_RDWR)

 

 

# String to be written

s = "GeeksForGeeks: A Computer science portal for Geeks."

 

# Convert the string to bytes

line = str.encode(s)

 

# Write the bytestring to the file

# associated with the file

# descriptor fd and get the number of

# Bytes actually written

numBytes = os.write(fd, line)

 

print("Number of bytes written:", numBytes)

 

# close the file descriptor

os.close(fd)  
  
---  
  
 __

 __

 **Output:**

    
    
    Number of bytes written: 51
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

