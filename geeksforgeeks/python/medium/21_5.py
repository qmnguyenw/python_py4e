Iterate over a list in Python



List is equivalent to arrays in other languages, with the extra benefit of
being dynamic in size. In Python, the list is a type of container in Data
Structures, which is used to store multiple data at the same time. Unlike
Sets, lists in Python are ordered and have a definite count.  
There are multiple ways to iterate over a list in Python. Let’s see all the
different ways to iterate over a list in Python, and performance comparison
between them.  

**Method #1:** Using For loop

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to iterate over a list

list = [1, 3, 5, 7, 9]

 

# Using for loop

for i in list:

 print(i)  
  
---  
  
 __

 __

 **Output:**  

    
    
    1
    3
    5
    7
    9
    
    

  
**Method #2:** For loop and range()  
In case we want to use the traditional for loop which iterates from number x
to number y.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to iterate over a list

list = [1, 3, 5, 7, 9]

 

# getting length of list

length = len(list)

 

# Iterating the index

# same as 'for i in range(len(list))'

for i in range(length):

 print(list[i])  
  
---  
  
 __

 __

 **Output:**  

  

  

    
    
    1
    3
    5
    7
    9
    
    

Iterating using the index is not recommended if we can iterate over the
elements (as done in Method #1).  
  
**Method #3:** Using while loop  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to iterate over a list

list = [1, 3, 5, 7, 9]

 

# Getting length of list

length = len(list)

i = 0

 

# Iterating using while loop

while i < length:

 print(list[i])

 i += 1  
  
---  
  
 __

 __

 **Output:**  

    
    
    1
    3
    5
    7
    9
    
    

  
**Method #4:** Using list comprehension (Possibly the most concrete way).  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to iterate over a list

list = [1, 3, 5, 7, 9]

 

# Using list comprehension

[print(i) for i in list]  
  
---  
  
 __

 __

 **Output:**  

    
    
    1
    3
    5
    7
    9
    
    

  
**Method #5:** Using enumerate()  
If we want to convert the list into an iterable list of tuples (or get the
index based on a condition check, for example in linear search you might need
to save the index of minimum element), you can use the enumerate() function.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to iterate over a list

list = [1, 3, 5, 7, 9]

 

# Using enumerate()

for i, val in enumerate(list):

 print (i, ",",val)  
  
---  
  
 __

 __

 **Output:**  

    
    
    0 , 1
    1 , 3
    2 , 5
    3 , 7
    4 , 9
    
    

**Note:** Even _method #2_ can be used to find the index, but _method #1_
can’t (Unless an extra variable is incremented every iteration) and _method
#5_ gives a concise representation of this indexing.  
  
**Method #6:** Using Numpy  
For very large n-dimensional lists (for example an image array), it is
sometimes better to use an external library such as numpy.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program for

# iterating over array

import numpy as geek

 

# creating an array using 

# arrange method

a = geek.arange(9)

 

# shape array with 3 rows 

# and 4 columns

a = a.reshape(3, 3)

 

# iterating an array

for x in geek.nditer(a):

 print(x)  
  
---  
  
 __

 __

 **Output:**  

    
    
    0
    1
    2
    3
    4
    5
    6
    7
    8
    
    

We can use np.ndenumerate() to mimic the behavior of enumerate. The extra
power of numpy comes from the fact that we can even control the way to visit
the elements (Fortran order rather than C order, say :)) but the one caveat is
that the np.nditer treats the array as read-only by default, so one must pass
extra flags such as op_flags=[‘readwrite’] for it to be able to modify
elements.  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

