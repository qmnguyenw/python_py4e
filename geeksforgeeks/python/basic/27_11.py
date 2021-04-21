Import module in Python



Import in python is similar to #include header_file in C/C++. Python modules
can get access to code from another module by importing the file/function
using import. The import statement is the most common way of invoking the
import machinery, but it is not the only way.

 **import module_name**  
When import is used, it searches for the module initially in the local scope
by calling __import__() function. The value returned by the function are then
reflected in the output of the initial code.

 __

 __  
 __

 __

 __  
 __  
 __

import math

print(math.pi)  
  
---  
  
 __

 __

Output:

    
    
    3.141592653589793

**import module_name.member_name**  
In the above code module math is imported, and its variables can be accessed
by considering it to be a class and pi as its object.  
The value of pi is returned by __import__().  
pi as whole can be imported into our intial code, rather than importing the
whole module.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

from math import pi

 

# Note that in the above example, 

# we used math.pi. Here we have used

# pi directly.

print(pi)  
  
---  
  
 __

 __

Output:

    
    
    3.141592653589793

**from module_name import ***  
In the above code module math is not imported, rather just pi has been
imported as a variable.  
All the functions and constants can be imported using *.

 __

 __  
 __

 __

 __  
 __  
 __

from math import *

print(pi)

print(factorial(6))  
  
---  
  
 __

 __

Output:

    
    
    3.141592653589793
    720
    

As said above import uses __import__() to search for module, and if not found,
it would raise ImportError

 __

 __  
 __

 __

 __  
 __  
 __

import mathematics

print(mathematics.pi)  
  
---  
  
 __

 __

Output:

    
    
    Traceback (most recent call last):
      File "C:/Users/GFG/Tuples/xxx.py", line 1, in 
        import mathematics
    ImportError: No module named 'mathematics'
    

This article is contributed by **Piyush Doorwar**. If you like GeeksforGeeks
and would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

