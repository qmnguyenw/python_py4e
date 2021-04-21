Why import star in Python is a bad idea



Using **import *** in python programs is considered a bad habit because this
way you are polluting your namespace, the import * statement imports all the
functions and classes into your own namespace, which may clash with the
functions you define or functions of other libraries that you import. Also it
becomes very difficult at some times to say from which library does a
particular function came from. The risk of overriding the variables/functions
etc always persist with the import * practice.

Below are some points about why **import *** should not be used:

  * Code Readability
  * It is always remains a mystery what is imported and cannot be found easily from which module a certain thing was imported that result in low code readability.
  * Polluting the namespace, import * imports all the functions and classes in your own namespace that may clash with the function and classes you define or function and classes of other libraries that you may import.
  * Concrete possibility of hiding bugs
  * Tools like pyflakes can’t be used to statically detect errors in the source code.

All of this does not mean that using **import *** is always bad, if i had told
you that there is nothing like import * thing on this universe you would have
been craving for it. The only thing you should remember while using import *
is that you should always use this carefully and with discipline maintained.

Now lets dive into an example to see the problem in a more practical and easy
to understand way.

consider a package **a** that contains a function **sum (a, b)**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# import the module a using import *

from a import *

 

# define a function sum

def sum (x, y):

 return x + y

 

print (sum (2, 6))  
  
---  
  
 __

 __

the error with this code is that the sum function that we define overrides the
sum function from the module ‘a’ that we imported and we don’t even have any
idea about it. also it becomes very difficult to identify which function is
actually being called in case of large programs.

Correct method:

 __

 __  
 __

 __

 __  
 __  
 __

# import the module a as l

import a as l

 

def sum (x, y):

 return x + y

 

# calls the self-defined sum function

print (sum (2, 6))

 

# calls the sum function defined in the module a

print (l.sum(2, 6))  
  
---  
  
 __

 __

Coding this way increases code readability as well as it becomes easy to debug
and there are almost zero chances that any conflict will occur.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

