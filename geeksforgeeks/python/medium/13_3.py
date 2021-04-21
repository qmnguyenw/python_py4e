Duck Typing in Python



 **Duck Typing** is a type system used in dynamic languages. For example,
Python, Perl, Ruby, PHP, Javascript, etc. where the type or the class of an
object is less important than the method it defines. Using Duck Typing, we do
not check types at all. Instead, we check for the presence of a given method
or attribute.

The name Duck Typing comes from the phrase:

> “If it looks like a duck and quacks like a duck, it’s a duck”

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# duck typing

 

class Specialstring:

 def __len__(self):

 return 21

 

# Driver's code

if __name__ == "__main__":

 

 string = Specialstring()

 print(len(string))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    21

In this case, we call method len() gives the return value from __len__
method. Here __len__ method defines the property of the class
Specialstring

The object’s type itself is not significant in this we do not declare the
argument in method prototypes. This means that compilers can not do type-
checking. Therefore, what really matters is if the object has particular
attributes at run time. Duck typing is hence implemented by dynamic languages.
But now some of the static languages like Haskell also supports it. But,
Java/C# doesn’t have this ability yet.

 **Example:** Now, lets look demonstrates how an object be used in any other
circumstances until it is not supported.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# duck typing

 

 

class Bird:

 def fly(self):

 print("fly with wings")

 

class Airplane:

 def fly(self):

 print("fly with fuel")

 

class Fish:

 def swim(self):

 print("fish swim in sea")

 

# Attributes having same name are

# considered as duck typing

for obj in Bird(), Airplane(), Fish():

 obj.fly()  
  
---  
  
 __

 __

 **Output:**

    
    
    fly with wings
    fly with fuel
    
    
    
    Traceback (most recent call last):
      File "/home/854855e5570b9ce4a9e984209b6a1c21.py", line 20, in 
        obj.fly()
    AttributeError: 'Fish' object has no attribute 'fly'
    

In this example, we can see a class supports some method we can modify it or
give them new functionality. Duck-typing emphasis what the object can really
do, rather than what the object is.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

