Object Oriented Programming in Python | Set 1 (Class, Object and Members)



Below is a simple Python program that creates a class with a single method.  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# A simple example class

class Test:

 

 # A sample method

 def fun(self):

 print("Hello")

# Driver code

obj = Test()

obj.fun()  
  
---  
  
 __

 __

Output:

    
    
    Hello

As we can see above, we create a new class using the class statement and the
name of the class. This is followed by an indented block of statements that
form the body of the class. In this case, we have defined a single method in
the class.  
Next, we create an object/instance of this class using the name of the class
followed by a pair of parentheses.

 **Object:**

The object is an entity that has a state and behavior associated with it. It
may be any real-world object like the mouse, keyboard, chair, table, pen, etc.
Integers, strings, floating-point numbers, even arrays, and dictionaries, are
all objects. More specifically, any single integer or any single string is an
object. The number 12 is an object, the string “Hello, world” is an object, a
list is an object that can hold other objects, and so on. You’ve been using
objects all along and may not even realize it.

  

  

 **Class:**

A class is a blueprint that defines the variables and the methods
(Characteristics) common to all objects of a certain kind.

Example: If Car is a class, then Audi A6 is an object of the Car class. All
cars share similar features like 4 wheels, 1 steering wheel, windows, breaks
etc. Audi A6 (The Car object) has all these features.  
  
**The self**  

  1. Class methods must have an extra first parameter in the method definition. We do not give a value for this parameter when we call the method, Python provides it
  2. If we have a method that takes no arguments, then we still have to have one argument – the self. See fun() in the above simple example.
  3. This is similar to this pointer in C++ and this reference in Java.

When we call a method of this object as myobject.method(arg1, arg2), this is
automatically converted by Python into MyClass.method(myobject, arg1, arg2) –
this is all the special self is about.  
  
**The __init__ method**  
The __init__ method is similar to constructors in C++ and Java. It is run as
soon as an object of a class is instantiated. The method is useful to do any
initialization you want to do with your object.  

## Python

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

p = Person('Shwetanshu')

p.say_hi()  
  
---  
  
 __

 __

Output:

    
    
    Hello, my name is Shwetanshu 

Here, we define the __init__ method as taking a parameter name (along with the
usual self). .  
  
**Class and Instance Variables (Or attributes)**  
In Python, instance variables are variables whose value is assigned inside a
constructor or method with self.  
Class variables are variables whose value is assigned in class.  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to show that the variables with a value

# assigned in class declaration, are class variables and

# variables inside methods and constructors are instance

# variables.

 

# Class for Computer Science Student

class CSStudent:

 # Class Variable

 stream = 'cse'

 # The init method or constructor

 def __init__(self, roll):

 

 # Instance Variable 

 self.roll = roll 

 

# Objects of CSStudent class

a = CSStudent(101)

b = CSStudent(102)

 

print(a.stream) # prints "cse"

print(b.stream) # prints "cse"

print(a.roll) # prints 101

 

# Class variables can be accessed using class

# name also

print(CSStudent.stream) # prints "cse"   
  
---  
  
__

__

We can define instance variables inside normal methods also.  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to show that we can create

# instance variables inside methods

 

# Class for Computer Science Student

class CSStudent:

 

 # Class Variable

 stream = 'cse'

 

 # The init method or constructor

 def __init__(self, roll):

 

 # Instance Variable

 self.roll = roll 

 # Adds an instance variable

 def setAddress(self, address):

 self.address = address

 

 # Retrieves instance variable 

 def getAddress(self): 

 return self.address 

# Driver Code

a = CSStudent(101)

a.setAddress("Noida, UP")

print(a.getAddress())  
  
---  
  
 __

 __

Output :

    
    
    Noida, UP

  
**How to create an empty class?**  
We can create an empty class using pass statement in Python.  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# An empty class

class Test:

 pass  
  
---  
  
 __

 __

Object Oriented Programming in Python | Set 2 (Data Hiding and Object
Printing)  

-xa0  
This article is contributed by **Shwetanshu Rohatgi**. Please write comments
if you find anything incorrect, or you want to share more information about
the topic discussed above  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

