Variations in different Sorting techniques in Python



These are all different types for sorting techniques that behave very
differently. Let’s study which technique works how and which one to use.

 _Let ‘a’ be anumpy array_

  *  **a.sort()**  
(i) Sorts the array in-place & returns None  
(ii) Return type is None  
(iii) Occupies less space. No copy created as it directly sorts the original
array  
(iv) Faster than sorted(a)

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to sort an array in-place

# using a.sort

import numpy as np

 

# Numpy array created

a = np.array([9, 3, 1, 7, 4, 3, 6])

 

# unsorted array print

print('Original array:\n', a)

 

# Return type is None

print('Return type:', a.sort())

 

# Sorted array output

print('Original array sorted->', a)  
  
---  
  
 __

 __

    
        OUTPUT: For a.sort()
    Original array:
     [9 3 1 7 4 3 6]
    Return type: None
    Original array sorted-> [1 3 3 4 6 7 9]
    

  * **sorted(a)**  
(i) Creates a new list from the old & returns the new one, sorted  
(ii) Return type is a list  
(iii) Occupies more space as copy of original array is created and then
sorting is done  
(iv) Slower than a.sort()

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to create a sorted copy using

# sorted()

import numpy as np

 

# Numpy array created

a = np.array([9, 3, 1, 7, 4, 3, 6])

 

# unsorted array print

print('Original array:\n', a)

b = sorted(a)

 

# sorted list returned to b, b type is

# <class 'list'> 

print('New array sorted->', b)

 

# original array no change

print('Original array->', a)  
  
---  
  
 __

 __

    
        OUTPUT:a.sorted()
    Original array:
     [9 3 1 7 4 3 6]
    New array sorted-> [1, 3, 3, 4, 6, 7, 9]
    Original array-> [9 3 1 7 4 3 6]
    

  * **np.argsort(a)**  
(i) Returns the indices that would sort an array  
(ii) Return type is numpy array  
(iii) Occupies space as a new array of sorted indices is returned

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate working of np.argsort

import numpy as np

 

# Numpy array created

a = np.array([9, 3, 1, 7, 4, 3, 6])

 

# unsorted array print

print('Original array:\n', a)

 

# Sort array indices

b = np.argsort(a)

print('Sorted indices of original array->', b)

 

# To get sorted array using sorted indices

# c is temp array created of same len as of b

c = np.zeros(len(b), dtype = int)

for i in range(0, len(b)):

 c[i]= a[b[i]]

print('Sorted array->', c)  
  
---  
  
 __

 __

    
    
    OUTPUT:np.argsort(a)
    Original array:
     [9 3 1 7 4 3 6]
    Sorted indices of original array-> [2 1 5 4 6 3 0]
    Sorted array-> [1 3 3 4 6 7 9]
    

* **np.lexsort((b, a))**  
(i) Perform an indirect sort using a sequence of keys  
(ii) Sort by a, then by b  
(iii) Return type ndarray of ints Array of indices that sort the keys along
the specified axis  
(iv) Occupies space as a new array of sorted indices pair wise is returned.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate working of

# np.lexsort()

import numpy as np

 

# Numpy array created

a = np.array([9, 3, 1, 3, 4, 3, 6]) # First
column

b = np.array([4, 6, 9, 2, 1, 8, 7]) #
Second column

print('column a, column b')

for (i, j) in zip(a, b):

 print(i, ' ', j)

 

ind = np.lexsort((b, a)) # Sort by a then by b

print('Sorted indices->', ind)  
  
---  
  
 __

 __

    
    
    OUTPUT:np.lexsort((b, a))
    column a, column b
    9   4
    3   6
    1   9
    3   2
    4   1
    3   8
    6   7
    Sorted indices-> [2 3 1 5 4 6 0]
    

