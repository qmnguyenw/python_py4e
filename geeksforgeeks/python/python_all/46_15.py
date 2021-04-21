How to Create a Sparse Matrix in Python



If most of the elements of the matrix have **0 value** , then it is called a
sparse matrix. The two major benefits of using sparse matrix instead of a
simple matrix are:

  *  **Storage:** There are lesser non-zero elements than zeros and thus lesser memory can be used to store only those elements.
  *  **Computing time:** Computing time can be saved by logically designing a data structure traversing only non-zero elements.

Sparse matrices are generally utilized in applied machine learning such as in
data containing data-encodings that map categories to count and also in entire
subfields of machine learning such as natural language processing (NLP).

 **Example:**

    
    
    0 0 3 0 4            
    0 0 5 7 0
    0 0 0 0 0
    0 2 6 0 0

Representing a sparse matrix by a 2D array leads to wastage of lots of memory
as zeroes in the matrix are of no use in most of the cases. So, instead of
storing zeroes with non-zero elements, we only store non-zero elements. This
means storing non-zero elements with **triples- (Row, Column, value).**

### Create a Sparse Matrix in Python

Python’s **SciPy** gives tools for creating sparse matrices using multiple
data structures, as well as tools for converting a dense matrix to a sparse
matrix. The function **csr_matrix()** is used to create a sparse matrix of
compressed sparse row format whereas **csc_matrix()** is used to create a
sparse matrix of compressed sparse column format.

  

  

####  **# Using** **csr_matrix()**

>  **Syntax:**
>
>  **scipy.sparse.csr_matrix** **(** _shape=None_ **,** _dtype=None_ **)**
>
> **Parameters:**
>
>  **shape:** Get shape of a matrix
>
>  **dtype:** Data type of the matrix

 **Example 1:**

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to create

# sparse matrix using csr_matrix()

 

# Import required package

import numpy as np

from scipy.sparse import csr_matrix

 

# Creating a 3 * 4 sparse matrix

sparseMatrix = csr_matrix((3, 4), 

 dtype = np.int8).toarray()

 

# Print the sparse matrix

print(sparseMatrix)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    [[0 0 0 0]
     [0 0 0 0]
     [0 0 0 0]]
    

**Example 2:**

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to create

# sparse matrix using csr_matrix()

 

# Import required package

import numpy as np

from scipy.sparse import csr_matrix

 

row = np.array([0, 0, 1, 1, 2, 1])

col = np.array([0, 1, 2, 0, 2, 2])

 

# taking data

data = np.array([1, 4, 5, 8, 9, 6])

 

# creating sparse matrix

sparseMatrix = csr_matrix((data, (row, col)), 

 shape = (3, 3)).toarray()

 

# print the sparse matrix

print(sparseMatrix)  
  
---  
  
 __

 __

 **Output:**

    
    
    [[ 1  4  0]
     [ 8  0 11]
     [ 0  0  9]]
    

#### **# Using** **csc_matrix()**

>  **Syntax:**
>
>  **scipy.sparse.csc_matrix** **(** _shape=None_ **,** _dtype=None_ **)**
>
> **Parameters:**
>
>  **shape:** Get shape of a matrix
>
>  **dtype:** Data type of the matrix

 **Example 1:**

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to create

# sparse matrix using csc_matrix()

 

# Import required package

import numpy as np

from scipy.sparse import csc_matrix

 

# Creating a 3 * 4 sparse matrix

sparseMatrix = csc_matrix((3, 4), 

 dtype = np.int8).toarray()

 

# Print the sparse matrix

print(sparseMatrix)  
  
---  
  
 __

 __

 **Output:**

    
    
    [[0 0 0 0]
     [0 0 0 0]
     [0 0 0 0]]
    

**Example 2:**

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to create

# sparse matrix using csc_matrix()

 

# Import required package

import numpy as np

from scipy.sparse import csc_matrix

 

row = np.array([0, 0, 1, 1, 2, 1])

col = np.array([0, 1, 2, 0, 2, 2])

 

# taking data

data = np.array([1, 4, 5, 8, 9, 6])

 

# creating sparse matrix

sparseMatrix = csc_matrix((data, (row, col)),

 shape = (3, 3)).toarray()

 

# print the sparse matrix

print(sparseMatrix)  
  
---  
  
 __

 __

 **Output:**

    
    
    [[ 1  4  0]
     [ 8  0 11]
     [ 0  0  9]]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

