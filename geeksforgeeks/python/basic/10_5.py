Private Methods in Python



 **Prerequisites –**

  * Python classes and objects
  * Encapsulation
  * Underscore in Python

Encapsulation is one of the fundamental concepts in object-oriented
programming (OOP). It describes the idea of wrapping data and the methods that
work on data within one unit. This puts restrictions on accessing variables
and methods directly and can prevent the accidental modification of data. A
class is an example of encapsulation as it encapsulates all the data that is
member functions, variables, etc.

Now, there can be some scenarios in which we need to put restrictions on some
methods of the class, so that they can neither be accessed outside the class
nor by any subclasses. To implement this private methods come into play.

## Private methods

Consider a real life example, a car engine, which is made up of many parts
like spark plug, valves, piston, etc. No user use these parts directly, rather
they just know how to use the parts which uses them. This is what private
methods are used for. It is used to hide the inner functionality of any class
from the outside world.

Private methods are those methods that should neither be accessed outside the
class nor by any base class. In Python, there is no existence of Private
methods that cannot be accessed except inside a class. However, to define a
private method prefix the member name with **double underscore** “ **__** ”.

  

  

 **Note:** The __init__ method is a constructor and runs as soon as an
object of a class is instantiated.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to

# demonstrate private methods

 

# Creating a Base class 

class Base: 

 

 # Declaring public method

 def fun(self):

 print("Public method")

 

 # Declaring private method

 def __fun(self):

 print("Private method")

 

# Creating a derived class 

class Derived(Base): 

 def __init__(self): 

 

 # Calling constructor of 

 # Base class 

 Base.__init__(self) 

 

 def call_public(self):

 

 # Calling public method of base class

 print("\nInside derived class")

 self.fun()

 

 def call_private(self):

 

 # Calling private method of base class

 self.__fun()

 

# Driver code 

obj1 = Base()

 

# Calling public method

obj1.fun()

 

obj2 = Derived()

obj2.call_public()

 

# Uncommenting obj1.__fun() will 

# raise an AttributeError 

 

# Uncommenting obj2.call_private() 

# will also raise an AttributeError  
  
---  
  
 __

 __

 **Output:**

    
    
    Public method
    
    Inside derived class
    Public method
    
    
    
    Traceback (most recent call last):
      File "/home/09d6f91fdb63d16200e172c7a925dd7f.py", line 43, in 
        obj1.__fun() 
    AttributeError: 'Base' object has no attribute '__fun'
    
    Traceback (most recent call last):
      File "/home/0d5506bab8f06cb7c842501d9704557b.py", line 46, in 
        obj2.call_private() 
      File "/home/0d5506bab8f06cb7c842501d9704557b.py", line 32, in call_private
        self.__fun()
    AttributeError: 'Derived' object has no attribute '_Derived__fun'
    

The above example shows that private methods of the class can neither be
accessed outside the class nor by any base class. However, private methods can
be accessed by calling the private methods via public methods.

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to

# demonstrate private methods

 

# Creating a class 

class A: 

 

 # Declaring public method

 def fun(self):

 print("Public method")

 

 # Declaring private method

 def __fun(self):

 print("Private method")

 

 # Calling private method via

 # another method

 def Help(self):

 self.fun()

 self.__fun()

 

# Driver's code

obj = A()

obj.Help()  
  
---  
  
 __

 __

 **Output:**

    
    
    Public method
    Private method
    

#### Name mangling

Python provides a magic wand which can be used to call private methods outside
the class also, it is known as name mangling. It means that any identifier of
the form __geek (at least two leading underscores or at most one trailing
underscore) is replaced with _classname__geek, where classname is the current
class name with leading underscore(s) stripped.

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to

# demonstrate private methods

 

# Creating a class 

class A: 

 

 # Declaring public method

 def fun(self):

 print("Public method")

 

 # Declaring private method

 def __fun(self):

 print("Private method")

 

# Driver's code

obj = A()

 

# Calling the private member 

# through name mangling

obj._A__fun()  
  
---  
  
 __

 __

 **Output:**

    
    
    Private method
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

