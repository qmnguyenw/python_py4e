numpy.zeros() in Python



The **numpy.zeros()** function returns a new array of given shape and type,
with zeros.  
 **Syntax:**

    
    
    numpy.zeros(shape, dtype = None, order = 'C')

 **Parameters :**

    
    
    **shape :** integer or sequence of integers
    **order  :** C_contiguous or F_contiguous
             C-contiguous order in memory(last index varies the fastest)
             C order means that operating row-rise on the array will be slightly quicker
             FORTRAN-contiguous order in memory (first index varies the fastest).
             F order means that column-wise operations will be faster. 
    **dtype :** [optional, float(byDeafult)] Data type of returned array.  
    

**Returns :**

    
    
    ndarray of zeros having given shape, order and datatype.

 **  
Code 1 :**

 __

 __  
 __

 __

 __  
 __  
 __

# Python Program illustrating

# numpy.zeros method

 

import numpy as geek

 

b = geek.zeros(2, dtype = int)

print("Matrix b : \n", b)

 

a = geek.zeros([2, 2], dtype = int)

print("\nMatrix a : \n", a)

 

c = geek.zeros([3, 3])

print("\nMatrix c : \n", c)  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    Matrix b : 
     [0 0]
    
    Matrix a : 
     [[0 0]
     [0 0]]
    
    Matrix c : 
     [[ 0.  0.  0.]
     [ 0.  0.  0.]
     [ 0.  0.  0.]]
    

**  
Code 2 : Manipulating data types**

 __

 __  
 __

 __

 __  
 __  
 __

# Python Program illustrating

# numpy.zeros method

 

import numpy as geek

 

# manipulation with data-types

b = geek.zeros((2,), dtype=[('x', 'float'), ('y',
'int')])

print(b)  
  
---  
  
 __

 __

 **Output :**

    
    
    [(0.0, 0) (0.0, 0)]
    

**Reference :**  
https://docs.scipy.org/doc/numpy-
dev/reference/generated/numpy.zeros.html#numpy.zeros  
 **Note :** zeros, unlike zeros and empty, does not set the array values to
zero or random values respectively.Also, these codes won’t run on online-ID.
Please run them on your systems to explore the working.

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

