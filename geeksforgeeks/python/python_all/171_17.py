Python program to insert an element into sorted list



Given a sorted list and an element, Write a Python program to insert the
element into the given list in sorted position.

 **Examples:**

    
    
    **Input :** list = [1, 2, 4], n = 3
    **Output :** list = [1, 2, 3, 4]
    
    **Input :** list = ['a', 'b', 'c', 'd'], n = 'e'
    **Output :** list = ['a', 'b', 'c', 'd', 'e']
    

**Approach #1 :**  
This approach is the brute force method. Since the list is already sorted, we
begin with a loop and check if the list element is greater than the given
element. If yes, the given element need to be inserted at this position.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to insert

# an element into sorted list

 

# Function to insert element

def insert(list, n):

 

 # Searching for the position

 for i in range(len(list)):

 if list[i] > n:

 index = i

 break

 

 # Inserting n in the list

 list = list[:i] + [n] + list[i:]

 return list

 

# Driver function

list = [1, 2, 4]

n = 3

 

print(insert(list, n))  
  
---  
  
 __

 __

 **Output:**

    
    
    [1, 2, 3, 4]
    

  
**Approach #2 :**  
Python comes with a _bisect module_ whose purpose is to find a position in
list where an element needs to be inserted to keep the list sorted. Thus we
use this module to solve the given problem.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to insert

# an element into sorted list

import bisect 

 

def insert(list, n):

 bisect.insort(list, n) 

 return list

 

# Driver function

list = [1, 2, 4]

n = 3

 

print(insert(list, n))  
  
---  
  
 __

 __

 **Output:**

    
    
    [1, 2, 3, 4]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

