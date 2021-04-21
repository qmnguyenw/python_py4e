Python program to Convert a Matrix to Sparse Matrix



Given a matrix with most of its elements as 0, we need to convert this matrix
into a sparse matrix in Python.

 **Example:**

>  **Input:** Matrix:  
> 1 0 0 0  
> 0 2 0 0  
> 0 0 3 0  
> 0 0 0 4  
> 5 0 0 0
>
>  **Output:** Sparse Matrix:  
> 0 0 1  
> 1 1 2  
> 2 2 3  
> 3 3 4  
> 4 0 5
>
>  **Explanation:**  
>  Here the Matrix is represented using a 2D list and the Sparse Matrix is
> represented in the form **Row Column Value**
>
>  
>
>
>  
>
>
> In the Sparse Matrix the first row is 0 1 1 indicates that the value of
> the Matrix at row 0 and column 1 is 1.

 **Approach:**

  1. Create an empty list which will represent the sparse matrix list.
  2. Iterate through the 2D matrix to find non zero elements.
  3. If an element is non zero, create a temporary empty list.
  4. Append the row value, column value, and the non zero element itself into the temporary list.
  5. Now append the temporary list into the sparse matrix list such that the temporary list acts as a sub-list of the sparse matrix list.
  6. After getting all the non zero elements from the matrix, display the sparse matrix.

The above approach has been used in convertToSparseMatrix() function in the
below program:

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to convert a

# matrix to sparse matrix

 

 

# function display a matrix

def displayMatrix(matrix):

 

 for row in matrix:

 for element in row:

 print(element, end =" ")

 print()

 

# function to convert the matrix 

# into a sparse matrix

def convertToSparseMatrix(matrix):

 

 # creating an empty sparse 

 # matrix list

 sparseMatrix =[]

 

 # searching values greater 

 # than zero

 for i in range(len(matrix)):

 for j in range(len(matrix[0])):

 if matrix[i][j] != 0 :

 

 # creating a temporaray

 # sublist

 temp = []

 

 # appending row value, column 

 # value and element into the 

 # sublist 

 temp.append(i)

 temp.append(j)

 temp.append(matrix[i][j])

 

 # appending the sublist into

 # the sparse matrix list

 sparseMatrix.append(temp)

 

 # displaying the sparse matrix

 print("\nSparse Matrix: ") 

 displayMatrix(sparseMatrix) 

 

# Driver's code

# initializing a normal matrix

normalMatrix =[[1, 0, 0, 0], 

 [0, 2, 0, 0], 

 [0, 0, 3, 0], 

 [0, 0, 0, 4], 

 [5, 0, 0, 0]] 

 

# displaying the matrix

displayMatrix(normalMatrix)

 

# converting the matrix to sparse 

# displayMatrix 

convertToSparseMatrix(normalMatrix)   
  
---  
  
__

__

**Output:**

    
    
    0 1 0 0 
    0 0 2 0 
    0 3 0 0 
    0 0 5 0 
    0 0 0 4 
    
    Sparse Matrix: 
    0 0 1 
    1 1 2 
    2 2 3 
    3 3 4 
    4 0 5 
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

