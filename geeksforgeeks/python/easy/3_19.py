Compute the Reciprocal for all elements in a NumPy array



In this article, let’s discuss how to compute the reciprocal for all the
elements of a given NumPy array.

 **Method 1:** Through **reciprocal_arr = 1/arr** statement, we can convert
every element of arr to it reciprocal and saved it to reciprocal_arr.But there
is a catch, you will be encountered with an error if any element of “arr” be
zero. So be careful not to pass any array to reciprocal_arr which contains 0.

 **Example 1:**

## Python

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# PROGRAM TO FIND RECIPROCAL OF EACH

# ELEMENT OF NUMPY ARRAY

import numpy as np

 

lst = [22, 34, 65, 50, 7]

arr = np.array(lst)

reciprocal_arr = 1/arr

 

print(reciprocal_arr)  
  
---  
  
 __

 __

