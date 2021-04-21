Python Lists VS Numpy Arrays



 **NumPy** is the fundamental package for scientific computing in Python.
NumPy arrays facilitate advanced mathematical and other types of operations on
large numbers of data. Typically, such operations are executed more
efficiently and with less code than is possible using Python’s built-in
sequences. NumPy is not another programming language but a Python extension
module. It provides fast and efficient operations on arrays of homogeneous
data.

 **Some important points about Numpy arrays:**

  * We can create a N-dimensional array in python using numpy.array().
  * Array are by default Homogeneous, which means data inside an array must be of the same Datatype. (Note you can also create a structured array in python).
  * Element wise operation is possible.
  * Numpy array has the various function, methods, and variables, to ease our task of matrix computation.
  * Elements of an array are stored contiguously in memory. For example, all rows of a two dimensioned array must have the same number of columns. Or a three dimensioned array must have the same number of rows and columns on each card.

 **Representation of Numpy array:**

  * Single Dimensional Numpy Array;

 __

 __  
 __

 __

 __  
 __  
 __

import numpy as np

 

a = np.array([1, 2, 3])

print(a)  
  
---  
  
 __

 __

 **Output:**

    
    
    [1 2 3]
    

  * Multi-dimensional Numpy Array:

 __

 __  
 __

 __

 __  
 __  
 __

import numpy as np

 

a = np.array([(1, 2, 3), (4, 5, 6)])

print(a)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    [[1 2 3]
     [4 5 6]]
    

