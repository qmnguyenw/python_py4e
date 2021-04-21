Multiplication of two Matrices in Single line using Numpy in Python



Matrix multiplication is an operation that takes two matrices as input and
produces single matrix by multiplying rows of the first matrix to the column
of the second matrix.In matrix multiplication make sure that the number of
rows of the first matrix should be equal to the number of columns of the
second matrix.  
 **Example:** Multiplication of two matrices by each other of size 3×3.

    
    
    Input:matrix1 = ([1, 2, 3],
                     [3, 4, 5],
                     [7, 6, 4])
          matrix2 = ([5, 2, 6],
                     [5, 6, 7],
                     [7, 6, 4])
    
    Output : [[36 32 32]
              [70 60 66]
              [93 74 100]]
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

Methods to multiply two matrices in python  
1. **Using explicit for loops:** This is a simple technique to multiply matrices but one of the expensive method for larger input data set.In this, we use nested **for** loops to iterate each row and each column.  
If matrix1 is a **n x m** matrix and matrix2 is a **m x l** matrix.

 __

 __  
 __

 __

 __  
 __  
 __

# input two matrices of size n x m

matrix1 = [[12,7,3],

 [4 ,5,6],

 [7 ,8,9]]

matrix2 = [[5,8,1],

 [6,7,3],

 [4,5,9]]

 

res = [[0 for x in range(3)] for y in
range(3)] 

 

# explicit for loops

for i in range(len(matrix1)):

 for j in range(len(matrix2[0])):

 for k in range(len(matrix2)):

 

 # resulted matrix

 res[i][j] += matrix1[i][k] * matrix2[k][j]

 

print (res)  
  
---  
  
 __

 __

Output:

    
    
    [[114 160  60]
     [ 74  97  73]
     [119 157 112]]
    

In this program, we have used nested for loops for computation of result which
will iterate through each row and column of the matrices, at last it will
accumulate the sum of product in the result.  
2\. **Using Numpy :** Multiplication using Numpy also know as vectorization
which main aim to reduce or remove the explicit use of for loops in the
program by which computation becomes faster.  
Numpy is a build in a package in python for array-processing and
manipulation.For larger matrix operations we use numpy python package which is
1000 times faster than iterative one method.  
For detail about Numpy please visit the Link

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# We need install numpy in order to import it

import numpy as np

 

# input two matrices

mat1 = ([1, 6, 5],[3 ,4, 8],[2, 12,
3])

mat2 = ([3, 4, 6],[5, 6, 7],[6,56,
7])

 

# This will return dot product

res = np.dot(mat1,mat2)

 

 

# print resulted matrix

print(res)  
  
---  
  
 __

 __

Output:

    
    
    [[ 63 320  83]
     [ 77 484 102]
     [ 84 248 117]]
    

**Usingnumpy**

 __

 __  
 __

 __

 __  
 __  
 __

# same result will be obtained when we use @ operator

# as shown below(only in python >3.5)

import numpy as np

 

# input two matrices

mat1 = ([1, 6, 5],[3 ,4, 8],[2, 12,
3])

mat2 = ([3, 4, 6],[5, 6, 7],[6,56,
7])

 

# This will return matrix product of two array

res = mat1 @ mat2

 

# print resulted matrix

print(res)  
  
---  
  
 __

 __

Output:

    
    
    [[ 63 320  83]
     [ 77 484 102]
     [ 84 248 117]]
    

In the above example we have used dot product and in mathematics the dot
product is an algebraic operation that takes two vectors of equal size and
returns a single number. The result is calculated by multiplying corresponding
entries and adding up those products.

This article is contributed by **Dheeraj Sharma**. If you like GeeksforGeeks
and would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

