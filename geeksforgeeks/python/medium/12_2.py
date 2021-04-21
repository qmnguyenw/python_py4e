Defaultdict in Python



Dictionary in Python is an unordered collection of data values that are used
to store data values like a map. Unlike other Data Types that hold only single
value as an element, the Dictionary holds key:value pair. In Dictionary, the
key must be unique and immutable. This means that a Python Tuple can be a key
whereas a Python List can not. A Dictionary can be created by placing a
sequence of elements within curly {} braces, separated by ‘comma’.

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# dictionary

 

 

Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'} 

print("Dictionary:") 

print(Dict)

print(Dict[1])

 

# Uncommenting this print(Dict[4])

# will raise a KeyError as the

# 4 is not present in the dictionary  
  
---  
  
 __

 __

 **Output:**

    
    
    Dictionary:
    {1: 'Geeks', 2: 'For', 3: 'Geeks'}
    Geeks
    
    
    
    Traceback (most recent call last):
      File "/home/1ca83108cc81344dc7137900693ced08.py", line 11, in 
        print(Dict[4])
    KeyError: 4
    

Sometimes, when the KeyError is raised, it might become a problem. To
overcome this Python introduces another dictionary like container known as
**Defaultdict** which is present inside the collections module.

 **Note:** For more information, refer to Python Dictionary.

  

  

## DefaultDict

 **Defaultdict** is a container like dictionaries present in the module
**collections**. Defaultdict is a sub-class of the dict class that returns a
dictionary-like object. The functionality of both dictionaries and defualtdict
are almost same except for the fact that defualtdict never raises a
KeyError. It provides a default value for the key that does not exists.

>  **Syntax:** defaultdict(default_factory)
>
>  **Parameters:**
>
>   *  **default_factory:** A function returning the default value for the
> dictionary defined. If this argument is absent then the dictionary raises a
> KeyError.
>

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# defaultdict

 

 

from collections import defaultdict

 

 

# Function to return a default

# values for keys that is not

# present

def def_value():

 return "Not Present"

 

# Defining the dict

d = defaultdict(def_value)

d["a"] = 1

d["b"] = 2

 

print(d["a"])

print(d["b"])

print(d["c"])  
  
---  
  
 __

 __

 **Output:**

    
    
    1
    2
    Not Present
    

## Inner Working of defaultdict

Defaultdict adds one writable instance variable and one method in addition to
the standard dictionary operations. The instance variable is the
default_factory parameter and the method provided is __missing__.

  *  **Default_factory:** It is a function returning the default value for the dictionary defined. If this argument is absent then the dictionary raises a KeyError.

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# default_factory argument of 

# defaultdict

 

 

from collections import defaultdict

 

 

# Defining the dict and passing 

# lambda as default_factory argument

d = defaultdict(lambda: "Not Present")

d["a"] = 1

d["b"] = 2

 

print(d["a"])

print(d["b"])

print(d["c"])  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    1
    2
    Not Present
    

  * **__missing__():** This function is used to provide the default value for the dictionary. This function takes default_factory as an argument and if this argument is None, a KeyError is raised otherwise it provides a default value for the given key. This method is basically called by the __getitem__() method of the dict class when the requested key is not found. __getitem__() raises or return the value returned by the __missing__(). method.

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# defaultdict

 

 

from collections import defaultdict

 

 

# Defining the dict

d = defaultdict(lambda: "Not Present")

d["a"] = 1

d["b"] = 2

 

# Provides the default value 

# for the key

print(d.__missing__('a'))

print(d.__missing__('d'))  
  
---  
  
 __

 __

 **Output:**

    
    
    Not Present
    Not Present
    

## Using List as default_factory

When the list class is passed as the default_factory argument, then a
defaultdict is created with the values that are list.

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# defaultdict

 

 

from collections import defaultdict

 

 

# Defining a dict

d = defaultdict(list)

 

for i in range(5):

 d[i].append(i)

 

print("Dictionary with values as list:")

print(d)  
  
---  
  
 __

 __

 **Output:**

    
    
    Dictionary with values as list:
    defaultdict(<class 'list'>, {0: [0], 1: [1], 2: [2], 3: [3], 4: [4]})
    

## Using int as default_factory

When the int class is passed as the default_factory argument, then a
defaultdict is created with default value as zero.

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# defaultdict

 

 

from collections import defaultdict

 

 

# Defining the dict

d = defaultdict(int)

 

L = [1, 2, 3, 4, 2, 4, 1, 2]

 

# Iterate through the list

# for keeping the count

for i in L:

 

 # The default value is 0

 # so there is no need to 

 # enter the key first

 d[i] += 1

 

print(d)  
  
---  
  
 __

 __

 **Output:**

    
    
    defaultdict(<class 'int'>, {1: 2, 2: 3, 3: 1, 4: 2})
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

