Matrix manipulation in Python



In python matrix can be implemented as 2D list or 2D Array. Forming matrix
from latter, gives the additional functionalities for performing various
operations in matrix. These operations and array are defines in module “
**numpy** “.

 **Operation on Matrix :**

 **1\. add() :-** This function is used to perform **element wise matrix
addition**.

 **2\. subtract() :-** This function is used to perform **element wise matrix
subtraction**.

 **3\. divide() :-** This function is used to perform **element wise matrix
division**.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate matrix operations

# add(), subtract() and divide()

 

# importing numpy for matrix operations

import numpy

 

# initializing matrices

x = numpy.array([[1, 2], [4, 5]])

y = numpy.array([[7, 8], [9, 10]])

 

# using add() to add matrices

print ("The element wise addition of matrix is : ")

print (numpy.add(x,y))

 

# using subtract() to subtract matrices

print ("The element wise subtraction of matrix is : ")

print (numpy.subtract(x,y))

 

# using divide() to divide matrices

print ("The element wise division of matrix is : ")

print (numpy.divide(x,y))  
  
---  
  
 __

 __

Output :

    
    
    The element wise addition of matrix is : 
    [[ 8 10]
     [13 15]]
    The element wise subtraction of matrix is : 
    [[-6 -6]
     [-5 -5]]
    The element wise division of matrix is : 
    [[ 0.14285714  0.25      ]
     [ 0.44444444  0.5       ]]
    

**4\. multiply() :-** This function is used to perform **element wise matrix
multiplication**.

 **5\. dot() :-** This function is used to compute the **matrix
multiplication, rather than element wise multiplication**.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate matrix operations

# multiply() and dot()

 

# importing numpy for matrix operations

import numpy

 

# initializing matrices

x = numpy.array([[1, 2], [4, 5]])

y = numpy.array([[7, 8], [9, 10]])

 

# using multiply() to multiply matrices element wise

print ("The element wise multiplication of matrix is : ")

print (numpy.multiply(x,y))

 

# using dot() to multiply matrices

print ("The product of matrices is : ")

print (numpy.dot(x,y))  
  
---  
  
 __

 __

Output :

    
    
    The element wise multiplication of matrix is : 
    [[ 7 16]
     [36 50]]
    The product of matrices is : 
    [[25 28]
     [73 82]]
    

**6\. sqrt() :-** This function is used to compute the **square root of each
element** of matrix.

 **7\. sum(x,axis) :-** This function is used to **add all the elements in
matrix**. Optional “axis” argument computes the **column sum if axis is 0**
and **row sum if **axis** is 1**.

 **8\. “T” :-** This argument is used to **transpose** the specified matrix.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate matrix operations

# sqrt(), sum() and "T"

 

# importing numpy for matrix operations

import numpy

 

# initializing matrices

x = numpy.array([[1, 2], [4, 5]])

y = numpy.array([[7, 8], [9, 10]])

 

# using sqrt() to print the square root of matrix

print ("The element wise square root is : ")

print (numpy.sqrt(x))

 

# using sum() to print summation of all elements of matrix

print ("The summation of all matrix element is : ")

print (numpy.sum(y))

 

# using sum(axis=0) to print summation of all columns of matrix

print ("The column wise summation of all matrix is : ")

print (numpy.sum(y,axis=0))

 

# using sum(axis=1) to print summation of all columns of matrix

print ("The row wise summation of all matrix is : ")

print (numpy.sum(y,axis=1))

 

# using "T" to transpose the matrix

print ("The transpose of given matrix is : ")

print (x.T)  
  
---  
  
 __

 __

Output :

    
    
    The element wise square root is : 
    [[ 1.          1.41421356]
     [ 2.          2.23606798]]
    The summation of all matrix element is : 
    34
    The column wise summation of all matrix  is : 
    [16 18]
    The row wise summation of all matrix  is : 
    [15 19]
    The transpose of given matrix is : 
    [[1 4]
     [2 5]]
    

This article is contributed by **Manjeet Singh 100 🙂**. If you like
GeeksforGeeks and would like to contribute, you can also write an article
using contribute.geeksforgeeks.org or mail your article to
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

