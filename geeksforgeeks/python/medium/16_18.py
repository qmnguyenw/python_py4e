Python | os.path.split() method



 **OS module** in Python provides functions for interacting with the operating
system. OS comes under Python’s standard utility modules. This module provides
a portable way of using operating system dependent functionality. **os.path**
module is submodule of **OS module** in Python used for common pathname
manipulation.

 _ **os.path.split()**_ method in Python is used to Split the path name into
a pair _head_ and _tail_. Here, _tail_ is the last path name component and
_head_ is everything leading up to that.

For example consider the following path name:

    
    
    path name = '/home/User/Desktop/file.txt'
    

In the above example _‘file.txt’_ component of path name is _tail_ and
_‘/home/User/Desktop/’_ is head.The tail part will never contain a slash; if
name of the path ends with a slash, tail will be empty and if there is no
slash in path name, head will be empty.

 **For example:**

  

  

    
    
         **path**                             **head**                 **tail**
    '/home/user/Desktop/file.txt'   '/home/user/Desktop/'   'file.txt'
    '/home/user/Desktop/'           '/home/user/Desktop/'    {empty}
    'file.txt'                           {empty}            'file.txt'
    

> **_Syntax:_** os.path.split(path)
>
>  ** _Parameter:_**  
>  **path** : A path-like object representing a file system path. A path-like
> object is either a _str_ or _bytes_ object representing a path.
>
>  ** _Return Type:_** This method returns a tuple that represents head and
> tail of the specified path name.

 **Code #1:** Use of os.path.split() method

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to explain os.path.split() method

 

# importing os module 

import os

 

# path

path = '/home/User/Desktop/file.txt'

 

# Split the path in 

# head and tail pair

head_tail = os.path.split(path)

 

# print head and tail

# of the specified path

print("Head of '% s:'" % path, head_tail[0])

print("Tail of '% s:'" % path, head_tail[1], "\n")

 

 

# path

path = '/home/User/Desktop/'

 

# Split the path in 

# head and tail pair

head_tail = os.path.split(path)

 

# print head and tail

# of the specified path

print("Head of '% s:'" % path, head_tail[0])

print("Tail of '% s:'" % path, head_tail[1], "\n")

 

# path

path = 'file.txt'

 

# Split the path in 

# head and tail pair

head_tail = os.path.split(path)

 

# print head and tail

# of the specified path

print("Head of '% s:'" % path, head_tail[0])

print("Tail of '% s:'" % path, head_tail[1])  
  
---  
  
 __

 __

 **Output:**

    
    
    Head of '/home/User/Desktop/file.txt': /home/User/Desktop
    Tail of '/home/User/Desktop/file.txt': file.txt 
    
    Head of '/home/User/Desktop/': /home/User/Desktop
    Tail of '/home/User/Desktop/':  
    
    Head of 'file.txt': 
    Tail of 'file.txt': file.txt
    

**Code #2:** If path is empty

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to explain os.path.split() method

 

# importing os module 

import os

 

# path

path = ''

 

# Split the path in 

# head and tail pair

head_tail = os.path.split(path)

 

# print head and tail

# of the specified path

print("Head of '% s':" % path, head_tail[0])

print("Tail of '% s':" % path, head_tail[1])

 

 

# os.path.split() function

# will return empty

# head and tail if 

# specified path is empty  
  
---  
  
 __

 __

 **Output:**

    
    
    Head of '': 
    Tail of '':
    

**Reference:** https://docs.python.org/3/library/os.path.html

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

