numpy.all() in Python



The **numpy.all()** function tests whether all array elements along the
mentioned axis evaluate to True.

    
    
     **Syntax:** numpy.all(array,
                        axis = None,
                        out = None,
                        keepdims = class numpy._globals._NoValue at 0x40ba726c)

 **Parameters :**

    
    
    **array    :** [array_like]Input array or object whose elements, we need to test.
    **axis     :** [int or tuple of ints, optional]Axis along which array elements 
         are evaluated.
         The default (axis = None) is to perform a logical AND over all the dimensions of the input
         array. Axis may be negative, in which case it counts from the last to the first axis.
    **out      :** [ndarray, optional]Output array with same dimensions as Input array, 
         placed with result
    **keepdmis :** [boolean, optional]If this is set to True, the axes which are 
         reduced are left in the result as dimensions with size one. With this option, the result 
         will broadcast correctly against the input array.
         If the default value is passed, then keepdims will not be passed through to the all 
         method of sub-classes of ndarray, however any non-default value will be. If the 
         sub-classes sum method does not implement keepdims any exceptions will be raised.
    

**Return :**

    
    
    A new Boolean array as per 'out' parameter
    

**Code 1 :**

 __

 __  
 __

 __

 __  
 __  
 __

# Python Program illustrating

# numpy.all() method

 

import numpy as geek

 

# Axis = NULL 

# True False

# True True

# True : False = False

 

print("Bool Value with axis = NONE : ",

 geek.all([[True,False],[True,True]]))

 

# Axis = 0 

# True False

# True True

# True : False

print("\nBool Value with axis = 0 : ",

 geek.all([[True,False],[True,True]], axis = 0))

 

print("\nBool : ", geek.all([-1, 4, 5]))

 

 

# Not a Number (NaN), positive infinity and negative infinity 

# evaluate to True because these are not equal to zero.

print("\nBool : ", geek.all([1.0, geek.nan]))

 

print("\nBool Value : ", geek.all([[0, 0],[0,
0]]))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    Bool Value with axis = NONE  :  False
    
    Bool Value with axis = 0  :  [ True False]
    
    Bool :  True
    
    Bool :  True
    
    Bool Value :  False
    

**Code 2 :**

 __

 __  
 __

 __

 __  
 __  
 __

# Python Program illustrating

# numpy.all() method

 

# Parameter : keepdmis 

 

import numpy as geek

 

# setting keepdmis = True

print("\nBool Value : ", geek.all([[1, 0],[0, 4]],
True))

 

 

# setting keepdmis = True

print("\nBool Value : ", geek.all([[0, 0],[0, 0]],
False))  
  
---  
  
 __

 __

 **Output :**

    
    
    
    Bool Value :  [False False]
    
    Bool Value :  [False False]
    VisibleDeprecationWarning: using a boolean instead of an integer
     will result in an error in the future
     return umr_all(a, axis, dtype, out, keepdims)
    

**References :**  
https://docs.scipy.org/doc/numpy-
dev/reference/generated/numpy.all.html#numpy.all

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

