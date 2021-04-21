Python | Get unique values from a list



Given a list, print all the unique numbers in any order.  
 **Examples:**

    
    
    Input : 10 20 10 30 40 40
    Output : 10 20 30 40 
    
    Input : 1 2 1 1 3 4 3 3 5 
    Output : 1 2 3 4 5  

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Method 1 : Traversal of list**

Using traversal, we can traverse for every element in the list and check if
the element is in the unique_list already if it is not over there, then we can
append it in the unique_list. This is done using one for loop and other if
statement which check if the value is in the unique list or not which is
equivalent to another for loop.

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to check if two

# to get unique values from list

# using traversal

# function to get unique values

def unique(list1):

 # intilize a null list

 unique_list = []

 

 # traverse for all elements

 for x in list1:

 # check if exists in unique_list or not

 if x not in unique_list:

 unique_list.append(x)

 # print list

 for x in unique_list:

 print x,

 

 

# driver code

list1 = [10, 20, 10, 30, 40, 40]

print("the unique values from 1st list is")

unique(list1)

list2 =[1, 2, 1, 1, 3, 4, 3, 3, 5]

print("\nthe unique values from 2nd list is")

unique(list2)  
  
---  
  
 __

 __

 **Output:**

    
    
    the unique values from 1st list is
    10 20 30 40 
    the unique values from 2nd list is
    1 2 3 4 5

 **Method 2 : Using Set**

  

  

Using set() property of Python, we can easily check for the unique values.
Insert the values of the list in a set. Set only stores a value once even if
it is inserted more then once. After inserting all the values in the set by
list_set=set(list1), convert this set to a list to print it.

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to check if two

# to get unique values from list

# using set

# function to get unique values

def unique(list1):

 

 # insert the list to the set

 list_set = set(list1)

 # convert the set to the list

 unique_list = (list(list_set))

 for x in unique_list:

 print x,

 

# driver code

list1 = [10, 20, 10, 30, 40, 40]

print("the unique values from 1st list is")

unique(list1)

list2 =[1, 2, 1, 1, 3, 4, 3, 3, 5]

print("\nthe unique values from 2nd list is")

unique(list2)  
  
---  
  
 __

 __

 **Output:**

    
    
    the unique values from 1st list is
    40 10 20 30 
    the unique values from 2nd list is
    1 2 3 4 5

 **Method 3 : Using numpy.unique**

Using Python’s import numpy, the unique elements in the array are also
obtained. In first step convert the list to **x=numpy.array(list)** and then
use **numpy.unique(x)** function to get the unique values from the list.
**numpy.unique()** returns only the unique values in the list.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

#Ppython program to check if two

# to get unique values from list

# using numpy.unique

import numpy as np

# function to get unique values

def unique(list1):

 x = np.array(list1)

 print(np.unique(x))

 

# driver code

list1 = [10, 20, 10, 30, 40, 40]

print("the unique values from 1st list is")

unique(list1)

list2 =[1, 2, 1, 1, 3, 4, 3, 3, 5]

print("\nthe unique values from 2nd list is")

unique(list2)  
  
---  
  
 __

 __

 **Output**  

    
    
    the unique values from 1st list is
    [10 20 30 40]
    
    the unique values from 2nd list is
    [1 2 3 4 5]

 **Method #4: Using collections.Counter()**

Using python import Counter() from collections print all the keys of Counter
elements or we print directly by using **“*”** symbol.

Below is the implementation of above approach.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to check if two

# to get unique values from list

# importing counter from collections

from collections import Counter

# Function to get unique values

def unique(list1):

 

 # Print directly by using * symbol

 print(*Counter(list1))

# driver code

list1 = [10, 20, 10, 30, 40, 40]

print("the unique values from 1st list is")

unique(list1)

list2 = [1, 2, 1, 1, 3, 4, 3, 3, 5]

print("\nthe unique values from 2nd list is")

unique(list2)

# This code is contributed by vikkycirus  
  
---  
  
 __

 __

 **Output:**

    
    
    the unique values from 1st list is
    10 20 30 40
    
    the unique values from 2nd list is
    1 2 3 4 5

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

