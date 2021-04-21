__init__ in Python



 **Prerequisites –** Python Class, Objects, Self

Whenever object oriented programming is done in Python, we mostly come across
__init__ method which we usually don’t fully understand. This article
explains the main concept of __init__ but before understanding the
__init__ some prerequisites are required.

## __init__

The __init__ method is similar to **constructors** in C++ and Java.
Constructors are used to initialize the object’s state. The task of
constructors is to initialize(assign values) to the data members of the class
when an object of class is created. Like methods, a constructor also contains
collection of statements(i.e. instructions) that are executed at time of
Object creation. It is run as soon as an object of a class is instantiated.
The method is useful to do any initialization you want to do with your object.

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# A Sample class with init method

class Person: 

 

 # init method or constructor 

 def __init__(self, name): 

 self.name = name 

 

 # Sample Method 

 def say_hi(self): 

 print('Hello, my name is', self.name) 

 

p = Person('Nikhil') 

p.say_hi()   
  
---  
  
__

__

**Output:**

  

  

    
    
    Hello, my name is Nikhil
    

#### Understanding the code

In the above example, a person name Nikhil is created. While creating a
person, “Nikhil” is passed as an argument, this argument will be passed to the
__init__ method to initialize the object. The keyword self represents the
instance of a class and binds the attributes with the given arguments.
Similarly, many objects of Person class can be created by passing different
names as arguments.

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# A Sample class with init method

class Person: 

 

 # init method or constructor 

 def __init__(self, name): 

 self.name = name 

 

 # Sample Method 

 def say_hi(self): 

 print('Hello, my name is', self.name) 

 

# Creating different objects 

p1 = Person('Nikhil') 

p2 = Person('Abhinav')

p3 = Person('Anshul')

 

p1.say_hi() 

p2.say_hi()

p3.say_hi()  
  
---  
  
 __

 __

 **Output:**

    
    
    Hello, my name is Nikhil
    Hello, my name is Abhinav
    Hello, my name is Anshul
    

#### __init__ with inheritance

Inheritance is the capability of one class to derive or inherit the properties
from some other class. Let’s consider the below example to see how __init__
works in inheritance.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to

# demonstrate init with

# inheritance

 

class A(object):

 def __init__(self, something):

 print("A init called")

 self.something = something

 

 

class B(A):

 def __init__(self, something):

 # Calling init of parent class

 A.__init__(self, something)

 print("B init called")

 self.something = something

 

obj = B("Something")  
  
---  
  
 __

 __

 **Output:**

    
    
    A init called
    B init called
    

So, the parent class constructor is called first. But in Python, it is not
compulsory that parent class constructor will always be called first. The
order in which the __init__ method is called for a parent or a child class can
be modified. This can simply be done by calling the parent class constructor
after the body of child class constructor.

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to

# demonstrate init with

# inheritance

 

class A(object):

 def __init__(self, something):

 print("A init called")

 self.something = something

 

 

class B(A):

 def __init__(self, something):

 print("B init called")

 self.something = something

 # Calling init of parent class

 A.__init__(self, something)

 

obj = B("Something")  
  
---  
  
 __

 __

 **Output:**

    
    
    B init called
    A init called
    

**Note:** To know more about inheritance click here.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

