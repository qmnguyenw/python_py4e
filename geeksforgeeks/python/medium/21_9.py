How to Call a C function in Python



Have you ever came across the situation where you have to call C function
using python? This article is going to help you on a very basic level and if
you have not come across any situation like this, you enjoy knowing how it is
possible.  
First, let’s write one simple function using C and generate a shared library
of the file. Let’s say file name is function.c.

## C

 __

 __  
 __

 __

 __  
 __  
 __

int myFunction(int num)

{

 if (num == 0)

 // if number is 0, do not perform any operation.

 return 0;

 else

 // if number is power of 2, return 1 else return 0

 return ((num & (num - 1)) == 0 ? 1 : 0) ;

}  
  
---  
  
 __

 __

Compile this :

    
    
    cc -fPIC -shared -o libfun.so function.c

###  **Using ctypes(foreign function interface) library to call C function
from Python**

The above statement will generate a shared library with the name libfun.so.
Now, let’s see how to make use of it in python. In python, we have one library
called ctypes. Using this library we can use C function in python.  
Let’s say file name is function.py.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import ctypes

NUM = 16

# libfun loaded to the python file

# using fun.myFunction(),

# C function can be accessed

# but type of argument is the problem.

 

fun = ctypes.CDLL("libfun.so") # Or full path to file 

# Now whenever argument

# will be passed to the function 

# ctypes will check it.

 

fun.myFunction.argtypes = [ctypes.c_int]

# now we can call this

# function using instant (fun)

# returnValue is the value

# return by function written in C

# code

returnVale = fun.myFunction(NUM)   
  
---  
  
__

__

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

