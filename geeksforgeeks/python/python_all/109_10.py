Python – os.pardir() method with example



In Python, **OS module** provides various functions to interact with the
operating system. This module comes under the Python standard utility module,
so there is no need to install it manually.

os.pardir is a constant string used by the operating system to refer to the
parent directory. This method is also available via os.path.pardir()

 **Note:**os.pardir is ‘.. for UNIX based OS and ‘::‘ for Mac OS.

>  **Syntax:** os.pardir
>
>  **Return type:** a string that refers to the parent directory.
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

# os.pardir

 

import os

 

# prints .. by default

print(os.pardir)  
  
---  
  
 __

 __

 **Output:**

    
    
    ..
    

  
**Example 2:** Let’s print the parent of current working directory.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# os.pardir

 

 

import os

 

 

# current working directory

path = os.getcwd()

print("Current Directory:", path)

 

# parent directory

parent = os.path.join(path, os.pardir)

 

# prints parent directory

print("\nParent Directory:", os.path.abspath(parent))  
  
---  
  
 __

 __

 **Output:**

    
    
    Current Directory: /home/geeks/Desktop/gfg
    
    Parent Directory: /home/geeks/Desktop
    

  
**Example 3:** Getting the parent of specified path.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# os.pardir

 

 

import os

 

 

# path

path = "your/path/for/parent/directory"

print("Path:", path)

 

# parent

parent = os.path.join(path, os.pardir)

 

# prints the relative file path 

# for the current directory (parent)

print("\nParent:", os.path.relpath(parent))  
  
---  
  
 __

 __

 **Output:**

    
    
    Path: your/path/for/parent/directory
    
    Parent: your/path/for/parent
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

