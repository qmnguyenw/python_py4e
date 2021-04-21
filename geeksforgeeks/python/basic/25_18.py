numpy.isinf() in Python



The **numpy.isinf()** function tests element-wise whether it is +ve or -ve
infinity or not return the result as a boolean array.

    
    
     **Syntax:** numpy.isinf(array [, out])

 **Parameters :**

    
    
    array : [array_like]Input array or object whose 
             elements, we need to test for  infinity
    out   : [ndarray, optional]Output array placed 
            with result. Its type is preserved and
            it  must be of the right shape to hold 
             the output.
    

**Return :**

    
    
    boolean array containing the result. For scalar 
    input, the result is a new boolean with value
    True if the input is positive or negative infinity; 
    otherwise the value is False. For array input, the 
    result is a boolean array with the same shape as 
    the input and the values are True where the 
    corresponding element of the input is positive
    or negative infinity; elsewhere the values are False.
    

**Code 1 :**

 __

 __  
 __

 __

 __  
 __  
 __

# Python Program illustrating

# numpy.isinf() method

 

import numpy as geek 

 

print("Finite : ", geek.isinf(1), "\n")

 

print("Finite : ", geek.isinf(0), "\n")

 

# not a number

print("Finite : ", geek.isinf(geek.nan), "\n")

 

# infinity

print("Finite : ", geek.isinf(geek.inf), "\n")

 

print("Finite : ", geek.isinf(geek.NINF), "\n") 

 

x = geek.array([-geek.inf, 0., geek.inf])

y = geek.array([2, 2, 2])

print("Checking for infinity : ", geek.isinf(x, y))   
  
---  
  
__

__

**Output :**

  

  

    
    
    Finite :  False 
    
    Finite :  False 
    
    Finite :  False 
    
    Finite :  True 
    
    Finite :  True 
    
    Checking for infinity :  [1 0 1]
    
    

**Code 2 :**

 __

 __  
 __

 __

 __  
 __  
 __

# Python Program illustrating

# numpy.isinf() method

 

import numpy as geek 

 

# Returns True/False value for each element 

b = geek.arange(8).reshape(2, 4)

 

print("\n",b)

print("\nIs Infifnity : \n", geek.isinf(b))

 

# geek.inf : Positive Infinity

# geek.NINF : negative Infinity

b = [[geek.inf], 

 [geek.NINF]]

print("\nIs Infifnity : \n", geek.isinf(b))  
  
---  
  
 __

 __

 **Output :**

    
    
    
     [[0 1 2 3]
     [4 5 6 7]]
    
    Is Infifnity : 
     [[False False False False]
     [False False False False]]
    
    Is Infifnity : 
     [[ True]
     [ True]]

 **References :**  
https://docs.scipy.org/doc/numpy-
dev/reference/generated/numpy.isinf.html#numpy.isinf

 **Note :**  
These codes won’t run on online-ID. Please run them on your systems to explore
the working.  
.  
This article is contributed by **Mohit Gupta_OMG 😀**. If you like
GeeksforGeeks and would like to contribute, you can also write an article
using contribute.geeksforgeeks.org or mail your article to
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

