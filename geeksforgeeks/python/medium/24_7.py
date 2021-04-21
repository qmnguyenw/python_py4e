Python | Convert an array to an ordinary list with the same items



Prerequisite : Array in Python

Python program to convert an array to an ordinary list with the same items.

 **Examples:**

    
    
    Input : array('i', [1, 3, 5, 3, 7, 1, 9, 3])
    Output :[1, 3, 5, 3, 7, 1, 9, 3]
    Explanation: the array with elements [1, 3, 5, 3, 
    7, 1, 9, 3] are converted into list with the 
    same elements.
    
    Input :array('k', [45, 23, 56, 12])
    Output :[45, 23, 56, 12]
    Explanation: the array with elements [45, 23, 56, 
    12] are converted into list with the same elements.
    

**Approach to the problem:**  
We want to convert an array into an ordinary list with the same items. For
doing so we need to use a function

    
    
    // This function tolist() converts the array into a list.
    arrayname.tolist()

  

  

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 __

 __  
 __

 __

 __  
 __  
 __

from array import *

def array_list(array_num):

 num_list = array_num.tolist() # list

 print(num_list)

 

# driver code

array_num = array('i', [45,34,67]) # array

array_list(array_num)  
  
---  
  
 __

 __

Output:

    
    
    [45, 34, 67]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

