numpy.argmax() in Python



The **numpy.argmax()** function returns indices of the max element of the
array in a particular axis.

 **Syntax :**

    
    
    numpy.argmax(array, axis = None, out = None)

 **Parameters :**

    
    
    **array :** Input array to work on 
    **axis  :** [int, optional]Along a specified axis like 0 or 1
    **out   :** [array optional]Provides a feature to insert output to the **out**
              array and it should be of appropriate shape and dtype
    

**Return :**

    
    
    Array of indices into the array with same shape as array.shape
     with the dimension along axis removed.

 **Code 1 :**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python Program illustrating

# working of argmax()

 

import numpy as geek 

 

# Working on 2D array

array = geek.arange(12).reshape(3, 4)

print("INPUT ARRAY : \n", array)

 

# No axis mentioned, so works on entire array

print("\nMax element : ", geek.argmax(array))

 

# returning Indices of the max element

# as per the indices

print("\nIndices of Max element : ", geek.argmax(array, axis=0))

print("\nIndices of Max element : ", geek.argmax(array, axis=1))  
  
---  
  
 __

 __

 **Output :**

    
    
    INPUT ARRAY : 
     [[ 0  1  2  3]
     [ 4  5  6  7]
     [ 8  9 10 11]]
    
    Max element :  11
    
    Indices of Max element :  [2 2 2 2]
    
    Indices of Max element :  [3 3 3]
    

**Code 2 :**

 __

 __  
 __

 __

 __  
 __  
 __

# Python Program illustarting

# working of argmax()

 

import numpy as geek 

 

# Working on 2D array

array = geek.random.randint(16, size=(4, 4))

print("INPUT ARRAY : \n", array)

 

# No axis mentioned, so works on entire array

print("\nMax element : ", geek.argmax(array))

 

# returning Indices of the max element

# as per the indices

 

''' 

 [[ 0 3 8 13]

 [12 11 2 11]

 [ 5 13 8 3]

 [12 15 3 4]]

 ^ ^ ^ ^

 12 15 8 13 - element

 1 3 0 0 - indices

'''

print("\nIndices of Max element : ", geek.argmax(array, axis =
0))

 

 

''' 

 ELEMENT INDEX

 ->[[ 0 3 8 13] 13 3

 ->[12 11 2 11] 12 0

 ->[ 5 13 8 3] 13 1

 ->[12 15 3 4]] 15 1

 

'''

print("\nIndices of Max element : ", geek.argmax(array, axis =
1))  
  
---  
  
 __

 __

 **Output :**

    
    
    INPUT ARRAY : 
     [[ 0  3  8 13]
      [12 11  2 11]
      [ 5 13  8  3]
      [12 15  3  4]]
    
    Max element :  15
    
    Indices of Max element :  [1 3 0 0]
    
    Indices of Max element :  [3 0 1 1]
    

**Code 3 :**

 __

 __  
 __

 __

 __  
 __  
 __

# Python Program illustarting

# working of argmax()

 

import numpy as geek 

 

# Working on 2D array

array = geek.arange(10).reshape(2, 5)

print("array : \n", array)

 

array[0][1] = 6

print("\narray : \n", array)

 

# Returns max element

print("\narray : ", geek.argmax(array))

 

# First occurrence of an max element is given

print("\nMAX ELEMENT INDICES : ", geek.argmax(array, axis = 0))  
  
---  
  
 __

 __

 **Output :**

    
    
    array : 
     [[0 1 2 3 4]
     [5 6 7 8 9]]
    
    array : 
     [[0 6 2 3 4]
     [5 6 7 8 9]]
    
    array :  9
    
    MAX ELEMENT INDICES :  [1 0 1 1 1]
    

**References :**  
https://docs.scipy.org/doc/numpy-
dev/reference/generated/numpy.argmax.html#numpy.argmax

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

