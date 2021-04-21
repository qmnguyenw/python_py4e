User-defined Exceptions in Python with Examples



Prerequisite- This article is an extension to Exception Handling.

Python throws errors and exceptions, when there is a code gone wrong, which
may cause program to stop abruptly. Python also provides exception handling
method with the help of try-except. Some of the standard exceptions which are
most frequent include IndexError, ImportError, IOError, ZeroDivisionError,
TypeError and FileNotFoundError. A user can create his own error using
exception class.

 **Creating User-defined Exception**

Programmers may name their own exceptions by creating a new exception class.
Exceptions need to be derived from the Exception class, either directly or
indirectly. Although not mandatory, most of the exceptions are named as names
that end in **“Error”** similar to naming of the standard exceptions in
python. For example:

 __

 __  
 __

 __

 __  
 __  
 __

# A python program to create user-defined exception

 

# class MyError is derived from super class Exception

class MyError(Exception):

 

 # Constructor or Initializer

 def __init__(self, value):

 self.value = value

 

 # __str__ is to print() the value

 def __str__(self):

 return(repr(self.value))

 

try:

 raise(MyError(3*2))

 

# Value of Exception is stored in error

except MyError as error:

 print('A New Exception occured: ',error.value)  
  
---  
  
 __

 __

Output:

  

  

    
    
    ('A New Exception occured: ', 6)

 **Knowing all about Exception Class**

To know more about about class Exception, run the code below

 __

 __  
 __

 __

 __  
 __  
 __

help(Exception)  
  
---  
  
 __

 __

 **Deriving Error from Super Class Exception**

Super class Exceptions are created when a module needs to handle several
distinct errors. One of the common way of doing this is to create a base class
for exceptions defined by that module. Further, various subclasses are defined
to create specific exception classes for different error conditions.

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

 

 # Error message thrown is saved in msg

 self.msg = msg

try:

 raise(TransitionError(2,3*2,"Not Allowed"))

 

# Value of Exception is stored in error

except TransitionError as error:

 print('Exception occured: ',error.msg)  
  
---  
  
 __

 __

Output:

    
    
    ('Exception occured: ', 'Not Allowed')
    

**How to use standard Exceptions as base class?**

Runtime error is a class is a standard exception which is raised when a
generated error does not fall into any category. This program illustrates how
to use runtime error as base class and network error as derived class. In a
similar way, any exception can be derived from the standard exceptions of
Python.

 __

 __  
 __

 __

 __  
 __  
 __

# NetworkError has base RuntimeError

# and not Exception

class Networkerror(RuntimeError):

 def __init__(self, arg):

 self.args = arg

 

try:

 raise Networkerror("Error")

 

except Networkerror as e:

 print (e.args)  
  
---  
  
 __

 __

Output:

    
    
    ('E', 'r', 'r', 'o', 'r')
    

This article is contributed by **Piyush Doorwar**. If you like GeeksforGeeks
and would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

