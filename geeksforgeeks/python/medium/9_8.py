How to pass argument to an Exception in Python?



There might arise a situation where there is a need for additional information
from an exception raised by Python.  
Python has two types of exceptions namely, Built-In Exceptions and User-
Defined Exceptions.

 **Why use Argument in Exceptions?**  
Using arguments for Exceptions in Python is useful for the following reasons:

  * It can be used to gain additional information about the error encountered.
  * As contents of an Argument can vary depending upon different types of Exceptions in Python, Variables can be supplied to the Exceptions to capture the essence of the encountered errors. Same error can occur of different causes, Arguments helps us identify the specific cause for an error using the **except** clause.
  * It can also be used to trap multiple exceptions, by using a variable to follow the tuple of Exceptions.

 **Arguments in Buil-in Exceptions:**

The below codes demonstrates use of Argument with Built-in Exceptions:

 **Example 1:**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

try:

 b = float(100 + 50 / 0)

except Exception as Argument:

 print( 'This is the Argument\n', Argument)  
  
---  
  
 __

 __

 **Output:**

    
    
    This is the Argument
     division by zero

 **Example 2:**

 __

 __  
 __

 __

 __  
 __  
 __

my_string= "GeeksForGeeks"

 

try:

 b = float(my_string / 20)

except Exception as Argument:

 print( 'This is the Argument\n', Argument)  
  
---  
  
 __

 __

 **Output:**

    
    
    This is the Argument
     unsupported operand type(s) for /: 'str' and 'int'

 **Arguments in User-defined Exceptions:**

The below codes demonstrates use of Argument with User-defined Exceptions:

 **Example 1:**

 __

 __  
 __

 __

 __  
 __  
 __

# create user-defined exception

# derived from super class Exception 

class MyError(Exception): 

 

 # Constructor or Initializer 

 def __init__(self, value): 

 self.value = value 

 

 # __str__ is to print() the value 

 def __str__(self): 

 return(repr(self.value)) 

 

try: 

 raise(MyError("Some Error Data")) 

 

# Value of Exception is stored in error 

except MyError as Argument: 

 print('This is the Argument\n', Argument)   
  
---  
  
__

__

**Output:**

    
    
    This is the Argument
     'Some Error Data'

 **Example 2:**

 __

 __  
 __

 __

 __  
 __  
 __

# class Error is derived from super class Exception

class Error(Exception): 

 

 # Error is derived class for Exception, but 

 # Base class for exceptions in this module 

 pass

 

class TransitionError(Error): 

 

 # Raised when an operation attempts a state 

 # transition that's not allowed. 

 def __init__(self, prev, nex, msg): 

 self.prev = prev 

 self.next = nex 

 

try: 

 raise(TransitionError(2, 3 * 2, "Not Allowed")) 

 

# Value of Exception is stored in error 

except TransitionError as Argument: 

 print('Exception occurred: ', Argument)   
  
---  
  
__

__

**Output:**

    
    
    Exception occurred:  (2, 6, 'Not Allowed')

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

