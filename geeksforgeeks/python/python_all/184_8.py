Python Program to find transpose of a matrix



Transpose of a matrix is obtained by changing rows to columns and columns to
rows. In other words, transpose of A[][] is obtained by changing A[i][j] to
A[j][i].

![matrix-transpose](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/matrix-transpose.jpg)

 **For Square Matrix :**

The below program finds transpose of A[][] and stores the result in B[][], we
can change N for different dimension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 Program to find

# transpose of a matrix

 

N = 4

 

# This function stores

# transpose of A[][] in B[][]

 

def transpose(A,B):

 

 for i in range(N):

 for j in range(N):

 B[i][j] = A[j][i]

 

# driver code

A = [ [1, 1, 1, 1],

 [2, 2, 2, 2],

 [3, 3, 3, 3],

 [4, 4, 4, 4]]

 

 

B = A[:][:] # To store result

 

transpose(A, B)

 

print("Result matrix is")

for i in range(N):

 for j in range(N):

 print(B[i][j], " ", end='')

 print()

 

# This code is contributed by Anant Agarwal.  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    Result matrix is
    1  2  3  4  
    2  2  3  4  
    3  3  3  4  
    4  4  4  4
    

