Calculate the Euclidean distance using NumPy



In simple terms, Euclidean distance is the shortest between the 2 points
irrespective of the dimensions. In this article to find the Euclidean
distance, we will use the NumPy library. This library used for manipulating
multidimensional array in a very efficient way. Let’s discuss a few ways to
find Euclidean distance by NumPy library.

 **Method #1: Using linalg.norm()**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to find Euclidean distance

# using linalg.norm()

 

import numpy as np

 

# intializing points in

# numpy arrays

point1 = np.array((1, 2, 3))

point2 = np.array((1, 1, 1))

 

# calculating Euclidean distance

# using linalg.norm()

dist = np.linalg.norm(point1 - point2)

 

# printing Euclidean distance

print(dist)  
  
---  
  
 __

 __

 **Output:**

    
    
    2.23606797749979

 **Method #2: Using dot()**

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to find Euclidean distance

# using dot()

 

import numpy as np

 

# intializing points in

# numpy arrays

point1 = np.array((1, 2, 3))

point2 = np.array((1, 1, 1))

 

# subtracting vector

temp = point1 - point2

 

# doing dot product

# for finding

# sum of the squares

sum_sq = np.dot(temp.T, temp)

 

# Doing squareroot and

# printing Euclidean distance

print(np.sqrt(sum_sq))  
  
---  
  
 __

 __

 **Output:**

    
    
    2.23606797749979

 **Method #3: Using square() and sum()**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to find Euclidean distance

# using sum() and square()

 

import numpy as np

 

# intializing points in

# numpy arrays

point1 = np.array((1, 2, 3))

point2 = np.array((1, 1, 1))

 

# finding sum of squares

sum_sq = np.sum(np.square(point1 - point2))

 

# Doing squareroot and

# printing Euclidean distance

print(np.sqrt(sum_sq))  
  
---  
  
 __

 __

 **Output:**

    
    
    2.23606797749979

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

