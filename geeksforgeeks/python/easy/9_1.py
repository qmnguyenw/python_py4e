Python | functools.wraps() function



 **functools** is a standard Python module for higher-order functions
(functions that act on or return other functions). wraps() is a decorator
that is applied to the wrapper function of a decorator. It updates the
wrapper function to look like wrapped function by coping attributes such
as __name__, __doc__ (the docstring), etc.

>  **Syntax:** @functools.wraps(wrapped, assigned = WRAPPER_ASSIGNMENTS,
> updated = WRAPPER_UPDATES)
>
>  **Parameters:**  
>  **wrapped** : The function name that is to be decorated by wrapper
> function.  
>  **assigned** : Tuple to specify which attributes of the original function
> are assigned directly to the matching attributes on the wrapper function. By
> default set to WRAPPER_ASSIGNMENTS (which assigns to the wrapper function’s
> __module__, __name__, __qualname__, __annotations__ and __doc__, the
> documentation string)  
>  **updated** : Tuple to specify which attributes of the wrapper function are
> updated with the corresponding attributes from the original function. By
> default set to WRAPPER_UPDATES (which updates the wrapper function’s
> __dict__, i.e. the instance dictionary).

 **Example 1:** Without functools.wraps()

 __

 __  
 __

 __

 __  
 __  
 __

def a_decorator(func):

 def wrapper(*args, **kwargs):

 """A wrapper function"""

 # Extend some capabilities of func

 func()

 return wrapper

 

@a_decorator

def first_function():

 """This is docstring for first function"""

 print("first function")

 

@a_decorator

def second_function(a):

 """This is docstring for second function"""

 print("second function")

 

print(first_function.__name__)

print(first_function.__doc__)

print(second_function.__name__)

print(second_function.__doc__)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    wrapper
    A wrapper function
    wrapper
    A wrapper function
    

