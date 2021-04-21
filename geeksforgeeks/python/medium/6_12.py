Calculate average values of two given NumPy arrays



Finding average of NumPy arrays is quite similar to finding average of given
numbers. We just have to get the sum of corresponding array elements and then
divide that sum with the total number of arrays.

Let’s see an example:

 **Example 1:** Calculate average values of two given NumPy 1d-arrays

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import library

import numpy as np

 

# create a numpy 1d-arrays

arr1 = np.array([3, 4])

arr2 = np.array([1, 0])

 

# find average of NumPy arrays

avg = (arr1 + arr2) / 2

 

print("Average of NumPy arrays:\n",

 avg)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    Average of NumPy arrays:
     [2. 2.]

 **Example 2:** Calculate average values of two given NumPy 2d-arrays

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import library

import numpy as np

 

# create a numpy 2d-arrays

arr1 = np.array([[3, 4], [8, 2]])

arr2 = np.array([[1, 0], [6, 6]])

 

# find average of NumPy arrays

avg = (arr1 + arr2) / 2

 

print("Average of NumPy arrays:\n",

 avg)  
  
---  
  
 __

 __

 **Output:**

    
    
    Average of NumPy arrays:
     [[2. 2.]
     [7. 4.]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

