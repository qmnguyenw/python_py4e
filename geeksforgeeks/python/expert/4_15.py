PYTHONPATH Environment Variable in Python



Python’s behavior is greatly influenced by its environment variables. One of
those variables is PYTHONPATH. It is used to set the path for the user-defined
modules so that it can be directly imported into a Python program. It is also
responsible for handling the default search path for Python Modules. The
PYTHONPATH variable holds a string with the name of various directories that
need to be added to the sys.path directory list by Python. The primary use of
this variable is to allow users to import modules that are not made
installable yet. Let’s try to understand the concept using an example.

Suppose you defined a module as below:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# user-defined module

# saved as my_module.py

 

 

def module_func():

 print("You just imported the user-defined module")  
  
---  
  
 __

 __

Now if you attempt to import the_ _ **my_module.py**_ in your python script as
below:

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# python script to

# call the module

 

# import the module

import my_module

 

# call the module function

my_module.module_func()  
  
---  
  
 __

 __

