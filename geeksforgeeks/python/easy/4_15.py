Array Copying in Python



Let us see how to copy arrays in Python. There are 3 ways to copy arrays :

  * Simply using the assignment operator.
  * Shallow Copy
  * Deep Copy

### Assigning the Array

We can create a copy of an array by using the assignment operator (=).  

**Syntax :**

    
    
    new_arr = old_ arr

In Python, Assignment statements do not copy objects, they create bindings
between a target and an object. When we use = operator user thinks that this
creates a new object; well, it doesn’t. It only creates a new variable that
shares the reference of the original object.  

  

  

**Example :**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing the module

from numpy import *

# creating the first array

arr1 = array([2, 6, 9, 4]) 

# displaying the identity of arr1

print(id(arr1))

# assigning arr1 to arr2

arr2 = arr1 

# displaying the identity of arr2

print(id(arr2))

# making a change in arr1

arr1[1] = 7

# displayin the arrays

print(arr1)

print(arr2)  
  
---  
  
 __

 __

 **Output :**  

    
    
    117854800
    117854800
    [2 7 9 4]
    [2 7 9 4]

We can see that both the arrays reference the same object.  

### Shallow Copy

A shallow copy means constructing a new collection object and then populating
it with references to the child objects found in the original. The copying
process does not recurse and therefore won’t create copies of the child
objects themselves. In the case of shallow copy, a reference of the object is
copied in another object. It means that any changes made to a copy of the
object do reflect in the original object. We will be implementing shallow copy
using the **view()** function.  
 **Example :**  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing the module

from numpy import *

 

# creating the first array

arr1 = array([2, 6, 9, 4])

# displaying the identity of arr1

print(id(arr1))

# shallow copy arr1 in arr2 using view()

arr2 = arr1.view() 

# displaying the identity of arr2

print(id(arr2))

 

# making a change in arr1

arr1[1] = 7

 

# displayin the arrays

print(arr1)

print(arr2)  
  
---  
  
 __

 __

This time although the 2 arrays reference different objects, still on changing
the value of one, the value of another also changes.  

### Deep Copy

Deep copy is a process in which the copying process occurs recursively. It
means first constructing a new collection object and then recursively
populating it with copies of the child objects found in the original. In the
case of deep copy, a copy of the object is copied into another object. It
means that any changes made to a copy of the object do not reflect in the
original object. We will be implementing deep copy using the **copy()**
function.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing the module

from numpy import *

 

# creating the first array

arr1 = array([2, 6, 9, 4])

# displaying the identity of arr1

print(id(arr1))

# shallow copy arr1 in arr2 using view()

arr2 = arr1.copy()

# displaying the identity of arr2

print(id(arr2))

 

# making a change in arr1

arr1[1] = 7

 

# displayin the arrays

print(arr1)

print(arr2)  
  
---  
  
 __

 __

 **Output :**  

    
    
    121258976
    125714048
    [2 7 9 4]
    [2 6 9 4]

This time the changes made in one array are not reflected in the other array.

## Deep Copy Continued

If you are dealing with NumPy matrices, then numpy.copy() will give you a deep
copy. However, if your matrix is simply a list of lists then consider the
below two approaches in the task of rotating an image (represented as a list
of a list) 90 degrees:

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import copy

def rotate_matrix(image):

 # Copy method one

 copy_image_one = copy.deepcopy(image)

 print("Original", matrix)

 print("Copy of original", copy_image_one)

 N = len(matrix)

 # Part 1, reverse order within each row

 for row in range(N):

 for column in range(N):

 copy_image_one[row][column] = image[row][N-column-1]

 print("After modification")

 print("Original", matrix)

 print("Copy", copy_image_one)

 # Copy method two

 copy_image_two = [list(row) for row in copy_image_one]

 # Test on what happens when you remove list from the above code.

 # Part 2, transpose

 for row in range(N):

 for column in range(N):

 copy_image_two[column][row] = copy_image_one[row][column]

 return copy_image_two

if __name__ == "__main__":

 matrix = [[1, 2, 3],

 [4, 5, 6],

 [7, 8, 9]]

 print("Rotated image", rotate_matrix(matrix))  
  
---  
  
 __

 __

 **Output:**

    
    
    Original [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Copy of original [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    After modification
    Original [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Copy [[3, 2, 1], [6, 5, 4], [9, 8, 7]]
    Rotated image [[3, 6, 9], [2, 5, 8], [1, 4, 7]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

