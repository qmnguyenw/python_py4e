Python | Find most common element in each column in a 2D list



Given a 2D list, write a Python program to find the most common element in
each column of the 2D list.

 **Examples:**

    
    
    **Input :** [[1, 1, 3],
            [2, 3, 3],
            [3, 2, 2],
            [2, 1, 3]]
    **Output :** [2, 1, 3]
    
    **Input :** [['y', 'y'],
             ['y', 'x'],
             ['x', 'x']]
    **Output :** ['y', 'x']
    

**Method #1 :** Using _most_common()_ from _collections_ module

 _most_common()_ return a list of the _n_ most common elements and their
counts from the most common to the least. Thus, we can easily find the most
common elements in each column using list comprehension.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to find most common

# element in each column in a 2D list

from collections import Counter

 

def mostCommon(lst):

 

 return [Counter(col).most_common(1)[0][0] for col in
zip(*lst)]

 

# Driver code

lst = [[1, 1, 3],

 [2, 3, 3],

 [3, 2, 2],

 [2, 1, 3]]

print(mostCommon(lst))  
  
---  
  
 __

 __

 **Output:**

    
    
    [2, 1, 3]
    

  
**Method #3 :** Using _mode()_ from _statistics_ module

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to find most common

# element in each column in a 2D list

from scipy.stats import mode

import numpy as np

 

def mostCommon(lst):

 

 val, count = mode(lst, axis = 0)

 return val.ravel().tolist()

 

# Driver code

lst = [[1, 1, 3],

 [2, 3, 3],

 [3, 2, 2],

 [2, 1, 3]]

print(mostCommon(lst))  
  
---  
  
 __

 __

 **Output:**

    
    
    [2, 1, 3]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

