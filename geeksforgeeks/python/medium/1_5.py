Sparse Matrix in Python using Dictionary



A sparse matrix is a matrix in which most of the elements have zero value and
thus efficient ways of storing such matrices are required. Sparse matrices are
generally utilized in applied machine learning such as in data containing
data-encodings that map categories to count and also in entire subfields of
machine learning such as natural language processing (NLP).

 **Examples:**

    
    
    0 0 0 1 0            
    2 0 0 0 3
    0 0 0 4 0
    
    Above is spare matrix with only 4 non-zero elements.

Representing a sparse matrix by a 2D array leads to wastage of lots of memory
as zeroes in the matrix are of no use in most cases. So, instead of storing
zeroes with non-zero elements, we only store non-zero elements. These
efficient ways require only the non-zero values to be stored along with their
index so that the original matrix can be retrieved when required. One such
efficient way in Python is the use of a dictionary. Dictionary in Python
stores data in key-value pairs like maps in Java. Dictionary stores data in an
unordered manner.

### Approach:

  * First, we take a sparse matrix and create an empty dictionary.
  * Then we iterate through all the elements of the matrix and check if they are zero or non-zero elements.
  * The non-zero elements are added to the dictionary with their index as the key and their data as the value in the key-value pairs of the dictionary.
  * Finally, we can print the dictionary giving each element with its index.

Below is the Implementation.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# creating sparse matrix

arr = [[0, 0, 0, 1, 0],

 [2, 0, 0, 0, 3],

 [0, 0, 0, 4, 0]]

 

# creating empty dictionary

dic = {}

 

# iterating through the matrix

for i in range(len(arr)):

 for j in range(len(arr[i])):

 if arr[i][j] != 0:

 

 # adding non zero elements to

 # the dictionary

 dic[i, j] = arr[i][j]

 

print("Position of non-zero elements in the matrix:")

print(dic)  
  
---  
  
 __

 __

 **Output:**

  

  

> The following dictionary shows the positional of non-zero elements in the
> sparse matrix
>
> {(0, 3): 1, (1, 0): 2, (1, 4): 3, (2, 3): 4}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

