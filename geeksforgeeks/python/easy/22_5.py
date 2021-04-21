dir() function in Python



 ** _dir()_ **is a powerful inbuilt function in Python3, which returns list of
the attributes and methods of any object (say functions , modules, strings,
lists, dictionaries etc.)

 **Syntax :**

    
    
    dir({object})

 **Parameters :**

    
    
     **object** _[optional]_ : Takes object name

>  **Returns :**
>
> dir() tries to return a valid list of attributes of the object it is called
> upon. Also, dir() function behaves rather differently with different type of
> objects, as it aims to produce the most relevant one, rather than the
> complete information.
>
>  
>
>
>  
>
>
>   * For Class Objects, it returns a list of names of all the valid
> attributes and base attributes as well.
>   * For Modules/Library objects, it tries to return a list of names of all
> the attributes, contained in that module.
>   * If no parameters are passed it returns a list of names in the current
> local scope.
>

  
**Code #1 :** With and Without importing external libraries.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate dir()

# when no parameters are passed

 

# Note that we have not imported any modules

print(dir())

 

 

# Now let's import two modules

import random

import math

 

# return the module names added to

# the local namespace including all

# the existing ones as before

print(dir())  
  
---  
  
 __

 __

 **Output :**

    
    
    
    ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__',
                                              '__name__', '__package__', '__spec__']
    
    
    
    ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__',
                             '__name__', '__package__', '__spec__', 'math', 'random']
    

  
**Code #2 :**

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate dir() function

# when a module Object is passed as parameter.

 

# import the random module 

import random

 

 

# Prints list which contains names of

# attributes in random function

print("The contents of the random library are::")

 

# module Object is passed as parameter

print(dir(random))  
  
---  
  
 __

 __

 **Output :**

    
    
    The contents of the random library are ::
    
    ['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST',
    'SystemRandom', 'TWOPI', '_BuiltinMethodType', '_MethodType', '_Sequence',
    '_Set', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__',
    '__name__', '__package__', '__spec__', '_acos', '_ceil', '_cos', '_e', '_exp',
    '_inst', '_log', '_pi', '_random', '_sha512', '_sin', '_sqrt', '_test', '_test_generator',
    '_urandom', '_warn', 'betavariate', 'choice', 'expovariate', 'gammavariate', 'gauss',
    'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randint',
    'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform',
    'vonmisesvariate', 'weibullvariate']
    

  
**Code #3 :** Object is passed as parameters.

 __

 __  
 __

 __

 __  
 __  
 __

# When a list object is passed as

# parameters for the dir() function

 

# A list, which conatains

# a few random values

geeks = ["geeksforgeeks", "gfg", "Computer Science",

 "Data Structures", "Algorithms" ]

 

 

# dir() will also list out common

# attributes of the dictionary

d = {} # empty dictionary

 

# dir() will return all the available 

# list methods in current local scope

print(dir(geeks))

 

 

# Call dir() with the dictionary

# name "d" as parameter. Return all

# the available dict methods in the 

# current local scope

print(dir(d))  
  
---  
  
 __

 __

 **Output :**

    
    
    ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__',
    '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
    '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', 
    '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', 
    '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', 
    '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 
    'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
    
    
    ['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', 
    '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', 
    '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', 
    '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', 
    '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 
    'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
    

  
**Code #4 :** User Defined – Class Object with an available __dir()__ method
is passed as parameter.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to demonstrate working

# of dir(), when user defined objects are

# passed are parameters.

 

 

# Creation of a simple class with __dir()__

# method to demonstrate it's working

class Supermarket:

 

 # Function __dir()___ which list all 

 # the base attributes to be used.

 def __dir__(self):

 return['customer_name', 'product',

 'quantity', 'price', 'date']

 

 

# user-defined object of class supermarket

my_cart = Supermarket()

 

# listing out the dir() method

print(dir(my_cart))  
  
---  
  
 __

 __

 **Output :**

    
    
    ['customer_name', 'date', 'price', 'product', 'quantity']
    

  
**Applications :**

  * The **dir()** has it’s own set of uses. It is usually used for _debugging purposes_ in simple day to day programs, and even in large projects taken up by a team of developers. The capability of dir() to list out all the attributes of the parameter passed, is really useful when handling a lot of classes and functions, separately.
  * The **dir()** function can also list out all the available attributes for a module/list/dictionary. So, it also gives us information on the operations we can perform with the available list or module, which can be very useful when having little to no information about the module. It also helps to know new modules faster.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

