Python | os.path.join() method



 **OS module** in Python provides functions for interacting with the operating
system. OS comes under Python’s standard utility modules. This module provides
a portable way of using operating system dependent functionality. **os.path**
module is sub-module of OS module in Python used for common pathname
manipulation.

 _ **os.path.join()**_ method in Python join one or more path components
intelligently. This method concatenates various path components with exactly
one directory separator (‘/’) following each non-empty part except the last
path component. If the last path component to be joined is empty then a
directory seperator (‘/’) is put at the end.  
If a path component represents an absolute path, then all previous components
joined are discarded and joining continues from the absolute path component.

>  ** _Syntax:_** os.path.join(path, *paths)
>
>  ** _Parameter:_**  
>  **path** : A path-like object representing a file system path.  
>  ***path** : A path-like object representing a file system path. It
> represents the path components to be joined.  
> A path-like object is either a string or bytes object representing a path.
>
>  **Note:** The special syntax *args (here *paths) in function definitions in
> python is used to pass a variable number of arguments to a function.
>
>  
>
>
>  
>
>
>  ** _Return Type:_** This method returns a string which represents the
> concatenated path components.

 **Code:** Use of os.path.join() method to join various path components

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to explain os.path.join() method

 

# importing os module 

import os

 

# Path

path = "/home"

 

# Join various path components 

print(os.path.join(path, "User/Desktop", "file.txt"))

 

 

# Path

path = "User/Documents"

 

# Join various path components 

print(os.path.join(path, "/home", "file.txt"))

 

# In above example '/home'

# represents an absolute path

# so all previous components i.e User / Documents

# are thrown away and joining continues 

# from the absolute path component i.e / home.

 

 

# Path

path = "/User"

 

# Join various path components 

print(os.path.join(path, "Downloads", "file.txt", "/home"))

 

# In above example '/User' and '/home'

# both represents an absolute path

# but '/home' is the last value

# so all previous components before '/home'

# will be discarded and joining will

# continue from '/home' 

 

# Path

path = "/home"

 

# Join various path components 

print(os.path.join(path, "User/Public/", "Documents", ""))

 

# In above example the last 

# path component is empty

# so a directory seperator ('/')

# will be put at the end

# along with the concatenated value  
  
---  
  
 __

 __

 **Output:**

    
    
    /home/User/Desktop/file.txt
    /home/file.txt
    /home
    /home/User/Public/Documents/
    

**Reference:** https://docs.python.org/3/library/os.path.html

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

