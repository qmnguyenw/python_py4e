sys.path in Python



Sys is a built-in Python module that contains parameters specific to the
system i.e. it contains variables and methods that interact with the
interpreter and are also governed by it.

### **sys.path**

sys.path is a built-in variable within the sys module. It contains a list of
directories that the interpreter will search in for the required module.

When a module(a module is a python file) is imported within a Python file, the
interpreter first searches for the specified module among its built-in
modules. If not found it looks through the list of directories(a directory is
a folder that contains related modules) defined by **sys.path**.

###  **Initializing sys.path __**

There are three ways to specify a path :

  *  **DEFAULT-** By default, the interpreter looks for a module within the current directory. To make the interpreter search in some other directory you just simply have to change the current directory. The following example depicts a default path taken by the interpreter:

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# importing module

import sys

 

# printing all directories for 

# interpreter to search

sys.path  
  
---  
  
 __

 __

