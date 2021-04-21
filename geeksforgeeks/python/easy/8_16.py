Why is Numpy faster in Python?



NumPy is a Python fundamental package used for efficient manipulations and
operations on High-level mathematical functions, Multi-dimensional arrays,
Linear algebra, Fourier Transformations, Random Number Capabilities, etc. It
provides tools for integrating C, C++, and Fortran code in Python. NumPy is
mostly used in Python for scientific computing.  
Let us look at the below program which compares NumPy Arrays and Lists in
Python in terms of execution time.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing required packages

import numpy

import time

# size of arrays and lists

size = 1000000

# declaring lists

list1 = range(size)

list2 = range(size)

# declaring arrays

array1 = numpy.arange(size) 

array2 = numpy.arange(size)

# list

initialTime = time.time()

resultantList = [(a * b) for a, b in zip(list1, list2)]

# calculating execution time

print("Time taken by Lists :",

 (time.time() - initialTime),

 "seconds")

# NumPy array

initialTime = time.time()

resultantArray = array1 * array2

# calculating execution time

print("Time taken by NumPy Arrays :",

 (time.time() - initialTime),

 "seconds")  
  
---  
  
 __

 __

 **Output:**  

    
    
    Time taken by Lists : 1.1984527111053467 seconds
    Time taken by NumPy Arrays : 0.13434123992919922 seconds
    
    
    
    

From the output of the above program, we see that the NumPy Arrays execute
very much faster than the Lists in Python. There is a big difference between
the execution time of arrays and lists.

 **NumPy Arrays are faster than Python Lists because of the following
reasons:**  

  * An array is a collection of homogeneous data-types that are stored in contiguous memory locations. On the other hand, a list in Python is a collection of heterogeneous data types stored in non-contiguous memory locations.
  * The NumPy package breaks down a task into multiple fragments and then processes all the fragments parallelly.
  * The NumPy package integrates C, C++, and Fortran codes in Python. These programming languages have very little execution time compared to Python.

Below is a program which compares the execution time of different operations
on NumPy arrays and Python Lists:  

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing required packages

import numpy

import time

 

# size of arrays and lists

size = 1000000

 

# declaring lists

list1 = [i for i in range(size)]

list2 = [i for i in range(size)]

# decalring arrays

array1 = numpy.arange(size)

array2 = numpy.arange(size)

# Concatenation

print("\nConcatenation:")

# list

initialTime = time.time()

list1 = list1 + list2

# calculating execution time

print("Time taken by Lists :",

 (time.time() - initialTime),

 "seconds")

 

# NumPy array

initialTime = time.time()

array = numpy.concatenate((array1, array2),

 axis = 0)

# calculating execution time

print("Time taken by NumPy Arrays :",

 (time.time() - initialTime),

 "seconds")

# Dot Product

dot = 0

print("\nDot Product:")

# list

initialTime = time.time()

for a, b in zip(list1, list2):

 dot = dot + (a * b)

 

# calculating execution time

print("Time taken by Lists :",

 (time.time() - initialTime),

 "seconds")

 

# NumPy array

initialTime = time.time()

array = numpy.dot(array1, array2)

# calculating execution time

print("Time taken by NumPy Arrays :",

 (time.time() - initialTime),

 "seconds")

# Scalar Addtion

print("\nScalar Addition:")

# list

initialTime = time.time()

list1 =[i + 2 for i in range(size)]

# calculating execution time

print("Time taken by Lists :",

 (time.time() - initialTime),

 "seconds")

 

# NumPy array

initialTime = time.time()

array1 = array1 + 2

# calculating execution time

print("Time taken by NumPy Arrays :",

 (time.time() - initialTime),

 "seconds")

# Deletion

print("\nDeletion: ")

# list

initialTime = time.time()

del(list1)

# calculating execution time

print("Time taken by Lists :",

 (time.time() - initialTime),

 "seconds")

 

# NumPy array

initialTime = time.time()

del(array1)

# calculating execution time

print("Time taken by NumPy Arrays :",

 (time.time() - initialTime),

 "seconds")  
  
---  
  
 __

 __

 **Output:**  

    
    
    Concatenation:
    Time taken by Lists : 0.02946329116821289 seconds
    Time taken by NumPy Arrays : 0.011709213256835938 seconds
    
    Dot Product:
    Time taken by Lists : 0.179551362991333 seconds
    Time taken by NumPy Arrays : 0.004144191741943359 seconds
    
    Scalar Addition:
    Time taken by Lists : 0.09385180473327637 seconds
    Time taken by NumPy Arrays : 0.005884408950805664 seconds
    
    Deletion: 
    Time taken by Lists : 0.01268625259399414 seconds
    Time taken by NumPy Arrays : 3.814697265625e-06 seconds
    
    
    
    

From the above program, we conclude that operations on NumPy arrays are
executed faster than Python lists. Moreover, the Deletion operation has the
highest difference in execution time between an array and a list compared to
other operations in the program.  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

