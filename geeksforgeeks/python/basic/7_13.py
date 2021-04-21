Built-in Objects in Python-builtins



This Python module provides direct access to all ‘built-in’ identifiers of
Python. _For example_ , **builtins.open** is the full name for the built-in
function open(). This module is not normally accessed explicitly by most
applications, but can be useful in modules that provide objects with the same
name as a built-in value, but in which the built-in of that name is also
needed.

 **For example** , in a module that wants to implement an open() function
that wraps the built-in open(), this module can be used directly:

    
    
    open(path, 'r')

But in cases where there is a function with the same name as the builtin
functions these needs to be called explicitly:

    
    
    def open(path):
        f = builtins.open(path, 'r')
    

Here the first open function is defined by the programmer and the second one
is being imported from the builtins module.

 **Example:**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# without explicitly calling

# the builtins module

print(round(3.14))

 

 

# explicitly calling the 

# builtins module

import builtins

 

a = builtins.round(3.14)

print(a)  
  
---  
  
 __

 __

 **Output:**

    
    
    3
    3

One more interesting thing to keep in mind is that the compiler gives higher
priority to user-defined versions of the predefined functions contained by the
builtins module. So, if a program consists of a call to both types of
programs, the user-defined program will be called. To call the predefined
version builtins keyword should be used.

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

import builtins

 

 

def pow():

 

 print("inside user-defined function pow() \

 to calculate 2**3 ")

 val = 2

 

 for i in range(1, 3, 1):

 val=val*2

 

 return val

 

def main():

 

 print("calling for pre-defined version of pow() \

 from builtins module to calculate 2**3 ")

 

 print(builtins.pow(2, 3))

 a = pow()

 print(a)

 

# Driver Code

main()  
  
---  
  
 __

 __

 **Output:**

> calling for pre-defined version of pow() from builtins module to calculate
> 2**3  
> 8  
> inside user-defined function pow() to calculate 2**3  
> 8

#### Contents of Builtins Module

This module is automatically loaded every time the interpreter starts, this is
the reason why it is generally never called explicitly. The following are
defined within builtins:

  *  **The Object Class** – base class for all python objects
  *  **All Built-in Data-Type Class** – all data types like numbers, string, list etc.
  *  **Built-in Exception Classes** – like BaseException class, etc.
  *  **Built-in Functions** – functions like open(), abs(), all(), etc.
  *  **Built-in Constants** – constants like False, True, etc.

#### Built-in Data Type Classes

  *  **TRUTH VALUE TESTING-** statements and conditions for checking the validity of the code.
  *  **BOOLEAN OPERATIONS-** and, or, not.
  *  **COMPARISONS-** =, ==, !=, is and is not.
  *  **NUMERIC TYPES-** int, float, complex and bitwise operations like and, or, exclusive or, shifts and inverse.
  *  **ITERATOR TYPES-** operations related to iteration of a container.
  *  **SEQUENCE TYPES-** list, tuple, range and operations on these.
  *  **TEXT SEQUENCE TYPE-** str and methods related with string mutation and display.
  *  **BINARY SEQUENCE TYPE-** bytes, bytearray and memoryview.
  *  **SET TYPES-** set and frozenset.
  *  **MAPPING TYPES-** dict.
  *  **CONTEXT MANAGER TYPES-** runtime context related matter.
  *  **OTHERS –** module, instances, null object,

 **Example** : simple program to depict the application of builtin types

 __

 __  
 __

 __

 __  
 __  
 __

a=[1, 2, 3, 4]

 

for i in a:

 

 if i == 3:

 print("found")

 else:

 print("not found")  
  
---  
  
 __

 __

 **Output:**

    
    
    not found
    not found
    found
    not found

 **BUILT-IN FUNCTIONS** abs()| delattr()| hash()| memoryview()| set()| all()|
dict()| help()| min()| setattr()| any()| dir()| hex()| next()| slice()|
ascii()| divmod()| id()| object()| sorted()| bin()| enumerate()| input()|
oct()| staticmethod()| bool()| eval()| int()| open()| str()| breakpoint()|
exec()| isinstance()| ord()| sum()| bytearray()| filter()| issubclass()|
pow()| super()| bytes()| float()| iter()| print()| tuple()| callable()|
format()| len()| property()| type()| chr()| frozenset()| list()| range()|
vars()| classmethod()| getattr()| locals()| repr()| zip()| compile()|
globals()| map()| reversed()| __import__()| complex()| hasattr()| max()|
round()|  
---|---|---|---|---  
  
Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

