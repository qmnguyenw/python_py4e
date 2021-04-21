How to inverse a matrix using NumPy



The inverse of a matrix is just a reciprocal of the matrix as we do in normal
arithmetic for a single number which is used to solve the equations to find
the value of unknown variables. The inverse of a matrix is that matrix which
when multiplied with the original matrix will give as an identity matrix. The
inverse of a matrix exists only if the matrix is **non-singular i.e.,
determinant should not be 0**. Using determinant and adjoint, we can easily
find the inverse of a square matrix using below formula,

    
    
    if det(A) != 0
        A-1 = adj(A)/det(A)
    else
        "Inverse doesn't exist"  

#### Matrix Equation

![=>Ax = B\\\\ =>A^{-1}Ax = A^{-1}B\\\\ =>x =
A^{-1}B](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-07b1d3a0d767eb4e3739cfe180108bce_l3.png)

>  **where,**
>
>  **A -1:** The inverse of matrix A
>
>  **x:** T _he unknown variable column_
>
>  
>
>
>  
>
>
>  _ **B:** The solution matrix_

#### Inverse of a Matrix using NumPy

Python provides a very easy method to calculate the inverse of a matrix. The
function **numpy.linalg.inv()** which is available in the python NumPy module
is used to compute the inverse of a matrix.

> **Syntax:**
>
>  **numpy.linalg.inv** **(** _a_ **)**
>
>  **Parameters:**
>
>  **a:** Matrix to be inverted
>
>  **Returns:**
>
> Inverse of the matrix _a_.
>
>  
>
>
>  
>

 **Example 1:**

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to inverse

# a matrix using numpy

 

# Import required package

import numpy as np

 

# Taking a 3 * 3 matrix

A = np.array([[6, 1, 1],

 [4, -2, 5],

 [2, 8, 7]])

 

# Calculating the inverse of the matrix

print(np.linalg.inv(A))  
  
---  
  
 __

 __

 **Output:**

    
    
    [[ 0.17647059 -0.00326797 -0.02287582]
     [ 0.05882353 -0.13071895  0.08496732]
     [-0.11764706  0.1503268   0.05228758]]

 **Example 2:**

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to inverse

# a matrix using numpy

 

# Import required package

import numpy as np

 

# Taking a 4 * 4 matrix

A = np.array([[6, 1, 1, 3],

 [4, -2, 5, 1],

 [2, 8, 7, 6],

 [3, 1, 9, 7]])

 

# Calculating the inverse of the matrix

print(np.linalg.inv(A))  
  
---  
  
 __

 __

 **Output:**

    
    
    [[ 0.13368984  0.10695187  0.02139037 -0.09090909]
     [-0.00229183  0.02673797  0.14820474 -0.12987013]
     [-0.12987013  0.18181818  0.06493506 -0.02597403]
     [ 0.11000764 -0.28342246 -0.11382735  0.23376623]]
    

**Example 3:**

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to inverse

# a matrix using numpy

 

# Import required package

import numpy as np

 

# Inverses of several matrices can

# be computed at once

A = np.array([[[1., 2.], [3., 4.]],

 [[1, 3], [3, 5]]])

 

# Calculating the inverse of the matrix

print(np.linalg.inv(A))  
  
---  
  
 __

 __

 **Output:**

    
    
    [[[-2.    1.  ]
      [ 1.5  -0.5 ]]
    
     [[-1.25  0.75]
      [ 0.75 -0.25]]]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

