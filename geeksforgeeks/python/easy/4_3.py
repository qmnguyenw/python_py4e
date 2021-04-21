Debugging decorators in Python



Decorators in Python are really a very powerful feature. If you are a web
developer and you have used the Django framework or even some other
development frameworks you would have already come across decorators.

For an overview decorators are wrapper functions that wrap an existing
function or a method and modify its features. Let’s take a short example.
Consider that you have a speak function that returns a neutral message

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

def speak():

 """Returns a neutral message"""

 return "Hi, Geeks!"

 

# printing the output

print(speak())  
  
---  
  
 __

 __

 **Output:**

    
    
    Hi, Geeks!
    

Suppose that you need to modify the function to return a message in a happy
tone. So let’s create a decorator for this.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# decorator

def make_geek_happy(func):

 def wrapper():

 neutral_message = func()

 happy_message = neutral_message + " You are happy!"

 return happy_message

 return wrapper

 

#using the decorator 

@make_geek_happy

def speak():

 """Returns a neutral message"""

 return "Hi, Geeks!"

 

print(speak())  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    Hi, Geeks! You are happy!
    

## Debugging a decorator

In this way, the decorators can also be used to modify different functions and
make them more useful. However, there are some drawbacks to this process. When
we wrap the original function in a decorator the metadata of the original
function gets lost. Consider the below program but this time we use the
decorator in another way just to make you understand.

If you try to access any of the metadata of the positive_message function it
actually returns the metadata of the wrapper inside the decorator.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# decorator

def make_geek_happy(func):

 def wrapper():

 neutral_message = func()

 happy_message = neutral_message + " You are happy!"

 return happy_message

 return wrapper

 

def speak():

 """Returns a neutral message"""

 return "Hi!"

 

 

# wrapping the function in the decorator

# and assigning it to positive_message

positive_message = make_geek_happy(speak)

 

print(positive_message())

 

print(speak.__name__) 

print(speak.__doc__) 

print(positive_message.__name__)

print(positive_message.__doc__)  
  
---  
  
 __

 __

 **Output:**

    
    
    Hi! You are happy!
    speak
    Returns a neutral message
    wrapper
    None
    

These results make it really very difficult for debugging. But thanks to
Python it also has a solution to fix this problem without much effort. We just
need to use the **functools.wraps()** decorator included in the Python
standard library.

Here’s an example:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing the module

import functools

 

# decorator

def make_geek_happy(func):

 @functools.wraps(func)

 def wrapper():

 neutral_message = func()

 happy_message = neutral_message + " You are happy!"

 return happy_message

 return wrapper

 

def speak():

 """Returns a neutral message"""

 return "Hi!"

 

positive_message = make_geek_happy(speak)

print(positive_message())

 

print(speak.__name__) 

print(speak.__doc__) 

print(positive_message.__name__)

print(positive_message.__doc__)  
  
---  
  
 __

 __

 **Output:**

    
    
    Hi! You are happy!
    speak
    Returns a neutral message
    speak
    Returns a neutral message
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

