Python program to select Random value form list of lists



Given a list of lists. The task is to extract a random element from it.

 **Examples:**

    
    
     **Input** : test_list = [[4, 5, 5], [2, 7, 4], [8, 6, 3]]
    **Output** : 7
    **Explanation** : Random number extracted from Matrix.
    
    **Input** : test_list = [[4, 5, 5], [2, 7, 4], [8, 6, 3]], r_no = 2
    **Output** : 6
    **Explanation** : Random number extracted from 2nd row from Matrix.

 **Method #1 : Using chain.from_iterable() + random.choice()**

In this, we flatten the Matrix to list using from_iterable() and choice() is
used to get a random number from the list.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Random Matrix Element

# Using chain.from_iterables() + random.choice()

from itertools import chain

import random

 

# initializing list

test_list = [[4, 5, 5], [2, 7, 4], [8, 6,
3]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# choice() for random number, from_iterables for flattening

res = random.choice(list(chain.from_iterable(test_list)))

 

# printing result

print("Random number from Matrix : " + str(res))  
  
---  
  
 __

 __

 **Output**

  

  

    
    
    The original list is : [[4, 5, 5], [2, 7, 4], [8, 6, 3]]
    Random number from Matrix : 6
    

