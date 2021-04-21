NumPy in Python | Set 2 (Advanced)



NumPy in Python | Set 1 (Introduction)

This article discusses some more and a bit advanced methods available in
NumPy.

  1.  **Stacking:** Several arrays can be stacked together along different axes.
    *  **np.vstack:** To stack arrays along vertical axis.
    *  **np.hstack:** To stack arrays along horizontal axis.
    *  **np.column_stack:** To stack 1-D arrays as columns into 2-D arrays.
    *  **np.concatenate:** To stack arrays along specified axis (axis is passed as argument).

 __

 __  
 __

 __

 __  
 __  
 __

import numpy as np

 

a = np.array([[1, 2],

 [3, 4]])

 

b = np.array([[5, 6],

 [7, 8]])

 

# vertical stacking

print("Vertical stacking:\n", np.vstack((a, b)))

 

# horizontal stacking

print("\nHorizontal stacking:\n", np.hstack((a, b)))

 

c = [5, 6]

 

# stacking columns

print("\nColumn stacking:\n", np.column_stack((a, c)))

 

# concatenation method 

print("\nConcatenating to 2nd axis:\n", np.concatenate((a, b), 1))  
  
---  
  
 __

 __

Output:

    
        Vertical stacking:
     [[1 2]
     [3 4]
     [5 6]
     [7 8]]
    
    Horizontal stacking:
     [[1 2 5 6]
     [3 4 7 8]]
    
    Column stacking:
     [[1 2 5]
     [3 4 6]]
    
    Concatenating to 2nd axis:
     [[1 2 5 6]
     [3 4 7 8]]

  2.  **Splitting:** For splitting, we have these functions:
    *  **np.hsplit:** Split array along horizontal axis.
    *  **np.vsplit:** Split array along vertical axis.
    *  **np.array_split:** Split array along specified axis.

 __

 __  
 __

 __

 __  
 __  
 __

import numpy as np

 

a = np.array([[1, 3, 5, 7, 9, 11],

 [2, 4, 6, 8, 10, 12]])

 

# horizontal splitting

print("Splitting along horizontal axis into 2 parts:\n", np.hsplit(a,
2))

 

# vertical splitting

print("\nSplitting along vertical axis into 2 parts:\n", np.vsplit(a,
2))  
  
---  
  
 __

 __

Output:

    
        Splitting along horizontal axis into 2 parts:
     [array([[1, 3, 5],
           [2, 4, 6]]), array([[ 7,  9, 11],
           [ 8, 10, 12]])]
    
    Splitting along vertical axis into 2 parts:
     [array([[ 1,  3,  5,  7,  9, 11]]), array([[ 2,  4,  6,  8, 10, 12]])]

  3.  **Broadcasting:** The term broadcasting describes how NumPy treats arrays with different shapes during arithmetic operations. Subject to certain constraints, the smaller array is “broadcast” across the larger array so that they have compatible shapes.

Broadcasting provides a means of vectorizing array operations so that looping
occurs in C instead of Python. It does this without making needless copies of
data and usually leads to efficient algorithm implementations. There are also
cases where broadcasting is a bad idea because it leads to inefficient use of
memory that slows computation.

  

  

NumPy operations are usually done element-by-element which requires two arrays
to have exactly the same shape. Numpy’s broadcasting rule relaxes this
constraint when the arrays’ shapes meet certain constraints.

 **The Broadcasting Rule:** In order to broadcast, the size of the trailing
axes for both arrays in an operation must either be the same size or one of
them must be **one**.

Let us see some examples:

    
        A(2-D array): 4 x 3
    B(1-D array):     3
    Result      : 4 x 3
    
    
        A(4-D array): 7 x 1 x 6 x 1
    B(3-D array):     3 x 1 x 5
    Result      : 7 x 3 x 6 x 5
    

But this would be a mismatch:

    
        A: 4 x 3
    B:     4
    

The simplest broadcasting example occurs when an array and a scalar value are
combined in an operation.  
Consider the example given below:

 __

 __  
 __

 __

 __  
 __  
 __

import numpy as np

 

a = np.array([1.0, 2.0, 3.0])

 

# Example 1

b = 2.0

print(a * b)

 

# Example 2

c = [2.0, 2.0, 2.0]

print(a * c)  
  
---  
  
 __

 __

Output:

    
        [ 2.  4.  6.]
    [ 2.  4.  6.]

We can think of the scalar b being stretched during the arithmetic operation
into an array with the same shape as a. The new elements in b, as shown in
above figure, are simply copies of the original scalar. Although, the
stretching analogy is only conceptual.  
Numpy is smart enough to use the original scalar value without actually making
copies so that broadcasting operations are as memory and computationally
efficient as possible. Because Example 1 moves less memory, (b is a scalar,
not an array) around during the multiplication, it is about 10% faster than
Example 2 using the standard numpy on Windows 2000 with one million element
arrays!  
The figure below makes the concept more clear:

![](https://media.geeksforgeeks.org/wp-content/uploads/numpy.png)

