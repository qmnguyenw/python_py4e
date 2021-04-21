__exit__ in Python



Context manager is used for managing resources used by the program. After
completion of usage, we have to release memory and terminate connections
between files. If they are not released then it will lead to resource leakage
and may cause the system to either slow down or crash. Even if we do not
release resources, context managers implicitly performs this task.

> Refer the below article to get the idea about basics of Context Manager.
>
> * Context Manager  
>

## __exit__() method

This is a method of ContextManager class. The __exit__ method takes care
of releasing the resources occupied with the current code snippet. This method
must be executed no matter what after we are done with the resources. This
method contains instructions for properly closing the resource handler so that
the resource is freed for further use by other programs in the OS.

If an exception is raised; its type, value, and traceback are passed as
arguments to __exit__(). Otherwise, three None arguments are supplied. If
the exception is suppressed, then the return value from the __exit__()
method will be True, otherwise, False.

>  **syntax:** __exit__(self, exception_type, exception_value,
> exception_traceback)
>
>  
>
>
>  
>
>
>  **parameters:**  
>  **exception_type:** indicates class of exception.  
>  **exception_value:** indicates type of exception . like divide_by_zero
> error, floating_point_error, which are types of arithmetic exception.  
>  **exception_traceback:** traceback is a report which has all of the
> information needed to solve the exception.

 **# Example 1:**.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program creating a

# context manager 

 

class ContextManager(): 

 def __init__(self): 

 print('init method called') 

 

 def __enter__(self): 

 print('enter method called') 

 return self

 

 def __exit__(self, exc_type, exc_value, exc_traceback): 

 print('exit method called') 

 

 

with ContextManager() as manager: 

 print('with statement block')  
  
---  
  
 __

 __

 **Output :**

    
    
    init method called
    enter method called
    with statement block
    exit method called
    

**# Example 2:** Understanding parameters of __exit__(). We will create a
context manager that will be used to divide two numbers. If the

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# __exit__ method

 

class Divide:

 def __init__(self, num1, num2):

 self.num1 = num1

 self.num2 = num2

 

 def __enter__(self):

 print("Inside __enter__")

 return self

 

 def __exit__(self, exc_type, exc_value, traceback):

 print("\nInside __exit__")

 print("\nExecution type:", exc_type)

 print("\nExecution value:", exc_value)

 print("\nTraceback:", traceback)

 

 def divide_by_zero(self):

 # causes ZeroDivisionError exception

 print(self.num1 / self.num2)

 

 

# Driver's code

with Divide(3, 1) as r:

 r.divide_by_zero()

 

print("................................................")

 

# will raise a ZeroDivisionError

with Divide(3, 0) as r:

 r.divide_by_zero()  
  
---  
  
 __

 __

 **Output:**

    
    
    Inside __enter__
    3.0
    
    Inside __exit__
    
    Execution type: None
    
    Execution value: None
    
    Traceback: None
    ................................................
    Inside __enter__
    
    Inside __exit__
    
    Execution type: 
    
    Execution value: division by zero
    
    Traceback: 
    Traceback (most recent call last):
      File "gfg.py", line 32, in 
        r.divide_by_zero()
      File "gfg.py", line 21, in divide_by_zero
        print(self.num1 / self.num2)
    ZeroDivisionError: division by zero
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

