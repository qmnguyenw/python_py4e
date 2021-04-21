Python | Merge first and last elements separately in a list



Given a list of lists, where each sublist consists of only two elements, write
a Python program to merge the first and last element of each sublist
separately and finally, output a list of two sub-lists, one containing all
first elements and other containing all last elements.

 **Examples:**

    
    
    **Input :** [['x', 'y'], ['a', 'b'], ['m', 'n']]
    **Output :** [['x', 'a', 'm'], ['y', 'b', 'n']]
    
    **Input :** [[1, 2], [3, 4], [5, 6], [7, 8]]
    **Output :** [[1, 3, 5, 7], [2, 4, 6, 8]]
    

  
**Approach #1 :** List comprehension and zip

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to Merge first and last

# elements separately in a list of lists

 

def merge(lst):

 

 return [list(ele) for ele in list(zip(*lst))]

 

# Driver code

lst = [['x', 'y'], ['a', 'b'], ['m', 'n']]

print(merge(lst))  
  
---  
  
 __

 __

 **Output:**

    
    
    [['x', 'a', 'm'], ['y', 'b', 'n']]
    

  
**Approach #2 :** Using _Numpy_ array

  

  

First convert the given list to _numpy_ array and then return transpose of the
array, and finally convert the array to list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to Merge first and last

# elements separately in a list of lists

import numpy as np

 

def merge(lst):

 arr = np.array(lst)

 return arr.T.tolist()

 

# Driver code

lst = [['x', 'y'], ['a', 'b'], ['m', 'n']]

print(merge(lst))  
  
---  
  
 __

 __

 **Output:**

    
    
    [['x', 'a', 'm'], ['y', 'b', 'n']]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

