Python | Transpose elements of two dimensional list



Given a two-dimensional list of integers, write a Python program to get the
transpose of given list of lists.  
In Python, a matrix can be interpreted as a list of lists. Each element is
treated as a row of the matrix. For example m = [[10, 20], [40, 50], [30, 60]]
represents a matrix of 3 rows and 2 columns. First element of the list – m[0]
and element in first row, first column – m[0][0].

 **Example:**

    
    
    **Input :**  l1 = [[4, 5, 3, 9],
                   [7, 1, 8, 2],
                   [5, 6, 4, 7]]
    
    **Output :** lt = [[4, 7, 5],
                   [5, 1, 6],
                   [3, 8, 4],
                   [9, 2, 7]]

**Method #1:** Using loops

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to get transpose

# elements of two dimension list

def transpose(l1, l2):

 # iterate over list l1 to the length of an item

 for i in range(len(l1[0])):

 # print(i)

 row =[]

 for item in l1:

 # appending to new list with values and index positions

 # i contains index position and item contains values

 row.append(item[i])

 l2.append(row)

 return l2

# Driver code

l1 = [[4, 5, 3, 9], [7, 1, 8, 2], [5,
6, 4, 7]]

l2 = []

print(transpose(l1, l2))  
  
---  
  
 __

 __

 **Output**

    
    
    [[4, 7, 5], [5, 1, 6], [3, 8, 4], [9, 2, 7]]
    

**Method #2:** Using List comprehensions

  

  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to get transpose

# elements of two dimension list

def transpose(l1, l2):

 # we have nested loops in comprehensions

 # value of i is assigned using inner loop

 # then value of item is directed by row[i]

 # and appended to l2

 l2 =[[row[i] for row in l1] for i in
range(len(l1[0]))]

 return l2

# Driver code

l1 = [[4, 5, 3, 9], [7, 1, 8, 2], [5,
6, 4, 7]]

l2 = []

print(transpose(l1, l2))  
  
---  
  
 __

 __

 **Output**

    
    
    [[4, 7, 5], [5, 1, 6], [3, 8, 4], [9, 2, 7]]
    

**Method #3:** Using numpy

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to get transpose

# elements of two dimension list

import numpy

 

l1= [[4, 5, 3, 9], [7, 1, 8, 2], [5,
6, 4, 7]]

print(numpy.transpose(l1))  
  
---  
  
 __

 __

 **Output:**

    
    
    [[4 7 5]
     [5 1 6]
     [3 8 4]
     [9 2 7]]

 **Method #4:** Using zip function

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to get transpose

# elements of two dimension list

def transpose(l1, l2):

 # star operator will first

 # unpack the values of 2D list

 # and then zip function will

 # pack them again in opposite manner

 l2 = list(map(list, zip(*l1)))

 return l2

# Driver code

l1 = [[4, 5, 3, 9], [7, 1, 8, 2], [5,
6, 4, 7]]

l2 = []

print(transpose(l1, l2))

# code contributed by

# chaudhary_19

# Mayank Chaudhary

# modified by Chirag Shilwant  
  
---  
  
 __

 __

 **Output**

    
    
    [[4, 7, 5], [5, 1, 6], [3, 8, 4], [9, 2, 7]]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

