Type Systems:Dynamic Typing, Static Typing & Duck Typing



In Dynamic Typing, type checking is performed at runtime. For example, Python
is a dynamically typed language. It means that the type of a variable is
allowed to change over its lifetime. Other dynamically typed languages are
-Perl, Ruby, PHP, Javascript etc.  
Let’s take a Python code example to see if a variable can change type:

 __

 __  
 __

 __

 __  
 __  
 __





## variable a is assigned to a string

a ="hello"

print(type(a))

 

## variable a is assigned to an integer

a = 5

print(type(a))  
  
---  
  
 __

 __

This confirms that the type of variable “a” is allowed to change and Python
correctly infers the type as it changes.

Let’s take another example of Dynamic Typing in Python :

 __

 __  
 __

 __

 __  
 __  
 __

## simple function

def add(a, b):

 return a + b

 

## calling the function with string

print(add('hello', 'world'))

 

## calling the function with integer

print(add(2, 4))  
  
---  
  
 __

 __

In Python, we don’t really have a good idea of what are the types that this
function deals with and also what the type of the return value is going to be.

 **Static Typing:**

Static Typing is opposite to Dynamic Typing. In Static Typing, type checking
is performed during compile time. It means that the type of a variable is
known at compile time. For some languages, the programmer must specify what
type each variable is (e.g C, C++, Java), other languages offer some form of
type inference(e.g. Scala, Haskell).  
With Static Typing, variables generally are not allowed to change types.  
Let’s look at a simple example from a statically typed language. Consider the
following Java snippet;

  

  

 __

 __  
 __

 __

 __  
 __  
 __

String a;

a = "Java is good";  
  
---  
  
 __

 __

The first line declares that the variable “a” is bound to the string type at
compile time. In the second line, “a” is assigned a value which is not a
string object. For example, if we say, a =5, the compiler would raise an error
because of incompatible types.

 **Duck Typing**

Duck Typing is a concept related to Dynamic Typing, where the type or the
class of an object is less important than the method it defines.Using Duck
Typing, we do not check types at all. Instead we check for the presence of a
given method or attribute.  
The reason behind the name is the duck test: “If it looks like a duck, swims
like a duck, and quack like a duck, then it probably is a duck”.  
Let’s take a simple Python code example to understand it clearly:

 __

 __  
 __

 __

 __  
 __  
 __

class Duck:

 def quack(self):

 print("Quack")

 

class Goose:

 def quack(self):

 print("Quack Quack")

 

class Dog:

 def bark(self):

 print("I just bark")

 

class ItQuacks:

 def __init__(self, animal):

 animal.quack()

 

ItQuacks(Duck())

ItQuacks(Goose())

ItQuacks(Dog())  
  
---  
  
 __

 __

The classes which have an implementation of “quack” method will be able to
call (Duck, Goose objects) but for the “Dog” class which does not provide an
implementation of “quack” method, gets a “AttributeError” if we try to pass an
object.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

