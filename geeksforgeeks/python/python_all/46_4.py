Compute the inner product of vectors for 1-D arrays using NumPy in Python



Python has a popular package called NumPy which used to perform complex
calculations on 1-D and multi-dimensional arrays. To find the inner product of
two arrays, we can use the inner() function of the NumPy package.

>  **Syntax:** numpy.inner(array1, array2)
>
>  **Parameters:**
>
>  **array1, array2:** arrays to be evaluated
>
>  **Returns:** Inner Product of two arrays
>
>  
>
>
>  
>

 **Example 1:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Importing library

import numpy as np

 

# Creating two 1-D arrays

array1 = np.array([6,2])

array2 = np.array([2,5])

 

print("Original 1-D arrays:")

print(array1)

print(array2)

 

# Output

print("Inner Product of the two array is:")

result = np.inner(array1, array2)

print(result)  
  
---  
  
 __

 __

 **Output:**

    
    
    Original 1-D arrays:
    [6 2]
    [2 5]
    Inner Product of the two array is:
    22
    

**Example 2:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Importing library

import numpy as np

 

# Creating two 1-D arrays

array1 = np.array([1,3,5])

array2 = np.array([0,1,5])

 

print("Original 1-D arrays:")

print(array1)

print(array2)

 

# Output

print("Inner Product of the two array is:")

result = np.inner(array1, array2)

print(result)  
  
---  
  
 __

 __

 **Output:**

    
    
    Original 1-D arrays:
    [1 3 5]
    [0 1 5]
    Inner Product of the two array is:
    28
    

**Example 3:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Importing library

import numpy as np

 

# Creating two 1-D arrays

array1 = np.array([1,2,2,8])

array2 = np.array([2,1,0,6])

 

print("Original 1-D arrays:")

print(array1)

print(array2)

 

# Output

print("Inner Product of the two array is:")

result = np.inner(array1, array2)

print(result)  
  
---  
  
 __

 __

 **Output:**

    
    
    Original 1-D arrays:
    [1 2 2 8]
    [2 1 0 6]
    Inner Product of the two array is:
    52
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

