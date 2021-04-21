Create a Pandas Series from array



 **Pandas Series** is a one-dimensional labelled array capable of holding any
data type (integers, strings, floating point numbers, Python objects, etc.).
It has to be remembered that unlike Python lists, a Series will always contain
data of the same type.

Let’s see how to create a Pandas Series from the array.

 **Method #1:** Create a series from array without index.

In this case as no index is passed, so by default index will be range(n)
where _n_ is array length.

 __

 __  
 __

 __

 __  
 __  
 __

# importing Pandas& numpy

import pandas as pd

import numpy as np

 

# numpy array

data = np.array(['a', 'b', 'c', 'd', 'e'])

 

# creating series

s = pd.Series(data)

print(s)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    0    a
    1    b
    2    c
    3    d
    4    e
    dtype: object
    

