Python Modules



A module is a file containing Python definitions and statements. A module can
define functions, classes, and variables. A module can also include runnable
code. Grouping related code into a module makes the code easier to understand
and use. It also makes the code logically organized.

 **Example:**

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# A simple module, calc.py

def add(x, y):

 return (x+y)

def subtract(x, y):

 return (x-y)  
  
---  
  
 __

 __

###  **The import statement**

We can use any Python source file as a module by executing an import statement
in some other Python source file.  
When the interpreter encounters an import statement, it imports the module if
the module is present in the search path. A search path is a list of
directories that the interpreter searches for importing a module. For example,
to import the module calc.py, we need to put the following command at the top
of the script :

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# importing module calc.py

import calc

print(add(10, 2))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    12
    

### **The from import** _ ****_**Statement**

Python’s _from_ statement lets you import specific attributes from a module.
The _from .. import .._ has the following syntax :

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing sqrt() and factorial from the

# module math

from math import sqrt, factorial

# if we simply do "import math", then

# math.sqrt(16) and math.factorial()

# are required.

print(sqrt(16))

print(factorial(6))  
  
---  
  
 __

 __

 **Output:**

    
    
    4.0
    720
    

### The from import * Statement

The * symbol used with the from import the statement is used to import all the
names from a module to a current namespace.

 **Syntax:**

    
    
    from module_name import *
    

The use of * has it’s advantages and disadvantages. If you know exactly what
you will be needing from the module, it is not recommended to use *, else do
so.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Import built-in module random

from random import *

print(dir(random))  
  
---  
  
 __

 __

 **Output:**

> [‘__call__’, ‘__class__’, ‘__delattr__’, ‘__dir__’, ‘__doc__’, ‘__eq__’,
> ‘__format__’, ‘__ge__’, ‘__getattribute__’, ‘__gt__’, ‘__hash__’,
> ‘__init__’, ‘__init_subclass__’, ‘__le__’, ‘__lt__’, ‘__module__’,
> ‘__name__’, ‘__ne__’, ‘__new__’, ‘__qualname__’, ‘__reduce__’,
> ‘__reduce_ex__’, ‘__repr__’, ‘__self__’, ‘__setattr__’, ‘__sizeof__’,
> ‘__str__’, ‘__subclasshook__’, ‘__text_signature__’]

###  **The dir() function**

The dir() built-in function returns a sorted list of strings containing the
names defined by a module. The list contains the names of all the modules,
variables, and functions that are defined in a module.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Import built-in module random

import random

print(dir(random))  
  
---  
  
 __

 __

 **Output:**

> [‘BPF’, ‘LOG4’, ‘NV_MAGICCONST’, ‘RECIP_BPF’, ‘Random’, ‘SG_MAGICCONST’,
> ‘SystemRandom’, ‘TWOPI’, ‘_BuiltinMethodType’, ‘_MethodType’, ‘_Sequence’,
> ‘_Set’, ‘__all__’, ‘__builtins__’, ‘__cached__’, ‘__doc__’, ‘__file__’,
> ‘__loader__’, ‘__name__’, ‘__package__’, ‘__spec__’, ‘_acos’, ‘_bisect’,
> ‘_ceil’, ‘_cos’, ‘_e’, ‘_exp’, ‘_inst’, ‘_itertools’, ‘_log’, ‘_pi’,
> ‘_random’, ‘_sha512’, ‘_sin’, ‘_sqrt’, ‘_test’, ‘_test_generator’,
> ‘_urandom’, ‘_warn’, ‘betavariate’, ‘choice’, ‘choices’, ‘expovariate’,
> ‘gammavariate’, ‘gauss’, ‘getrandbits’, ‘getstate’, ‘lognormvariate’,
> ‘normalvariate’, ‘paretovariate’, ‘randint’, ‘random’, ‘randrange’,
> ‘sample’, ‘seed’, ‘setstate’, ‘shuffle’, ‘triangular’, ‘uniform’,
> ‘vonmisesvariate’, ‘weibullvariate’]

 **Code Snippet illustrating python built-in modules:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing built-in module math

import math

# using square root(sqrt) function contained

# in math module

print(math.sqrt(25))

# using pi function contained in math module

print(math.pi)

# 2 radians = 114.59 degreees

print(math.degrees(2)) 

# 60 degrees = 1.04 radians

print(math.radians(60)) 

# Sine of 2 radians

print(math.sin(2)) 

# Cosine of 0.5 radians

print(math.cos(0.5)) 

# Tangent of 0.23 radians

print(math.tan(0.23))

# 1 * 2 * 3 * 4 = 24

print(math.factorial(4)) 

# importing built in module random

import random

# printing random integer between 0 and 5

print(random.randint(0, 5)) 

# print random floating point number between 0 and 1

print(random.random()) 

# random number between 0 and 100

print(random.random() * 100) 

List = [1, 4, True, 800, "python", 27,
"hello"]

# using choice function in random module for choosing

# a random element from a set such as a list

print(random.choice(List))

# importing built in module datetime

import datetime

from datetime import date

import time

# Returns the number of seconds since the

# Unix Epoch, January 1st 1970

print(time.time()) 

# Converts a number of seconds to a date object

print(date.fromtimestamp(454554))   
  
---  
  
__

__

**Output:**

    
    
    5.0
    3.14159265359
    114.591559026
    1.0471975512
    0.909297426826
    0.87758256189
    0.234143362351
    24
    3
    0.401533172951
    88.4917616788
    True
    1461425771.87
    1970-01-06
    

This article is contributed by **Gaurav Shrestha**. Please write comments if
you find anything incorrect, or you want to share more information about the
topic discussed above. If you like GeeksforGeeks and would like to contribute,
you can also write an article and mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

