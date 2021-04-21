Abstract Classes in Python



An abstract class can be considered as a blueprint for other classes. It
allows you to create a set of methods that must be created within any child
classes built from the abstract class. A class which contains one or more
abstract methods is called an abstract class. An abstract method is a method
that has a declaration but does not have an implementation. While we are
designing large functional units we use an abstract class. When we want to
provide a common interface for different implementations of a component, we
use an abstract class.  
  
**Why use Abstract Base Classes :**  
By defining an abstract base class, you can define a common Application
Program Interface(API) for a set of subclasses. This capability is especially
useful in situations where a third-party is going to provide implementations,
such as with plugins, but can also help you when working in a large team or
with a large code-base where keeping all classes in your mind is difficult or
not possible.  
  
**How Abstract Base classes work :**  
By default, Python does not provide abstract classes. Python comes with a
module that provides the base for defining Abstract Base classes(ABC) and that
module name is ABC. _**ABC**_ works by decorating methods of the base class as
abstract and then registering concrete classes as implementations of the
abstract base. A method becomes abstract when decorated with the keyword
@abstractmethod. For Example –  

**Code 1:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program showing

# abstract base class work

from abc import ABC, abstractmethod

class Polygon(ABC):

 @abstractmethod

 def noofsides(self):

 pass

class Triangle(Polygon):

 # overriding abstract method

 def noofsides(self):

 print("I have 3 sides")

class Pentagon(Polygon):

 # overriding abstract method

 def noofsides(self):

 print("I have 5 sides")

class Hexagon(Polygon):

 # overriding abstract method

 def noofsides(self):

 print("I have 6 sides")

class Quadrilateral(Polygon):

 # overriding abstract method

 def noofsides(self):

 print("I have 4 sides")

# Driver code

R = Triangle()

R.noofsides()

K = Quadrilateral()

K.noofsides()

R = Pentagon()

R.noofsides()

K = Hexagon()

K.noofsides()  
  
---  
  
 __

 __

 **Output:**  

    
    
    I have 3 sides
    I have 4 sides
    I have 5 sides
    I have 6 sides

  
**Code 2:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program showing

# abstract base class work

from abc import ABC, abstractmethod

class Animal(ABC):

 def move(self):

 pass

class Human(Animal):

 def move(self):

 print("I can walk and run")

class Snake(Animal):

 def move(self):

 print("I can crawl")

class Dog(Animal):

 def move(self):

 print("I can bark")

class Lion(Animal):

 def move(self):

 print("I can roar")

 

# Driver code

R = Human()

R.move()

K = Snake()

K.move()

R = Dog()

R.move()

K = Lion()

K.move()  
  
---  
  
 __

 __

 **Output:**  

  

  

    
    
    I can walk and run
    I can crawl
    I can bark
    I can roar

  
**Implementation Through Subclassing :**  
By subclassing directly from the base, we can avoid the need to register the
class explicitly. In this case, the Python class management is used to
recognize _PluginImplementation_ as implementing the abstract PluginBase.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program showing

# implementation of abstract

# class through subclassing

import abc

class parent: 

 def geeks(self):

 pass

class child(parent):

 def geeks(self):

 print("child class")

# Driver code

print( issubclass(child, parent))

print( isinstance(child(), parent))  
  
---  
  
 __

 __

 **Output:**  

    
    
    True
    True

A side-effect of using direct subclassing is, it is possible to find all the
implementations of your plugin by asking the base class for the list of known
classes derived from it.  
  
**Concrete Methods in Abstract Base Classes :**  
Concrete classes contain only concrete (normal)methods whereas abstract
classes may contain both concrete methods and abstract methods. The concrete
class provides an implementation of abstract methods, the abstract base class
can also provide an implementation by invoking the methods via super().  

Let look over the example to invoke the method using super():

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program invoking a

# method using super()

import abc

from abc import ABC, abstractmethod

class R(ABC):

 def rk(self):

 print("Abstract Base Class")

class K(R):

 def rk(self):

 super().rk()

 print("subclass ")

# Driver code

r = K()

r.rk()  
  
---  
  
 __

 __

 **Output:**  

    
    
    Abstract Base Class
    subclass

In the above program, we can invoke the methods in abstract classes by using
super().  
  
**Abstract Properties :**  
Abstract classes include attributes in addition to methods, you can require
the attributes in concrete classes by defining them with @abstractproperty.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program showing

# abstract properties

import abc

from abc import ABC, abstractmethod

class parent(ABC):

 @abc.abstractproperty

 def geeks(self):

 return "parent class"

class child(parent):

 

 @property

 def geeks(self):

 return "child class"

 

 

try:

 r =parent()

 print( r.geeks)

except Exception as err:

 print (err)

 

r = child()

print (r.geeks)  
  
---  
  
 __

 __

 **Output:**  

    
    
    Can't instantiate abstract class parent with abstract methods geeks
    child class

In the above example, the Base class cannot be instantiated because it has
only an abstract version of the property getter method.  
  
**Abstract Class Instantiation :**  
Abstract classes are incomplete because they have methods that have nobody. If
python allows creating an object for abstract classes then using that object
if anyone calls the abstract method, but there is no actual implementation to
invoke. So we use an abstract class as a template and according to the need,
we extend it and build on it before we can use it. Due to the fact, an
abstract class is not a concrete class, it cannot be instantiated. When we
create an object for the abstract class it raises an _error_.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program showing

# abstract class cannot

# be an instantiation

from abc import ABC,abstractmethod

class Animal(ABC):

 @abstractmethod

 def move(self):

 pass

class Human(Animal):

 def move(self):

 print("I can walk and run")

class Snake(Animal):

 def move(self):

 print("I can crawl")

class Dog(Animal):

 def move(self):

 print("I can bark")

class Lion(Animal):

 def move(self):

 print("I can roar")

c=Animal()  
  
---  
  
 __

 __

 **Output:**  

    
    
    Traceback (most recent call last):
      File "/home/ffe4267d930f204512b7f501bb1bc489.py", line 19, in 
        c=Animal()
    TypeError: Can't instantiate abstract class Animal with abstract methods move

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

