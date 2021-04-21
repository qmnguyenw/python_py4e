Python List VS Array VS Tuple



 **List:** **** A list is of an ordered collection data type that is mutable
which means it can be easily modified and we can change its data values and a
list can be indexed, sliced, and changed and each element can be accessed
using its index value in the list. The following are the main characteristics
of a List:

  * The list is an ordered collection of data types.
  * The list is mutable.
  * List are dynamic and can contain objects of different data types.
  * List elements can be accessed by index number.

 **Example:**

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate List

list = ["mango", "strawberry", "orange",

 "apple", "banana"]

print(list)

# we can specify the range of the

# index by specifying where to start

# and where to end

print(list[2:4])

# we can also change the item in the

# list by using its index number

list[1] = "grapes"

print(list[1])  
  
---  
  
 __

 __

 **Output :**

    
    
    ['mango', 'strawberry', 'orange', 'apple', 'banana']
    ['orange', 'apple']
    grapes

 **Array:** **** An array is a collection of items stored at contiguous memory
locations. The idea is to store multiple items of the same type together. This
makes it easier to calculate the position of each element by simply adding an
offset to a base value, i.e., the memory location of the first element of the
array (generally denoted by the name of the array). The following are the main
characteristics of an Array:

  * An array is an ordered collection of the similar data types.
  * An array is mutable.
  * An array can be accessed by using its index number.

 **Examples:**

  

  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate

# Creation of Array 

 

# importing "array" for array creations

import array as arr

 

# creating an array with integer type

a = arr.array('i', [1, 2, 3])

 

# printing original array

print ("The new created array is : ", end =" ")

for i in range (0, 3):

 print (a[i], end =" ")

print()

 

# creating an array with float type

b = arr.array('d', [2.5, 3.2, 3.3])

 

# printing original array

print ("The new created array is : ", end =" ")

for i in range (0, 3):

 print (b[i], end =" ")  
  
---  
  
 __

 __

 **Output:**

    
    
    The new created array is :  1 2 3 
    The new created array is :  2.5 3.2 3.3

 **Tuple:** **** A tuple is an ordered and an immutable data type which means
we cannot change its values and tuples are written in round brackets. We can
access tuple by referring to the index number inside the square brackets. The
following are the main characteristics of a Tuple:

  * Tuples are immutable and can store any type of data type.
  * it is defined using ().
  * it cannot be changed or replaced as it is an immutable data type.

 **Examples:**

## Python

 __

 __  
 __

 __

 __  
 __  
 __

tuple = ("orange","apple","banana")

print(tuple)

# we can access the items in

# the tuple by its index number

print(tuple[2])

#we can specify the range of the

# index by specifying where to start

# and where to end

print(tuple[0:2])  
  
---  
  
 __

 __

 **Output :**

    
    
    ('orange', 'apple', 'banana')
    banana
    ('orange', 'apple')

##  **Table of Difference between List, Array, and Tuple :**

 **List**|

 **Array**|

 **Tuple**|  List is mutable| Array is mutable| Tuple is immutable| A list is
ordered collection of items| An array is ordered collection of items| A tuple
is an ordered collection of items| Item in the list can be changed or
replaced| Item in the array can be changed or replaced| Item in the tuple
cannot be changed or replaced| List can store more than one data type| Array
can store only similar data types| Tuple can store more than one data type  
---|---|---  
  
Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

