Take Matrix input from user in Python



Matrix is nothing but a rectangular arrangement of data or numbers. In other
words, it is a rectangular array of data or numbers. The horizontal entries in
a matrix are called as ‘rows’ while the vertical entries are called as
‘columns’. If a matrix has r number of rows and c number of columns then the
order of matrix is given by **r x c**. Each entries in a matrix can be integer
values, or floating values, or even it can be complex numbers.

 **Examples:**

    
    
     **// 3 x 4 matrix**
         1 2 3 4
    M =  4 5 6 7
         6 7 8 9
    
    **// 2 x 3 matrix in Python**
    A = ( [ 2, 5, 7 ],
          [ 4, 7, 9 ] )
    
    **// 3 x 4 matrix in Python where entries are floating numbers**
    B = ( [ 1.0, 3.5, 5.4, 7.9 ],
          [ 9.0, 2.5, 4.2, 3.6 ],
          [ 1.5, 3.2, 1.6, 6.5 ] )

In Python, we can take a user input matrix in different ways. Some of the
methods for user input matrix in Python are shown below:

 **Code #1:**

 __

 __  
 __

 __

 __  
 __  
 __

# A basic code for matrix input from user

 

R = int(input("Enter the number of rows:"))

C = int(input("Enter the number of columns:"))

 

# Initialize matrix

matrix = []

print("Enter the entries rowwise:")

 

# For user input

for i in range(R): # A for loop for row entries

 a =[]

 for j in range(C): # A for loop for column entries

 a.append(int(input()))

 matrix.append(a)

 

# For printing the matrix

for i in range(R):

 for j in range(C):

 print(matrix[i][j], end = " ")

 print()  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    Enter the number of rows:2
    Enter the number of columns:3
    Enter the entries rowwise:
    1
    2
    3
    4
    5
    6
    
    1 2 3 
    4 5 6 
    

One liner:

 __

 __  
 __

 __

 __  
 __  
 __

# one-liner logic to take input for rows and columns

mat = [[int(input()) for x in range (C)] for y
in range(R)]  
  
---  
  
 __

 __

  
**Code #2:** Using map() function and Numpy.

In Python, there exists a popular library called _**NumPy**_. This library is
a fundamental library for any scientific computation. It is also used for
multidimensional arrays and as we know matrix is a rectangular array, we will
use this library for user input matrix.

 __

 __  
 __

 __

 __  
 __  
 __

import numpy as np

 

R = int(input("Enter the number of rows:"))

C = int(input("Enter the number of columns:"))

 

 

print("Enter the entries in a single line (separated by space): ")

 

# User input of entries in a 

# single line separated by space

entries = list(map(int, input().split()))

 

# For printing the matrix

matrix = np.array(entries).reshape(R, C)

print(matrix)  
  
---  
  
 __

 __

 **Output:**

    
    
    Enter the number of rows:2
    Enter the number of columns:2
    Enter the entries in a single line separated by space: 1 2 3 1 
    [[1 2]
     [3 1]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

