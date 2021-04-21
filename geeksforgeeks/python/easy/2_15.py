How to create an empty matrix with NumPy in Python ?



The term **empty matrix** has no rows and no columns. A matrix that contains
missing values has at least one row and column, as does a matrix that contains
zeros. **Numerical Python (** **NumPy** **)** provides an abundance of useful
features and functions for operations on numeric arrays and matrices in
Python. If you want to create an empty matrix with the help of NumPy. We can
use a function:

  1.  **numpy.empty**
  2.  **numpy.zeros**

 **1.** **numpy.empty :** It Returns a new array of given shape and type,
without initializing entries.

>  **Syntax :** numpy.empty(shape, dtype=float, order=’C’)
>
>  **Parameters:**
>
>   * shape :int or tuple of int i.e shape of the array (5,6) or 5.
>   * dtype data-type, optional i.e desired output data-type for the array,
> e.g, numpy.int8. Default isnumpy.float64.
>   * order{‘C’, ‘F’}, optional, default: ‘C’ i.e whether to store multi-
> dimensional data in row-major (C-style) or column-major (Fortran-style)
> order in memory.
>

Let’s get started with empty function in NumPy considering an example that you
want to create a empty matrix 5 x 5

  

  

 **Example 1:** To create an empty matrix of 5 columns and 0 row :

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import numpy as np

 

 

x = np.empty((0, 5))

print('The value is :', x)

 

# if we check the matrix dimensions 

# using shape:

print('The shape of matrix is :', x.shape)

 

# by default the matrix type is float64

print('The type of matrix is :', x.dtype)  
  
---  
  
 __

 __

 **Output:**

    
    
    The value is : []
    The shape of matrix is : (0, 5)
    The type of matrix is : float64

Here, the matrix consists of 0 rows and 5 columns that’s why the result is ‘[
]’. Let’s take another example of empty function in NumPy considering a
example that you want to create a empty matrix 4 x 2 with some random numbers.

 **Example 2:** Initializing an empty array, using the expected
dimensions/size :

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import the library

import numpy as np

 

# Here 4 is the number of rows and 2 

# is the number of columns

y = np.empty((4, 2))

 

# print the matrix

print('The matrix is : \n', y)

 

# print the matrix consist of 25 random numbers

z = np.empty(25)

 

# print the matrix

print('The matrix with 25 random values:', z)  
  
---  
  
 __

 __

 **Output :**

> The matrix is :  
> [[1.41200958e-316 3.99539825e-306]  
> [3.38460865e+125 1.06264595e+248]  
> [1.33360465e+241 6.76067859e-311]  
> [1.80734135e+185 6.47273003e+170]]
>
>  
>
>
>  
>
>
> The matrix with 25 random values: [1.28430744e-316 8.00386346e-322
> 0.00000000e+000 0.00000000e+000  
> 0.00000000e+000 1.16095484e-028 5.28595592e-085 1.04316726e-076  
> 1.75300433e+243 3.15476290e+180 2.45128397e+198 9.25608172e+135  
> 4.73517493e-120 2.16209963e+233 3.99255547e+252 1.03819288e-028  
> 2.16209973e+233 7.35874688e+223 2.34783498e+251 4.52287158e+217  
> 8.78424170e+247 4.62381317e+252 1.47278596e+179 9.08367237e+223  
> 1.16466228e-028]

Here, we define the number of rows and columns so the matrix is filled with
random numbers.

 **2\. numpy.zeros :** It returns a new array of given shape and type, filled
with zeros.

>  **Syntax :** numpy.zeros(shape, dtype=float, order=’C’)
>
>  **Parameters:**
>
>   * shape : int or tuple of int i.e shape of the array (5,6) or 5.
>   * dtype data-type, optional i.e desired output data-type for the array,
> e.g, numpy.int8. Default is numpy.float64.
>   * order{‘C’, ‘F’}, optional, default: ‘C’ i.e whether to store multi-
> dimensional data in row-major (C-style) or column-major (Fortran-style)
> order in memory.
>

Let’s get started with zeros function in NumPy considering an example that you
want to create a matrix with zeros.

 **Example:** To create an zeros matrix of 7 columns and 5 rows :

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import numpy as np

x = np.zeros((7, 5))

 

# print the matrix

print('The matrix is : \n', x)

 

# check the type of matrix

x.dtype  
  
---  
  
 __

 __

 **Output :**

    
    
    The matrix is : 
     [[0. 0. 0. 0. 0.]
     [0. 0. 0. 0. 0.]
     [0. 0. 0. 0. 0.]
     [0. 0. 0. 0. 0.]
     [0. 0. 0. 0. 0.]
     [0. 0. 0. 0. 0.]
     [0. 0. 0. 0. 0.]]
    dtype('float64')

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

