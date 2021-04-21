Python | Raising an Exception to Another Exception



Let’s consider a situation where we want to raise an exception in response to
catching a different exception but want to include information about both
exceptions in the traceback.

To chain exceptions, use the raise from statement instead of a simple raise
statement. This will give you information about both errors.

 **Code #1 :**

 __

 __  
 __

 __

 __  
 __  
 __

def example():

 try:

 int('N/A')

 except ValueError as e:

 raise RuntimeError('A parsing error occurred') from e...

 

example()  
  
---  
  
 __

 __

 **Output :**

    
    
    Traceback (most recent call last):
      File "", line 3, in example
    ValueError: invalid literal for int() with base 10: 'N/A'
    

This exception is the direct cause of the following exception –

  

  

    
    
    Traceback (most recent call last):
      File "", line 1, in 
      File "", line 5, in example
    RuntimeError: A parsing error occurred
    

Both exceptions are captured in the traceback. A normal except statement is
used to catch such an exception. However, __cause__ attribute of the
exception object can be looked to follow the exception chain as explained in
the code given below.

 **Code #2 :**

 __

 __  
 __

 __

 __  
 __  
 __

try:

 example()

except RuntimeError as e:

 print("It didn't work:", e)

 if e.__cause__:

 print('Cause:', e.__cause__)  
  
---  
  
 __

 __

An implicit form of chained exceptions occurs when another exception gets
raised inside an except block.

 **Code #3 :**

 __

 __  
 __

 __

 __  
 __  
 __

def example2():

 try:

 int('N/A')

 except ValueError as e:

 print("Couldn't parse:", err)

 

example2()  
  
---  
  
 __

 __

    
    
    Traceback (most recent call last):
        File " ", line 3, in example2
    ValueError: invalid literal for int() with base 10: 'N / A'
    

During handling of the above exception, another exception occurred:

    
    
    Traceback (most recent call last):
        File "", line 1, in 
        File "", line 5, in example2
    NameError: global name 'err' is not defined
    

In the code below, the NameError exception is raised as the result of a
programming error, not in direct response to the parsing error. For this case,
the __cause__ attribute of an exception is not set. Instead, a __context__
attribute is set to the prior exception.

 **Code #4 : To suppress chaining, use raise from None**

 __

 __  
 __

 __

 __  
 __  
 __

def example3():

 try:

 int('N / A')

 except ValueError:

 raise RuntimeError('A parsing error occurred') from None...

 

example3()  
  
---  
  
 __

 __

 **Output :**

    
    
    Traceback (most recent call last):
        File "", line 1, in 
        File "", line 5, in example3
    RuntimeError: A parsing error occurred
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

