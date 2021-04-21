Collections.UserDict in Python



An unordered collection of data value that is used to store data values like a
map is known as **Dictionary in Python**. Unlike other Data Types that hold
only single value as an element, Dictionary holds key:value pair. Key-value
is provided in the dictionary to make it more optimized.

 **Note:** For more information, refer to Python Dictionary

## Collections.UserDict

Python supports a dictionary like a container called **UserDict** present in
the **collections** module. This class acts as a wrapper class around the
dictionary objects. This class is useful when one wants to create a dictionary
of their own with some modified functionality or with some new functionality.
It can be considered as a way of adding new behaviors for the dictionary. This
class takes a dictionary instance as an argument and simulates a dictionary
that is kept in a regular dictionary. The dictionary is accessible by the data
attribute of this class.

 **Syntax:**

    
    
    collections.UserDict([initialdata])
    

**Example 1:**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# userdict

 

 

from collections import UserDict

 

 

d = {'a':1,

 'b': 2,

 'c': 3}

 

# Creating an UserDict

userD = UserDict(d)

print(userD.data)

 

 

# Creating an empty UserDict

userD = UserDict()

print(userD.data)  
  
---  
  
 __

 __

 **Output:**

    
    
    {'a': 1, 'b': 2, 'c': 3}
    {}
    

**Example 2:** Let’s create a class inherting from UserDict to implement a
customised dictionary.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# userdict

 

 

from collections import UserDict

 

 

# Creating a Dictionary where

# deletion is not allowed

class MyDict(UserDict):

 

 # Function to stop deleltion

 # from dictionary

 def __del__(self):

 raise RuntimeError("Deletion not allowed")

 

 # Function to stop pop from 

 # dictionary

 def pop(self, s = None):

 raise RuntimeError("Deletion not allowed")

 

 # Function to stop popitem 

 # from Dictionary

 def popitem(self, s = None):

 raise RuntimeError("Deletion not allowed")

 

# Driver's code

d = MyDict({'a':1,

 'b': 2,

 'c': 3})

 

print("Original Dictionary")

print(d)

 

d.pop(1)  
  
---  
  
 __

 __

 **Output:**

    
    
    Original Dictionary
    {'a': 1, 'c': 3, 'b': 2}
    
    
    Traceback (most recent call last):
      File "/home/3ce2f334f5d25a3e24d10d567c705ce6.py", line 35, in 
        d.pop(1)
      File "/home/3ce2f334f5d25a3e24d10d567c705ce6.py", line 20, in pop
        raise RuntimeError("Deletion not allowed")
    RuntimeError: Deletion not allowed
    Exception ignored in: 
    Traceback (most recent call last):
      File "/home/3ce2f334f5d25a3e24d10d567c705ce6.py", line 15, in __del__
    RuntimeError: Deletion not allowed

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

