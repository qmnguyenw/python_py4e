Python program to multiply two matrices



Given two matrix the task is that we will have to create a program to multiply
two matrices in python.

Examples:

    
    
    Input : X = [[1, 7, 3],
                 [3, 5, 6],
                 [6, 8, 9]]
           Y = [[1, 1, 1, 2],
               [6, 7, 3, 0],
               [4, 5, 9, 1]]
     
    Output : [55, 65, 49, 5]
             [57, 68, 72, 12]
             [90, 107, 111, 21]
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Using Simple Nested Loops**  
In this program we have to use nested for loops to iterate through each row
and each column.

 __

 __  
 __

 __

 __  
 __  
 __

# Program to multiply two matrices using nested loops

 

# take a 3x3 matrix

A = [[12, 7, 3],

 [4, 5, 6],

 [7, 8, 9]]

 

# take a 3x4 matrix 

B = [[5, 8, 1, 2],

 [6, 7, 3, 0],

 [4, 5, 9, 1]]

 

result = [[0, 0, 0, 0],

 [0, 0, 0, 0],

 [0, 0, 0, 0]]

 

# iterating by row of A

for i in range(len(A)):

 

 # iterating by coloum by B 

 for j in range(len(B[0])):

 

 # iterating by rows of B

 for k in range(len(B)):

 result[i][j] += A[i][k] * B[k][j]

 

for r in result:

 print(r)  
  
---  
  
 __

 __

Output:

    
    
    [114, 160, 60, 27]
    [74, 97, 73, 14]
    [119, 157, 112, 23]
    

**Method 2:** Matrix Multiplication Using Nested List. We use zip in Python.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Program to multiply two matrices using list comprehension

 

# take a 3x3 matrix

A = [[12, 7, 3],

 [4, 5, 6],

 [7, 8, 9]]

 

# take a 3x4 matrix

B = [[5, 8, 1, 2],

 [6, 7, 3, 0],

 [4, 5, 9, 1]]

 

# result will be 3x4

result = [[sum(a * b for a, b in zip(A_row, B_col)) 

 for B_col in zip(*B)]

 for A_row in A]

 

for r in result:

 print(r)  
  
---  
  
 __

 __

Output:

    
    
    [114, 160, 60, 27]
    [74, 97, 73, 14]
    [119, 157, 112, 23]
    
    

**Method 3:** Matrix Multiplication (Vectorized implementation).

 __

 __  
 __

 __

 __  
 __  
 __

# Program to multiply two matrices (vectorized implementation)

 

# Program to multiply two matrices (vectorized implementation)

import numpy as np

# take a 3x3 matrix

A = [[12, 7, 3],

 [4, 5, 6],

 [7, 8, 9]]

 

# take a 3x4 matrix

B = [[5, 8, 1, 2],

 [6, 7, 3, 0],

 [4, 5, 9, 1]]

 

# result will be 3x4

 

result= [[0,0,0,0],

 [0,0,0,0],

 [0,0,0,0]]

 

result = np.dot(A,B)

 

for r in result:

 print(r)  
  
---  
  
 __

 __

Output:

    
    
    [114, 160, 60, 27]
    [74, 97, 73, 14]
    [119, 157, 112, 23]
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

