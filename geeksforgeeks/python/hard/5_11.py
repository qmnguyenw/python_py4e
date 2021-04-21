Indexing Multi-dimensional arrays in Python using NumPy



NumPy is a general-purpose array-processing package. It provides a high-
performance multidimensional array object and tools for working with these
arrays. It is the fundamental package for scientific computing with Python. It
contains various features.

 **Note:** For more information, refer to Python Numpy

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

# numpy library imported

import numpy as np

 

# creating single-dimensional array

arr_s = np.arange(5)

print(arr_s)  
  
---  
  
 __

 __

 **Output:**

    
    
    [0 1 2 3 4]

 **arange()** method in numpy creates single dimension array of length 5.
Single parameter inside the **arange()** method acts as the end element for
the range. **arange()** also takes start and end arguments with steps.

  

  

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

import numpy as np

 

# here inside arrange method we

# provide start, end, step as

# arguments.

arr_b = np.arange(20, 30, 2)

 

# step argument helps in printing 

# every said step and skipping the 

# rest.

print(arr_b)  
  
---  
  
 __

 __

 **Output:**

    
    
    [20 22 24 26 28]

Indexing these arrays is simple. Every array element has a particular index
associated with them. Indexing starts at 0 and goes on till the length of
array-1. In the previous example, arr_b has 5 elements within itself.
Accessing these elements can be done with:

    
    
    array_name[index_number]

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

import numpy as np

 

# here inside arrange method we

# provide start, end, step as

# arguments.

arr_b = np.arange(20, 30, 2)

 

# step argument helps in printing 

# every said step and skipping the 

# rest.

print(arr_b)

 

 

print(arr_b[2])

 

# Slicing operation from index 

# 1 to 3 

print(arr_b[1:4])  
  
---  
  
 __

 __

 **Output**

    
    
    [20 22 24 26 28]
    24
    [22 24 26]

For **Multidimensional array** you can use **reshape()** method along with
**arange()**

 __

 __  
 __

 __

 __  
 __  
 __

import numpy as np

 

arr_m = np.arange(12).reshape(6, 2)

print(arr_m)  
  
---  
  
 __

 __

 **Output:**

    
    
    [[ 0  1]
     [ 2  3]
     [ 4  5]
     [ 6  7]
     [ 8  9]
     [10 11]]

Inside **reshape()** the parameters should be the multiple of the **arange()**
parameter. In our previous example, we had 6 rows and 2 columns. You can
specify another parameter whereby you define the dimension of the array. By
default, it is an 2d array.

  

  

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

import numpy as np

 

arr_m = np.arange(12).reshape(2, 2, 3)

print(arr_m)  
  
---  
  
 __

 __

 **Output**

    
    
    [[[ 0  1  2]
      [ 3  4  5]]
    
     [[ 6  7  8]
      [ 9 10 11]]]

To index a multi-dimensional array you can index with slicing operation
similar to a single dimension array.

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

import numpy as np

 

arr_m = np.arange(12).reshape(2, 2, 3)

 

# Indexing

print(arr_m[0:3])

print()

print(arr_m[1:5:2,::3])  
  
---  
  
 __

 __

 **Output:**

    
    
    [[[ 0  1  2]
      [ 3  4  5]]
    
     [[ 6  7  8]
      [ 9 10 11]]]
    
    [[[6 7 8]]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

