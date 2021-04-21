__subclasscheck__ and __subclasshook__ in Python



Class is a collection of data (variables and methods). It bundles data and
functionality together. It provides all standard features of object-oriented
programming. Basically it is a blueprint for creating objects. Creating a new
class creates a new type of object, allowing new instances of that type to be
made.

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# class 'A' defined

class A(object):

 

 # Calling Constructor

 def __init__(self, a):

 

 self.a = a

 print("The value of a:", self.a)

 

# Driver's code

c = A(7)  
  
---  
  
 __

 __

 **Output:**

    
    
    The value of a: 7
    

#### __subclasscheck__ in Python

__subclasscheck__ is one of the methods to customize the result of
issubclass() built-in function. It is a method to check whether a class is a
subclass or not and returns True if the class is considered as a
subclass(direct or indirect) of another class, otherwise, returns False. It
cannot be defined as a class method in the actual/real class. It is
implemented in the metaclass, as it is not for ordinary classes. Consider the
below example for better understanding.

 **Example:** Consider a situation where you want to check if a certain value
is present as an attribute inside a class using the issubclass() method.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# subclasscheck

 

 

class A(type):

 

 # __subclasscheck__() defined

 def __subclasscheck__(cls, sub):

 

 # Getting the L attribute of

 # subclass

 attr = getattr(cls, 'L', [])

 

 # Checking if the subclass

 # is present in the L attribute

 # of subclass or not

 if sub in attr:

 return True

 

 return False

 

 

class B(metaclass = A):

 

 # L Attribute

 L = [1, 2, 3, 4, 5]

 

class C(metaclass = A):

 

 # L Attribute

 L = ["Geeks", "For"]

 

 

# Driver's code

print(issubclass(1, B))

print(issubclass("Geeks", B))

print(issubclass("Geeks", C))  
  
---  
  
 __

 __

 **Output:**

    
    
    True
    False
    True
    

#### __subclasshook__ in Python

Abstract class can override __subclasshook__() method to customize
issubclass(). It returns True when a class is found to be subclass of a
ABC class, it returns False if it is not and returns NotImplemented if the
subclass check is continued with the usual mechanism. This method is defined
in the ABC class with some conditions. Classes that follow those conditions
are considered to be a subclass.

 **Note:** It must be defined as a class method.

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# subclasshook

 

 

from abc import ABCMeta

 

 

class A(metaclass = ABCMeta):

 

 @classmethod

 def __subclasshook__(cls, C):

 if cls is A:

 

 # condition to check if the 

 # function anyfun() is present 

 # in any sub class or not

 if any("__anyfun__" in Q.__dict__ 

 for Q in C.__mro__): 

 return True

 

 return False

 

class P(object):

 pass

 

class Q(object):

 

 def __anyfun__(self):

 return 0

 

 

# Driver's code

print(issubclass(Q, A) ) 

print(issubclass(P, A) )  
  
---  
  
 __

 __

 **Output:**

    
    
    True
    False
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

