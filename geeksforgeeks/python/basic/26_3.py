numpy.full_like() in Python



The **numpy.full_like()** function return a new array with the same shape and
type as a given array.

 **Syntax :**

    
    
    numpy.full_like(a, fill_value, dtype = None, order = 'K', subok = True)

 **Parameters :**

    
    
    **shape :** Number of rows
    **order :** C_contiguous or F_contiguous
    **dtype :** [optional, float(by Default )] Data type of returned array.  
    **subok :** [bool, optional] to make subclass of a or not
    

**Returns :**

    
    
    ndarray
    

__

__  
__

__

__  
__  
__

# Python Programming illustrating

# numpy.full_like method

 

import numpy as geek

 

x = geek.arange(10, dtype = int).reshape(2, 5)

print("x before full_like : \n", x)

 

# using full_like

print("\nx after full_like : \n", geek.full_like(x, 10.0))

 

y = geek.arange(10, dtype = float).reshape(2, 5)

print("\n\ny before full_like : \n", x)

 

# using full_like

print("\ny after full_like : \n", geek.full_like(y, 0.01))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    x before full_like : 
     [[0 1 2 3 4]
     [5 6 7 8 9]]
    
    x after full_like : 
     [[10 10 10 10 10]
     [10 10 10 10 10]]
    
    
    y before full_like : 
     [[0 1 2 3 4]
     [5 6 7 8 9]]
    
    y after full_like : 
     [[ 0.01  0.01  0.01  0.01  0.01]
     [ 0.01  0.01  0.01  0.01  0.01]]
    

**References :**  
https://docs.scipy.org/doc/numpy/reference/generated/numpy.full_like.html#numpy.full_like  
 **Note :**  
These codes won’t run on online-ID. Please run them on your systems to explore
the working  
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

