Python | os.path.splitext() method



 **OS module** in Python provides functions for interacting with the operating
system. OS comes under Python’s standard utility modules. This module provides
a portable way of using operating system dependent functionality. **os.path**
module is submodule of **OS module** in Python used for common pathname
manipulation.

 _ **os.path.splitext()**_ method in Python is used to split the path name
into a pair _root_ and _ext_. Here, _ext_ stands for extension and has the
extension portion of the specified path while _root_ is everything except
_ext_ part.  
 _ext_ is empty if specified path does not have any extension. If the
specified path has leading period (‘.’), it will be ignored.

For example consider the following path names:

    
    
          **path name**                          **root**                        **ext**
    /home/User/Desktop/file.txt    /home/User/Desktop/file              .txt
    /home/User/Desktop             /home/User/Desktop                  {empty}
    file.py                               file                          .py
    .txt                                  .txt                         {empty}   
    

> **_Syntax:_** os.path.splitext(path)
>
>  ** _Parameter:_**  
>  **path** : A path-like object representing a file system path. A path-like
> object is either a _str_ or _bytes_ object representing a path.
>
>  
>
>
>  
>
>
>  ** _Return Type:_** This method returns a tuple that represents root and
> ext part of the specified path name.

 **Code:** Use of os.path.splitext() method

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to explain os.path.splitext() method

 

# importing os module 

import os

 

# path

path = '/home/User/Desktop/file.txt'

 

# Split the path in 

# root and ext pair

root_ext = os.path.splitext(path)

 

# print root and ext

# of the specified path

print("root part of '% s':" % path, root_ext[0])

print("ext part of '% s':" % path, root_ext[1], "\n")

 

 

# path

path = '/home/User/Desktop/'

 

# Split the path in 

# root and ext pair

root_ext = os.path.splitext(path)

 

# print root and ext

# of the specified path

print("root part of '% s':" % path, root_ext[0])

print("ext part of '% s':" % path, root_ext[1])  
  
---  
  
 __

 __

 **Output:**

    
    
    root part of '/home/User/Desktop/file.txt': /home/User/Desktop/file
    ext part of '/home/User/Desktop/file.txt': .txt 
    
    root part of '/home/User/Desktop/': /home/User/Desktop/
    ext part of '/home/User/Desktop/': 
    

**Reference:** https://docs.python.org/3/library/os.path.html

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

