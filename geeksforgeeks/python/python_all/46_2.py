Python Program to print all Possible Combinations from the three Digits



Given 3 digits a, b, and c. The task is to find all the possible combinations
from these digits.

 **Examples:**

    
    
     **Input:** [1, 2, 3]
    **Output:**
    1 2 3
    1 3 2
    2 1 3
    2 3 1
    3 1 2
    3 2 1
    
    **Input:** [0, 9, 5]
    **Output:**
    0 9 5
    0 5 9
    9 0 5
    9 5 0
    5 0 9
    5 9 0
    

**Method 1:** Brute force or Naive approach

The naive approach is to run 3 loops from 0 to 3 and print all the numbers
from the list if the indexes are not equal to each other.

 **Example:**

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to print all

# the possible combinations

 

def comb(L):

 

 for i in range(3):

 for j in range(3):

 for k in range(3):

 

 # check if the indexes are not

 # same

 if (i!=j and j!=k and i!=k):

 print(L[i], L[j], L[k])

 

# Driver Code

comb([1, 2, 3])  
  
---  
  
 __

 __

 **Output:**

    
    
    1 2 3
    1 3 2
    2 1 3
    2 3 1
    3 1 2
    3 2 1
    

**Method 2:** Using itertools.permutations()

This method takes a list as an input and returns an object list of tuples that
contain all permutation in a list form.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to print all

# the possible combinations

 

from itertools import permutations

 

# Get all combination of [1, 2, 3]

# of length 3

comb = permutations([1, 2, 3], 3)

 

for i in comb:

 print(i)  
  
---  
  
 __

 __

 **Output:**

    
    
    (1, 2, 3)
    (1, 3, 2)
    (2, 1, 3)
    (2, 3, 1)
    (3, 1, 2)
    (3, 2, 1)
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

