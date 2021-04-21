How to Get a List of Class Attributes in Python?



A class is a user-defined blueprint or prototype from which objects are
created. Classes provide a means of bundling data and functionality together.
Creating a new class creates a new type of object, allowing new instances of
that type to be made. Each class instance can have attributes attached to it
for maintaining its state. Class instances can also have methods (defined by
its class) for modifying its state.

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# classes

 

 

class Student:

 

 # class variable

 stream = "COE"

 

 # Constructor

 def __init__(self, name, roll_no):

 

 self.name = name

 self.roll_no = roll_no

 

# Driver's code

a = Student("Shivam", 3425)

b = Student("Sachin", 3624)

 

print(a.stream)

print(b.stream)

print(a.name)

print(b.name)

 

# Class variables can be accessed

# using class name also 

print(Student.stream)   
  
---  
  
__

__

**Output :**

    
    
    COE
    COE
    Shivam
    Sachin
    COE
    

**Note:** For more information, refer to Python Classes and Objects.

#### Getting a List of Class Attributes

It is important to know the attributes we are working with. For small data, it
is easy to remember the names of the attributes but when working with huge
data, it is difficult to memorize all the attributes. Luckily, we have some
functions in Python available for this task.

  

  

 **Method 1:** To get the list of all the attributes, methods along with some
inherited magic methods of a class, we use a built-in called dir().

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

class Number :

 

 # Class Attributes

 one = 'first'

 two = 'second'

 three = 'third'

 

 def __init__(self, attr):

 self.attr = attr

 

 def show(self): 

 print(self.one, self.two, self.three, self.attr)

 

n = Number(2)

n.show()

 

 

 

# Passing both the object 

# and class as argument

# to the dir method

print('\nBy passing object of class')

print(dir(n))

 

print('\nBy passing class itself ')

print(dir(Number))  
  
---  
  
 __

 __

 **Output :**

> first second third 2
>
> By passing object of class  
> [‘__class__’, ‘__delattr__’, ‘__dict__’, ‘__dir__’, ‘__doc__’, ‘__eq__’,
> ‘__format__’, ‘__ge__’, ‘__getattribute__’, ‘__gt__’, ‘__hash__’,
> ‘__init__’, ‘__init_subclass__’, ‘__le__’, ‘__lt__’, ‘__module__’, ‘__ne__’,
> ‘__new__’, ‘__reduce__’, ‘__reduce_ex__’, ‘__repr__’, ‘__setattr__’,
> ‘__sizeof__’, ‘__str__’, ‘__subclasshook__’, ‘__weakref__’, ‘attr’, ‘one’,
> ‘show’, ‘three’, ‘two’]
>
> By passing class itself  
> [‘__class__’, ‘__delattr__’, ‘__dict__’, ‘__dir__’, ‘__doc__’, ‘__eq__’,
> ‘__format__’, ‘__ge__’, ‘__getattribute__’, ‘__gt__’, ‘__hash__’,
> ‘__init__’, ‘__init_subclass__’, ‘__le__’, ‘__lt__’, ‘__module__’, ‘__ne__’,
> ‘__new__’, ‘__reduce__’, ‘__reduce_ex__’, ‘__repr__’, ‘__setattr__’,
> ‘__sizeof__’, ‘__str__’, ‘__subclasshook__’, ‘__weakref__’, ‘one’, ‘show’,
> ‘three’, ‘two’]

 **Method 2:** Another way of finding a list of attributes is by using the
module inspect. This module provides a method called getmemebers() that
returns a list of class attributes and methods.

 **Example 1:**

 __

 __  
 __

 __

 __  
 __  
 __

import inspect

 

 

class Number :

 

 # Class Attributes

 one = 'first'

 two = 'second'

 three = 'third'

 

 def __init__(self, attr):

 self.attr = attr

 

 def show(self): 

 print(self.one, self.two, self.three, self.attr)

 

 

# Driver's code

n = Number(2)

n.show()

 

# getmembers() returns all the 

# members of an object 

for i in inspect.getmembers(n):

 

 # to remove private and protected

 # functions

 if not i[0].startswith('_'):

 

 # To remove other methods that

 # doesnot start with a underscore

 if not inspect.ismethod(i[1]): 

 print(i)  
  
---  
  
 __

 __

 **Output :**

    
    
    first second third 2
    ('attr', 2)
    ('one', 'first')
    ('three', 'third')
    ('two', 'second')
    

**Method 3:** To find attributes we can also use magic method __dict__. This
method only returns instance attributes.

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

class Number :

 

 # Class Attributes

 one = 'first'

 two = 'second'

 three = 'third'

 

 def __init__(self, attr):

 self.attr = attr

 

 def show(self): 

 print(self.one, self.two, self.three, self.attr)

 

# Driver's code

n = Number(2)

n.show()

 

# using __dict__ to access attributes

# of the object n along with their values

print(n.__dict__)

 

# to only access attributes

print(n.__dict__.keys())

 

# to only access values

print(n.__dict__.values())  
  
---  
  
 __

 __

 **Output:**

    
    
    first second third 2
    {'attr': 2}
    dict_keys(['attr'])
    dict_values([2])
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

