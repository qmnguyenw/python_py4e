Function Wrappers in Python



 **Wrappers** around the functions are also knows as **decorators** which are
a very powerful and useful tool in Python since it allows programmers to
modify the behavior of function or class. Decorators allow us to wrap another
function in order to extend the behavior of the wrapped function, without
permanently modifying it. In Decorators, functions are taken as the argument
into another function and then called inside the wrapper function.

 **Syntax:**

    
    
    @wrapper
    def function(n):
        statements(s)

This is also similar to

    
    
    def function(n):
        statement(s)
    
    function = wrapper(function)

Let’s see the below examples for better understanding.  
 **Example 1:**

 __

 __  
 __

 __

 __  
 __  
 __

# defining a decorator

def hello_decorator(func): 

 

 # inner1 is a Wrapper function in 

 # which the argument is called 

 

 # inner function can access the outer local 

 # functions like in this case "func" 

 def inner1(): 

 print("Hello, this is before function execution") 

 

 # calling the actual function now 

 # inside the wrapper function. 

 func() 

 

 print("This is after function execution") 

 

 return inner1 

 

 

# defining a function, to be called inside wrapper 

def function_to_be_used(): 

 print("This is inside the function !!") 

 

 

# passing 'function_to_be_used' inside the 

# decorator to control its behavior 

function_to_be_used = hello_decorator(function_to_be_used) 

 

 

# calling the function 

function_to_be_used()   
  
---  
  
__

__

**Output:**

  

  

    
    
    Hello, this is before function execution
    This is inside the function !!
    This is after function execution

 **Example 2:** Let’s define a decorator that count the time taken by the
function for execution.

 __

 __  
 __

 __

 __  
 __  
 __

import time

 

 

def timeis(func):

 '''Decorator that reports the execution time.'''

 

 def wrap(*args, **kwargs):

 start = time.time()

 result = func(*args, **kwargs)

 end = time.time()

 

 print(func.__name__, end-start)

 return result

 return wrap

 

@timeis

def countdown(n):

 '''Counts down'''

 while n > 0:

 n -= 1

 

countdown(5)

countdown(1000)  
  
---  
  
 __

 __

 **Output:**

    
    
    countdown 1.6689300537109375e-06
    countdown 5.507469177246094e-05

It’s critical to emphasize that decorators generally do not alter the calling
signature or return value of function being wrapped. The use of ***args** and
****kwargs** is there to make sure that any input arguments can be accepted.
The return value of a decorator is almost always the result of calling
**func(*args, **kwargs)** , where func is the original unwrapped function.

Please refer Decorators in Python for more details.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

