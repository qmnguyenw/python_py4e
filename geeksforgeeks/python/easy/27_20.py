numpy.reshape() in Python



The **numpy.reshape()** function shapes an array without changing data of
array.

    
    
     **Syntax:** numpy.reshape(array, shape, order = 'C')

 **Parameters :**

    
    
    **array :** [array_like]Input array
    **shape :** [int or tuples of int] e.g. if we are aranging an array with 10 elements then shaping
            it like numpy.reshape(4, 8) is wrong; we can 
    **order  :** [C-contiguous, F-contiguous, A-contiguous; optional]         
             C-contiguous order in memory(last index varies the fastest)
             C order means that operating row-rise on the array will be slightly quicker
             FORTRAN-contiguous order in memory (first index varies the fastest).
             F order means that column-wise operations will be faster. 
             ‘A’ means to read / write the elements in Fortran-like index order if,
             array is Fortran contiguous in memory, C-like order otherwise
    
    

**Return :**

    
    
    Array which is reshaped without changing the data.
    

__

__  
__

__

__  
__  
__

# Python Program illustrating

# numpy.reshape() method

 

import numpy as geek

 

array = geek.arange(8)

print("Original array : \n", array)

 

# shape array with 2 rows and 4 columns

array = geek.arange(8).reshape(2, 4)

print("\narray reshaped with 2 rows and 4 columns : \n", array)

 

# shape array with 4 rows and 2 columns

array = geek.arange(8).reshape(4 ,2)

print("\narray reshaped with 2 rows and 4 columns : \n", array)

 

# Constructs 3D array

array = geek.arange(8).reshape(2, 2, 2)

print("\nOriginal array reshaped to 3D : \n", array)  
  
---  
  
 __

 __

 **Output :**

    
    
    Original array : 
     [0 1 2 3 4 5 6 7]
    
    array reshaped with 2 rows and 4 columns : 
     [[0 1 2 3]
     [4 5 6 7]]
    
    array reshaped with 4 rows and 2 columns : 
     [[0 1]
     [2 3]
     [4 5]
     [6 7]]
    
    Original array reshaped to 3D : 
     [[[0 1]
      [2 3]]
    
     [[4 5]
      [6 7]]]
    

**References :**  
https://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.reshape.html

  

  

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

