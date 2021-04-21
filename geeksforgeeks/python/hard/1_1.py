Timing Functions With Decorators – Python



Everything in Python is an object. Functions in Python also object. Hence,
like any other object they can be referenced by variables, stored in data
structures like dictionary or list, passed as an argument to another function,
and returned as a value from another function. In this article, we are going
to see the timing function with decorators.

 **Decorator:** A decorator is used to supercharge or modify a function. A
decorator is a higher-order function that wraps another function and enhances
it or changes it.

**Example :**

The best way to explain what it is by coding our own decorator. Suppose, you
want to print * 10 times before and after the output of some function. It
would be very inconvenient to use print statements in every function again and
again. We can do this efficiently with the help of a decorator.

 **Code:**

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

def my_decorator(func):

 def wrapper_function(*args, **kwargs):

 print("*"*10)

 func(*args, **kwargs)

 print("*"*10)

 return wrapper_function

 

 

def say_hello():

 print("Hello Geeks!")

 

@my_decorator

def say_bye():

 print("Bye Geeks!")

 

 

say_hello = my_decorator(say_hello)

say_hello()

say_bye()  
  
---  
  
 __

 __

 **Output:**

    
    
    **********
    Hello Geeks!
    **********
    **********
    Bye Geeks!
    **********

 **Explanation :**

In the above example, my_decorator **** is a decorator function, which accepts
func, a function object as an argument. It defines a wrapper_function which
calls func **** and executes the code that it contains as well. The
my_decorator function returns this wrapper_function.

So, what happens when we write @my_decorator before defining any function?
Consider the example of the say_hello function above which is not decorated by
any decorator at the time of definition. We can still use our decorator for
decorating its output by calling the my_decorator function and passing the
say_hello function object as a parameter, which will return a wrapper_function
with two print statements, calling the say_hello() function in between. If we
receive this modified function in the say_hello object itself, whenever we
call say_hello() we’ll get the modified output.

Instead of writing this complex syntax, we can simply write @my_decorator
before defining the function and leave the rest of the work for python
interpreter as shown in the case of say_bye function.

##  **Timer Function using Decorator**

The timer function is one of the applications of decorators. In the below
example, we have made a timer_func function that accepts a function object
func. Inside the timer function, we have defined wrap_func which can take any
number of arguments (*args) and any number of keyword arguments (**kwargs)
passed to it. We did this to make our timer_func more flexible.

In the body of wrap_func, we recorded the current time t1 using the time
method of the time module, then we have called the function func passing the
same parameters (*args, **kwargs) that were received by wrap_func and stored
the returned value in the result. Now we have again recorded the current time
t2 and printed the difference between the recorded times i.e. { t2 – t1 } with
precision up to the 4th decimal place. This {t2 – t1} is the time passed
during the execution of the function func. At last, we have returned the
result value inside wrap_func function and returned this wrap_func function
inside timer_func function.

  

  

We have also defined the long_time function using @timer_func decorator, so
whenever we call long_time function it will be called like :

    
    
    timer_func(long_time)(5)

The timer_func function when called passing long_time as a parameter returns a
wrap_func function and a function object func starts pointing to the long_time
function.

    
    
    wrap_func(5)

Now the wrap_func will execute as explained above and the result is returned.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from time import time

 

 

def timer_func(func):

 # This function shows the execution time of 

 # the function object passed

 def wrap_func(*args, **kwargs):

 t1 = time()

 result = func(*args, **kwargs)

 t2 = time()

 print(f'Function {func.__name__!r} executed in {(t2-t1):.4f}s')

 return result

 return wrap_func

 

 

@timer_func

def long_time(n):

 for i in range(n):

 for j in range(100000):

 i*j

 

 

long_time(5)  
  
---  
  
 __

 __

 **Output:**

    
    
    Function 'long_time' executed in 0.0219s

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

