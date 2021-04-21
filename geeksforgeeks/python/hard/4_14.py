Nested Decorators in Python



Everything in Python is an object. Even function is a type of object in
Python. Decorators are a special type of function which return a wrapper
function. They are considered very powerful in Python and are used to modify
the behaviour of a function temporarily without changing its actual value.

Nesting means placing or storing inside the other. Therefore, Nested
Decorators means applying more than one decorator inside a function. Python
allows us to implement more than one decorator to a function. It makes
decorators useful for resuabale building blocks as it accumulates the several
effects together.

##  **How several decorators are applied?**

A function can be decorated multiple times. We need to define the decorator
first that we want to wrap the output string with, and then apply them to the
function using the ‘@’ . One simply needs to place the decorators above the
desired function.

 **Syntax :**

    
    
     _@function1_
    _@function2_
    _def function(name):_
    _print(f"{name}")_
    

Nested decorators follow a bottom to top approach i.e the reverse order. It
can be related to a construction of building where we start the construction
from the bottom (the ground) and then start building the floors.

  

  

 **Example :**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# nested decorators

 

def italic(func):

 

 def wrapper():

 return '<i>' + func() + '</i>'

 

 return wrapper

 

def strong(func):

 

 def wrapper():

 return '<strong>' + func() + '</strong>'

 

 return wrapper

 

 

@italic

@strong

def introduction():

 return 'This is a basic program'

 

print(introduction())  
  
---  
  
 __

 __

 **Output:**

    
    
    <i><strong>This is a basic program</strong></i>

 **Explanation :**

  1. We have defined two decorators first, which are used in wrapping the output string of the decorated function in the ‘strong’ and ‘italic’ tags of _HTML._
  2. Then we are applying the two decorators to our ‘introduction’ function by using just an “@” and the function name. For example in this program we are using @italic and @strong.
  3. The hierrachy that it follows is from bottom to top. Therefore according to it the string is wrapped with ‘strong’ first an then with ‘italic’.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

