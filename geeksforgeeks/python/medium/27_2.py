Python Closures



Before seeing what a closure is, we have to first understand what nested
functions and non-local variables are.  

### **Nested functions in Python**

A function that is defined inside another function is known as a nested
function. Nested functions are able to access variables of the enclosing
scope.  
In Python, these non-local variables can be accessed only within their scope
and not outside their scope. This can be illustrated by the following example:

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to illustrate

# nested functions

def outerFunction(text):

 text = text

 def innerFunction():

 print(text)

 innerFunction()

if __name__ == '__main__':

 outerFunction('Hey!')  
  
---  
  
 __

 __

As we can see innerFunction() can easily be accessed inside the outerFunction
body but not outside of it’s body. Hence, here, innerFunction() is treated as
nested Function which uses **text** as non-local variable.  

### **Python Closures**

A Closure is a function object that remembers values in enclosing scopes even
if they are not present in memory.  

  * It is a record that stores a function together with an environment: a mapping associating each free variable of the function (variables that are used locally but defined in an enclosing scope) with the value or reference to which the name was bound when the closure was created.
  * A closure—unlike a plain function—allows the function to access those captured variables through the closure’s copies of their values or references, even when the function is invoked outside their scope.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to illustrate

# closures

def outerFunction(text):

 text = text

 def innerFunction():

 print(text)

 # Note we are returning function

 # WITHOUT parenthesis

 return innerFunction 

if __name__ == '__main__':

 myFunction = outerFunction('Hey!')

 myFunction()  
  
---  
  
 __

 __

    
    
    Output:
    omkarpathak@omkarpathak-Inspiron-3542:
    ~/Documents/Python-Programs/$ python Closures.py 
    Hey!

  1. As observed from the above code, closures help to invoke functions outside their scope.
  2. The function **innerFunction** has its scope only inside the outerFunction. But with the use of closures, we can easily extend its scope to invoke a function outside its scope.

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to illustrate

# closures

import logging

logging.basicConfig(filename='example.log',

 level=logging.INFO)

def logger(func):

 def log_func(*args):

 logging.info(

 'Running "{}" with arguments {}'.format(func.__name__,

 args))

 print(func(*args))

 

 # Necessary for closure to

 # work (returning WITHOUT parenthesis)

 return log_func 

def add(x, y):

 return x+y

def sub(x, y):

 return x-y

add_logger = logger(add)

sub_logger = logger(sub)

add_logger(3, 3)

add_logger(4, 5)

sub_logger(10, 5)

sub_logger(20, 10)  
  
---  
  
 __

 __

