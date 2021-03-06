Python Classes and Objects



A class is a user-defined blueprint or prototype from which objects are
created. Classes provide a means of bundling data and functionality together.
Creating a new class creates a new type of object, allowing new instances of
that type to be made. Each class instance can have attributes attached to it
for maintaining its state. Class instances can also have methods (defined by
their class) for modifying their state.

To understand the need for creating a class let’s consider an example, let’s
say you wanted to track the number of dogs that may have different attributes
like breed, age. If a list is used, the first element could be the dog’s breed
while the second element could represent its age. Let’s suppose there are 100
different dogs, then how would you know which element is supposed to be which?
What if you wanted to add other properties to these dogs? This lacks
organization and it’s the exact need for classes.

Class creates a user-defined data structure, which holds its own data members
and member functions, which can be accessed and used by creating an instance
of that class. A class is like a blueprint for an object.

 **Some points on Python class:**

  * Classes are created by keyword class.
  * Attributes are the variables that belong to a class.
  * Attributes are always public and can be accessed using the dot (.) operator. Eg.: Myclass.Myattribute

    
    
     **Class Definition Syntax:**
    
    class ClassName:
        # Statement-1
        .
        .
        .
        # Statement-N

 **Defining a class –**

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to

# demonstrate defining

# a class

class Dog:

 pass  
  
---  
  
 __

 __

In the above example, the class keyword indicates that you are creating a
class followed by the name of the class (Dog in this case).  

## Class Objects

An Object is an instance of a Class. A class is like a blueprint while an
instance is a copy of the class with _actual values_. It’s not an idea
anymore, it’s an actual dog, like a dog of breed pug who’s seven years old.
You can have many dogs to create many different instances, but without the
class as a guide, you would be lost, not knowing what information is required.  
An object consists of :

  * **State:** It is represented by the attributes of an object. It also reflects the properties of an object.
  *  **Behavior:** It is represented by the methods of an object. It also reflects the response of an object to other objects.
  *  **Identity:** It gives a unique name to an object and enables one object to interact with other objects.

![python class](https://media.geeksforgeeks.org/wp-content/uploads/Blank-
Diagram-Page-1-5.png)

#### Declaring Objects (Also called instantiating a class)

When an object of a class is created, the class is said to be instantiated.
All the instances share the attributes and the behavior of the class. But the
values of those attributes, i.e. the state are unique for each object. A
single class may have any number of instances.

Example:  

![python declaring an object](https://media.geeksforgeeks.org/wp-
content/uploads/Blank-Diagram-Page-1-3.png)

**Declaring an object –**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to

# demonstrate instantiating

# a class

class Dog:

 

 # A simple class

 # attribute

 attr1 = "mammal"

 attr2 = "dog"

 # A sample method 

 def fun(self):

 print("I'm a", self.attr1)

 print("I'm a", self.attr2)

# Driver code

# Object instantiation

Rodger = Dog()

# Accessing class attributes

# and method through objects

print(Rodger.attr1)

Rodger.fun()  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    mammal
    I'm a mammal
    I'm a dog

In the above example, an object is created which is basically a dog named
Rodger. This class only has two class attributes that tell us that Rodger is a
dog and a mammal.  

## The self

  * Class methods must have an extra first parameter in the method definition. We do not give a value for this parameter when we call the method, Python provides it.
  * If we have a method that takes no arguments, then we still have to have one argument.
  * This is similar to this pointer in C++ and this reference in Java.

When we call a method of this object as myobject.method(arg1, arg2), this is
automatically converted by Python into MyClass.method(myobject, arg1, arg2) –
this is all the special self is about.  

## __init__ method

The __init__ method is similar to constructors in C++ and Java. Constructors
are used to initializing the object’s state. Like methods, a constructor also
contains a collection of statements(i.e. instructions) that are executed at
the time of Object creation. It is run as soon as an object of a class is
instantiated. The method is useful to do any initialization you want to do
with your object.

## Python3

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

## Class and Instance Variables

Instance variables are for data unique to each instance and class variables
are for attributes and methods shared by all instances of the class. Instance
variables are variables whose value is assigned inside a constructor or method
with self whereas class variables are variables whose value is assigned in the
class.

Defining instance variable using a constructor.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to show that the variables with a value

# assigned in the class declaration, are class variables and

# variables inside methods and constructors are instance

# variables.

 

# Class for Dog

class Dog:

 

 # Class Variable

 animal = 'dog'

 

 # The init method or constructor

 def __init__(self, breed, color):

 

 # Instance Variable 

 self.breed = breed

 self.color = color 

 

# Objects of Dog class

Rodger = Dog("Pug", "brown")

Buzo = Dog("Bulldog", "black")

print('Rodger details:') 

print('Rodger is a', Rodger.animal)

print('Breed: ', Rodger.breed)

print('Color: ', Rodger.color)

print('\nBuzo details:') 

print('Buzo is a', Buzo.animal)

print('Breed: ', Buzo.breed)

print('Color: ', Buzo.color)

# Class variables can be accessed using class

# name also

print("\nAccessing class variable using class name")

print(Dog.animal)   
  
---  
  
__

__

**Output:**

    
    
    Rodger details:
    Rodger is a dog
    Breed:  Pug
    Color:  brown
    
    Buzo details:
    Buzo is a dog
    Breed:  Bulldog
    Color:  black
    
    Accessing class variable using class name
    dog

Defining instance variable using the normal method.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to show that we can create

# instance variables inside methods

 

# Class for Dog

class Dog:

 

 # Class Variable

 animal = 'dog'

 

 # The init method or constructor

 def __init__(self, breed):

 

 # Instance Variable

 self.breed = breed 

 

 # Adds an instance variable 

 def setColor(self, color):

 self.color = color

 

 # Retrieves instance variable 

 def getColor(self): 

 return self.color 

 

# Driver Code

Rodger = Dog("pug")

Rodger.setColor("brown")

print(Rodger.getColor())   
  
---  
  
__

__

**Output:**

    
    
    brown

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

