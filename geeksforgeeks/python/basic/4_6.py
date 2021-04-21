Adding and Subtracting Matrices in Python



In this article, we will discuss how to add and subtract elements of the
matrix in Python.

**Example:**

    
    
    Suppose we have two matrices A and B.
    A = [[1,2],[3,4]]
    B = [[4,5],[6,7]]
    
    then we get
    A+B = [[5,7],[9,11]]
    A-B = [[-3,-3],[-3,-3]]
    
    

Now let us try to implement this using Python

**1\. Adding elements of the matrix**

In the above code, we have used np.add() method to add elements of two
matrices. If shape of two arrays are not same, that is arr1.shape !=
arr2.shape, they must be broadcastable to a common shape (which may be the
shape of one or the other).

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing numpy as np

import numpy as np

 

 

# creating first matrix

A = np.array([[1, 2], [3, 4]])

 

# creating second matrix

B = np.array([[4, 5], [6, 7]])

 

print("Printing elements of first matrix")

print(A)

print("Printing elements of second matrix")

print(B)

 

# adding two matrix

print("Addition of two matrix")

print(np.add(A, B))  
  
---  
  
 __

 __

 **Output:**

    
    
    Printing elements of first matrix
    [[1 2]
     [3 4]]
    Printing elements of second matrix
    [[4 5]
     [6 7]]
    Addition of two matrix
    [[ 5  7]
     [ 9 11]]

 **2\. Subtracting elements of matrices**

In the above code, we have used np.subtract() to subtract elements of two
matrices. It returns the difference of arr1 and arr2, element-wise.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing numpy as np

import numpy as np

 

 

# creating first matrix

A = np.array([[1, 2], [3, 4]])

 

# creating second matrix

B = np.array([[4, 5], [6, 7]])

 

print("Printing elements of first matrix")

print(A)

print("Printing elements of second matrix")

print(B)

 

# subtracting two matrix

print("Subtraction of two matrix")

print(np.subtract(A, B))  
  
---  
  
 __

 __

 **Output:**

    
    
    Printing elements of first matrix
    [[1 2]
     [3 4]]
    Printing elements of second matrix
    [[4 5]
     [6 7]]
    Subtraction of two matrix
    [[-3 -3]
     [-3 -3]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

