Transpose a matrix in Single line in Python



Transpose of a matrix is a task we all can perform very easily in python
(Using a nested loop). But there are some interesting ways to do the same in a
single line.  
In Python, we can implement a matrix as nested list (list inside a list). Each
element is treated as a row of the matrix. For example m = [[1, 2], [4, 5],
[3, 6]] represents a matrix of 3 rows and 2 columns.  
First element of the list – **m[0]** and element in first row, first column –
**m[0][0]**.

  1.  **Using Nested List Comprehension:** Nested list comprehension are used to iterate through each element in the matrix.In the given example ,we iterate through each element of matrix (m) in column major manner and assign the result to rez matrix which is the transpose of m.

 __

 __  
 __

 __

 __  
 __  
 __

m= [[1,2],[3,4],[5,6]]

for row in m :

 print(row)

rez = [[m[j][i] for j in range(len(m))] for i in
range(len(m[0]))]

print("\n")

for row in rez:

 print(row)  
  
---  
  
 __

 __

 **Output:**

    
    
    [1, 2]
    [3, 4]
    [5, 6]
    
    
    [1, 3, 5]
    [2, 4, 6]
    

  2. **Using zip:** Zip returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables. In this example we unzip our array using * and then zip it to get the transpose.

 __

 __  
 __

 __

 __  
 __  
 __

matrix=[(1,2,3),(4,5,6),(7,8,9),(10,11,12)]

for row in matrix:

 print(row)

print("\n")

t_matrix = zip(*matrix)

for row in t_matrix:

 print(row)  
  
---  
  
 __

 __

 **Output:**

    
    
    (1, 2, 3)
    (4, 5, 6)
    (7, 8, 9)
    (10, 11, 12)
    
    (1, 4, 7, 10)
    (2, 5, 8, 11)
    (3, 6, 9, 12)
    

Note :- If you want your result in the form [[1,4,7,10][2,5,8,11][3,6,9,12]] ,
you can use t_matrix=map(list, zip(*matrix)).

  3.  **Using numpy:** NumPy is a general-purpose array-processing package designed to efficiently manipulate large multi-dimensional arrays. The transpose method returns a transposed view of the passed multi-dimensional matrix.

 __

 __  
 __

 __

 __  
 __  
 __

# You need to install numpy in order to import it

# Numpy transpose returns similar result when 

# applied on 1D matrix

import numpy 

matrix=[[1,2,3],[4,5,6]]

print(matrix)

print("\n")

print(numpy.transpose(matrix))  
  
---  
  
 __

 __

Or, simply using “.T” after the variable

 __

 __  
 __

 __

 __  
 __  
 __

# You need to install numpy in order to import it

import numpy as np

matrix = np.array([[1,2,3],[4,5,6]])

print(matrix)

print("\n")

print(matrix.T)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    [[1 2 3]
     [4 5 6]]
    
    [[1 4]
     [2 5]
     [3 6]]
    

Note :- “.T” only works on numpy arrays

This article is contributed by **Mayank Rawat** & simply modified by **Md.
Tahmid Hasan**. If you like GeeksforGeeks and would like to contribute, you
can also write an article using contribute.geeksforgeeks.org or mail your
article to contribute@geeksforgeeks.org. See your article appearing on the
GeeksforGeeks main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

