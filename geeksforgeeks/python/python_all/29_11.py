Python – Random range in list



Given a List, extract random range from it.

> **Input** : test_list = [3, 19, 4, 8, 10, 13, 5, 7, 2, 1, 4]  
> **Output** : [5, 7, 2, 1]  
> **Explanation** : A random range elements are extracted of any length.
>
>  **Input** : test_list = [3, 19, 4, 8, 10, 13, 5, 7, 2, 1, 4]  
> **Output** : [4, 8]  
> **Explanation** : A random range elements are extracted of any length.

**Method : Using randrange() + slicing**

 **randrange():** **** Python offers a function that can generate random
numbers from a specified range and also allowing rooms for steps to be
included, called _randrange()_ in _random_ module.

  

  

In this, we extract index of list, and for first index, and then again employ
the function to get end part of range using _randrange()_ from start index to
list length. The range is extracted using slicing.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Random range in list

# Using randrange() + slicing

import random

 

 

# function to Random range in list

def rabdomRangeList(test_list):

 # getting ranges

 strt_idx = random.randrange(0, len(test_list) - 1)

 end_idx = random.randrange(strt_idx, len(test_list) - 1)

 

 # getting range elements

 res = test_list[strt_idx: end_idx]

 

 return str(res)

 

 

# Driver Code

# initializing list

input_list1 = [3, 19, 4, 8, 10, 13, 5, 7,
2, 1, 4]

 

# printing original list

print("\nThe original list is : ", input_list1)

 

# printing result

print("Required List : " + rabdomRangeList(input_list1))

 

 

# initializing list

input_list2 = [3, 19, 4, 8, 10, 13, 5, 7,
2, 1, 4]

 

# printing original list

print("\nThe original list is : ", input_list2)

 

# printing result

print("Required List : " + rabdomRangeList(input_list2))

 

 

# initializing list

input_list3 = [3, 19, 4, 8, 10, 13, 5, 7,
2, 1, 4]

 

# printing original list

print("\nThe original list is : ", input_list3)

 

# printing result

print("Required List : " + rabdomRangeList(input_list3))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is :  [3, 19, 4, 8, 10, 13, 5, 7, 2, 1, 4]
    Required List : [19]
    
    The original list is :  [3, 19, 4, 8, 10, 13, 5, 7, 2, 1, 4]
    Required List : [10, 13, 5, 7]
    
    The original list is :  [3, 19, 4, 8, 10, 13, 5, 7, 2, 1, 4]
    Required List : []

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

