numpy.ravel() in Python



The **numpy.ravel()** functions returns contiguous flattened array(1D array
with all the input-array elements and with the same type as it). A copy is
made only if needed.  
 **Syntax :**

    
    
    numpy.ravel(array, order = 'C')

 **Parameters :**

    
    
    **array :** [array_like]Input array. 
    **order :** [C-contiguous, F-contiguous, A-contiguous; optional]         
             C-contiguous order in memory(last index varies the fastest)
             C order means that operating row-rise on the array will be slightly quicker
             FORTRAN-contiguous order in memory (first index varies the fastest).
             F order means that column-wise operations will be faster. 
             ‘A’ means to read / write the elements in Fortran-like index order if,
             array is Fortran contiguous in memory, C-like order otherwise
    

**Return :**

    
    
    Flattened array having same type as the Input array and and order as per choice. 
    

**Code 1 : Shows that array.ravel is equivalent to reshape(-1, order=order)**

 __

 __  
 __

 __

 __  
 __  
 __

# Python Program illustrating

# numpy.ravel() method

 

import numpy as geek

 

array = geek.arange(15).reshape(3, 5)

print("Original array : \n", array)

 

# Outpue comes like [ 0 1 2 ..., 12 13 14]

# as it is a long output, so it is the way of

# showing outptut in Python

print("\nravel() : ", array.ravel())

 

# This shows array.ravel is equivalent to reshape(-1, order=order).

print("\nnumpy.ravel() == numpy.reshape(-1)")

print("Reshaping array : ", array.reshape(-1))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    Original array : 
     [[ 0  1  2  3  4]
     [ 5  6  7  8  9]
     [10 11 12 13 14]]
    
    ravel() :  [ 0  1  2 ..., 12 13 14]
    
    numpy.ravel() == numpy.reshape(-1)
    Reshaping array :  [ 0  1  2 ..., 12 13 14]
    

**Code 2 :Showing ordering manipulation**

 __

 __  
 __

 __

 __  
 __  
 __

# Python Program illustrating

# numpy.ravel() method

 

import numpy as geek

 

array = geek.arange(15).reshape(3, 5)

print("Original array : \n", array)

 

# Outpue comes like [ 0 1 2 ..., 12 13 14]

# as it is a long output, so it is the way of

# showing outptut in Python

 

# About : 

print("\nAbout numpy.ravel() : ", array.ravel)

 

print("\nnumpy.ravel() : ", array.ravel())

 

# Maintaining both 'A' and 'F' order

print("\nMaintains A Order : ", array.ravel(order = 'A'))

 

# K-order preserving the ordering

# 'K' means that is neither 'A' nor 'F'

array2 =
geek.arange(12).reshape(2,3,2).swapaxes(1,2)

print("\narray2 \n", array2)

print("\nMaintains A Order : ", array2.ravel(order = 'K'))  
  
---  
  
 __

 __

 **Output :**

    
    
    Original array : 
     [[ 0  1  2  3  4]
     [ 5  6  7  8  9]
     [10 11 12 13 14]]
    
    About numpy.ravel() :  
    
    numpy.ravel() :  [ 0  1  2 ..., 12 13 14]
    
    Maintains A Order :  [ 0  1  2 ..., 12 13 14]
    
    array2 
     [[[ 0  2  4]
      [ 1  3  5]]
    
     [[ 6  8 10]
      [ 7  9 11]]]
    
    Maintains A Order :  [ 0  1  2 ...,  9 10 11]
    

**References :**  
https://docs.scipy.org/doc/numpy-
dev/reference/generated/numpy.ravel.html#numpy.ravel

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

