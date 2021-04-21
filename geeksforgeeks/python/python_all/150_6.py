Python | Find elements of a list by indices



Given two lists with elements and indices, write a Python program to find
elements of _list 1_ at indices present in _list 2_.

 **Examples:**

    
    
    **Input :** lst1 = [10, 20, 30, 40, 50]
            lst2 = [0, 2, 4]
    **Output :** [10, 30, 50]
    **Explanation:**
    Output elements at indices 0, 2 and 4 i.e 10, 30 and 50 respectively. 
    
    **Input :** lst1 = ['Hello', 'geeks', 'for', 'geeks']
            lst2 = [1, 2, 3]
    **Output :** ['geeks', 'for', 'geeks']
    

  
Below are some Pythonic approaches to do the above task.

 **Approach #1 :** Naive(List comprehension)

The first approach to find the desired elements is to use list comprehension.
We traverse through ‘lst2’ and for each ith element, we output lst1[i].

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to Find elements of a

# list by indices present in another list

 

def findElements(lst1, lst2):

 return [lst1[i] for i in lst2]

 

# Driver code

lst1 = [10, 20, 30, 40, 50]

lst2 = [0, 2, 4]

print(findElements(lst1, lst2))  
  
---  
  
 __

 __

 **Output:**

    
    
    [10, 30, 50]
    

  
**Approach #2 :** Using Python map()

We can also use Python map() method where we apply lst1.__getitem__
function on _lst2_ which return lst1[i] for each element ‘i’ of lst2.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to Find elements of a

# list by indices present in another list

 

def findElements(lst1, lst2):

 return list(map(lst1.__getitem__, lst2))

 

# Driver code

lst1 = [10, 20, 30, 40, 50]

lst2 = [0, 2, 4]

print(findElements(lst1, lst2))  
  
---  
  
 __

 __

 **Output:**

    
    
    [10, 30, 50]
    

  
**Approach #3 :** Using itemgetter()

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to Find elements of a

# list by indices present in another list

from operator import itemgetter 

 

def findElements(lst1, lst2):

 return list((itemgetter(*lst2)(lst1)))

 

# Driver code

lst1 = [10, 20, 30, 40, 50]

lst2 = [0, 2, 4]

print(findElements(lst1, lst2))  
  
---  
  
 __

 __

 **Output:**

    
    
    [10, 30, 50]
    

  
**Approach #4 :** Using numpy

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to Find elements of a

# list by indices present in another list

import numpy as np 

 

def findElements(lst1, lst2):

 return list(np.array(lst1)[lst2])

 

# Driver code

lst1 = [10, 20, 30, 40, 50]

lst2 = [0, 2, 4]

print(findElements(lst1, lst2))  
  
---  
  
 __

 __

 **Output:**

    
    
    [10, 30, 50]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

