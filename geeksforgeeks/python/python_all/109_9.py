Python: os.path.abspath() method with example



 **OS module** in Python provides various methods for interacting with the
operating system. It comes under Python’s standard utility module, so there is
no need to install it externally. **os.path** is a submodule of OS module
which contains some useful functions on pathnames. The path parameters are
either strings or bytes. These functions here are used for different purposes
such as for merging, normalizing and retrieving path names in Python.

According to docs os.path.abspath() returns a normalized absolutized version
of the pathname path which may sound fancy but it simply means that this
method returns the pathname to the path passed as a parameter to this
function.

>  **Syntax:** os.path.abspath(path)
>
>  **Parameter:**  
>  **Path:** A path-like object representing a file system path.
>
>  **Return Type:** This method returns a normalized version of the pathname
> path.
>
>  
>
>
>  
>

 **Example 1:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# os.path.abspath()

 

 

import os.path

 

# file name 

file_name = 'GFG.txt'

 

 

# prints the absolute path of current

# working directory with file name

print(os.path.abspath(file_name))  
  
---  
  
 __

 __

 **Output:**

    
    
    /home/geeks/Desktop/gfg/GFG.txt
    

**Example 2:** This function can also return the normalized path after
changing the current working directory.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# os.path.abspath()

 

 

import os

 

# file name 

file_name = 'GFG.txt'

 

# change the current working

# directory

os.chdir("/home/geeks/")

 

# prints the absolute path of current

# working directory with file name

print(os.path.abspath(file_name))  
  
---  
  
 __

 __

 **Output:**

    
    
    /home/geeks/GFG.txt
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

