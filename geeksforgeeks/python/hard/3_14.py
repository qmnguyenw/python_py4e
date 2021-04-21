Abstract Base Class (abc) in Python



Have you ever thought about checking whether the objects you are using adheres
to a particular specification? It is necessary to verify whether an object
implements a given method or property, especially while creating a library
where other developers make use of it. A developer can use hasattr or
isinstance methods to check whether the input conforms to a particular
identity. But sometimes it is inconvenient to use those methods to check a
myriad of different properties and methods.

As a solution to this inconvenience, Python introduced a concept called
**abstract base class (abc)**. In this section, we will discuss the abstract
base class and its importance.

  * Abstract Base Class
  * Declaring an Abstract Base Class
  * Why declare an Abstract Base Class?
  * Abstract Properties
  * Built-In Abstract Classes

## Abstract Base Class

The main goal of the abstract base class is to provide a standardized way to
test whether an object adheres to a given specification. It can also prevent
any attempt to instantiate a subclass that doesn’t override a particular
method in the superclass. And finally, using an abstract class, a class can
derive identity from another class without any object inheritance.

## Declaring an Abstract Base Class

Python has a module called abc (abstract base class) that offers the necessary
tools for crafting an abstract base class. First and foremost, you should
understand the ABCMeta metaclass provided by the abstract base class. The rule
is every abstract class must use ABCMeta metaclass.

ABCMeta metaclass provides a method called register method that can be invoked
by its instance. By using this register method, any abstract base class can
become an ancestor of any arbitrary concrete class. Let’s understand this
process by considering an example of an abstract base class that registers
itself as an ancestor of dict.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import abc

 

 

class AbstractClass(metaclass=abc.ABCMeta):

 def abstractfunc(self):

 return None

 

 

print(AbstractClass.register(dict))  
  
---  
  
 __

 __

 **Output:**

    
    
    <class 'dict'>

Here, dict identifies itself as a subclass of AbstractClass. Let’s do a check.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import abc

 

 

class AbstractClass(metaclass=abc.ABCMeta):

 def abstractfunc(self):

 return None

 

 

AbstractClass.register(dict)

print(issubclass(dict, AbstractClass))  
  
---  
  
 __

 __

 **Output:**

    
    
    True

## Why Declare an Abstract Base Class?

To understand the need to declare a virtual subclass, we need to consider the
example of a list-like object where you don’t want to put a restriction of
only considering list or tuple. Before that let’s see how to use
**isinstance** to check against a list or tuple of class.

    
    
    isinstance([], (list, tuple))
    

This _isinstance_ check meets the purpose if you are accepting only a list or
tuple. But here the case is different, there is no such restriction. So, this
solution is not extensible for a developer who uses your library to send
something else other than a list or tuple. Here comes the importance of
abstract class. Let’s understand through the below code.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import abc

 

 

class MySequence(metaclass=abc.ABCMeta):

 pass

 

MySequence.register(list)

MySequence.register(tuple)

 

a = [1, 2, 3]

b = ('x', 'y', 'z')

 

print('List instance:', isinstance(a, MySequence))

print('Tuple instance:', isinstance(b, MySequence))

print('Object instance:', isinstance(object(), MySequence))  
  
---  
  
 __

 __

 **Output:**

    
    
    List instance: True
    Tuple instance: True
    Object instance: False

As you can see, when you do isinstance check, it returns true for both the
list and tuple; for the other objects, it returns false. Let’s consider a
scenario where a developer expects a class object itself. In the above case,
the isinstance will return false. But it can be achieved by creating a custom
class and registering it with the abstract base class.

Here ‘MySequence’ is an abstract class within the library. A developer can
import it and register a custom class. Let’s have a look at the below code.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import abc

 

 

class MySequence(metaclass=abc.ABCMeta):

 pass

 

class CustomListLikeObjCls(object):

 pass

 

MySequence.register(CustomListLikeObjCls)

print(issubclass(CustomListLikeObjCls, MySequence))  
  
---  
  
 __

 __

 **Output:**

    
    
    True

Here, CustomListLikeObjCls instance is passed to the library by registering it
with MySequence. Therefore, the instance check returns True. Apart from the
above method, you can also use the register method as a decorator to register
a custom class. Let’s see how to use the **register method as a decorator**.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import abc

 

 

class MySequence(metaclass=abc.ABCMeta):

 pass

 

@MySequence.register

class CustomListLikeObjCls(object):

 pass

 

print(issubclass(CustomListLikeObjCls, MySequence))  
  
---  
  
 __

 __

 **Output:**

    
    
    True

Registering a class using the above-implemented method meets the purpose.
However, you have to do manual registration for every intended subclass. How
about automatic subclassing based on a particular method?. An abstract class
has a concept called __subclasshook__ to subclass the classes.

### __subclasshook___

It is a special magic method defined by ABCMeta. The __subclasshook__ must be
defined as a class method using @classmethod decorator. It takes one
additional positional argument other than the class and can return either of
the three values – True, False, or NotImplemented. Let’s look at the below
implementation.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import abc

 

 

class AbstractClass(metaclass=abc.ABCMeta):

 @classmethod

 def __subclasshook__(cls, other):

 print('subclass hook:', other)

 hookmethod = getattr(other, 'hookmethod', None)

 return callable(hookmethod)

 

class SubClass(object):

 def hookmethod(self):

 pass

 

class NormalClass(object):

 hookmethod = 'hook'

 

 

print(issubclass(SubClass, AbstractClass))

print(issubclass(NormalClass, AbstractClass))  
  
---  
  
 __

 __

 **Output:**

    
    
    subclass hook: <class '__main__.SubClass'>
    True
    subclass hook: <class '__main__.NormalClass'>
    False

From the above discussion, you understood how to hook subclasses
automatically. Now we will look into how to avoid instantiating a subclass
that doesn’t override a particular method in the superclass. This feature can
be achieved using @abc.abstractmethod.

### @abc.abstractmethod

@abc.abstractmethod prevents any attempt to instantiate a subclass that
doesn’t override a particular method in the superclass. Let’s have a look at
the below code:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import abc

 

 

class AbstractClass(metaclass=abc.ABCMeta):

 @abc.abstractmethod

 def abstractName(self):

 pass

 

class InvalidSubClass(AbstractClass):

 pass

 

isc = InvalidSubClass()  
  
---  
  
 __

 __

Since the InvalidSubclass doesn’t override the method abstractName, the
@abc.abstractmethod prevents the subclass from instantiation and throws the
below error.

> Traceback (most recent call last):  
>  File “/home/553d5199a662239eae3ff58efb37b6ec.py”, line 11, in <module>  
>  isc = InvalidSubClass()  
> TypeError: Can’t instantiate abstract class InvalidSubClass with abstract
> methods abstractName

Let’s look into another example where the subclass overrides the abstract
method.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import abc

 

class AbstractClass(metaclass=abc.ABCMeta):

 @abc.abstractmethod

 def abstractName(self):

 pass

 

class ValidSubClass(AbstractClass):

 def abstractName(self):

 return 'Abstract 1'

 

vc = ValidSubClass()

print(vc.abstractName())  
  
---  
  
 __

 __

 **Output:**

    
    
    Abstract 1

Next, let’s see how to declare properties as an abstract class.

## Abstract Properties

We can use @property decorator and @abc.abstractmethod to declare properties
as an abstract class. Let’s look into the below code.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import abc

 

 

class AbstractClass(metaclass=abc.ABCMeta):

 @property

 @abc.abstractmethod

 def abstractName(self):

 pass

 

 

class ValidSubClass(AbstractClass):

 @property

 def abstractName(self):

 return 'Abstract 1'

 

 

vc = ValidSubClass()

print(vc.abstractName)  
  
---  
  
 __

 __

 **Output:**

    
    
    Abstract 1

## Built-in Abstract classes

Python 3 standard library provides a few built-in abstract classes for both
abstract and non-abstract methods. These include sequence, mutable sequence,
iterable, and so on. It often serves as an alternative to subclassing a built-
in Python class. For example, subclassing the MutableSequence can substitute
the subclassing of list or str. The main purpose of using Abstract class is
that it allows you to consider a common type of collection rather than coding
for each type of collection. Here we will discuss Single-Method ABCs and
Alternative-Collection ABCs.

  * Single-Method ABCs
  * Alternative-Collection ABCs

### Single-Method ABCs

Python has five abstract base classes. They are as follows:

  * Callable (__call__)
  * Container (__contains__)
  * Hashable (__hash__)
  * Iterable (__iter__)
  * Sized (__len__)

These abstract base classes contain one abstract method each. Let’s consider
an example of the __len__ method.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from collections.abc import Sized

 

 

class SingleMethod(object):

 def __len__(self):

 return 10

 

 

print(issubclass(SingleMethod, Sized))  
  
---  
  
 __

 __

 **Output:**

    
    
    True

Any class that has the appropriate method is considered as the subclass of the
abstract base class. Out of the above five abstract base classes, the Iterator
is slightly different. It provides an implementation for __iter__ and adds an
abstract method called __next__.

### Alternative-Collection ABCs

Alternative-Collection ABCs are built-in abstract base classes that identify
subclasses, which serve similar purposes. They can be divided into three
categories. Let’s go through one by one.

  *  **Sequence and Mutable Sequence** : Sequence and Mutable Sequence are abstract base classes that generally behaves like tuples or list. A sequence abstract base class requires __getitem__ and __len__ , whereas mutable sequence needs __setitem__ and __getitem__.
  *  **Mapping** : Mapping comes with mutable mapping, which is mainly for dictionary-like objects
  *  **Set** : The set comes with a mutable set that is intended for unordered collections.

## Summary

The key purpose of the abstract class is to check whether an object conforms
to a particular protocol. It is a valuable class for testing certain
attributes of a class or testing class itself. However, there are many other
things that the abstract class does not check. Some of them are signatures,
return type, etc. Another advantage is it provides a flexible way for
developers to test common types of collections.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

