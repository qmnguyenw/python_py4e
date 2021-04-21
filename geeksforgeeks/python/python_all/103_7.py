Python program to print Aitken’s array



Given a number n. The task is to print the Aikten’s array upto n.

 **Examples:**

    
    
    **Input:** 5
    **Output:**
    [1]
    [1, 2]
    [2, 3, 5]
    [5, 7, 10, 15]
    [15, 20, 27, 37, 52]
    
    
    **Input:** 7
    **Output:**
    [1]
    [1, 2]
    [2, 3, 5]
    [5, 7, 10, 15]
    [15, 20, 27, 37, 52]
    [52, 67, 87, 114, 151, 203]
    [203, 255, 322, 409, 523, 674, 877]
    

**To print it first we follow the following steps:**

  * We write 1 in the first row.
  * Next, we fill the leftmost value of each row by the rightmost value of the previous row.
  * The next elements of each row are filled by the simple rule i.e. each element of a particular row is the sum of values to the left of that row with the values of the upper row at the same position.  
For better understanding, let’s consider the third row of the above example
consisting of the elements 2, 3, 5. The leftmost value of this row is the
rightmost value of the above row i.e. 2. The next value 3 is the sum of value
to the left if that row (2) and the value at same position of the above row
(1). Similarly, 5 is the sum of 3 and 2.

Below is the implementation.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to print

# Aitken's array

 

 

from queue import Queue

from functools import reduce, lru_cache

 

 

# for dynamic programming

# Recursive function to print the 

# Aitken's array.

@lru_cache()

def rec(n):

 

 # Base case

 if n == 1:

 print([1])

 return [1]

 

 array = [rec(n-1)[-1]]

 

 for k in range(n-1):

 array.append(array[k] + rec(n-1)[k])

 

 print(array)

 

 return array

 

# Driver's code 

rec(7)  
  
---  
  
 __

 __

 **Output:**

    
    
    [1]
    [1, 2]
    [2, 3, 5]
    [5, 7, 10, 15]
    [15, 20, 27, 37, 52]
    [52, 67, 87, 114, 151, 203]
    [203, 255, 322, 409, 523, 674, 877]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

