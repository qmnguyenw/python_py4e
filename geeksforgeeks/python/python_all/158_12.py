Python | Find groups of strictly increasing numbers in a list



Given a list of integers, write a Python program to find groups of strictly
increasing numbers.

 **Examples:**

    
    
    **Input :** [1, 2, 3, 5, 6]
    **Output :** [[1, 2, 3], [5, 6]]
    
    **Input :** [8, 9, 10, 7, 8, 1, 2, 3]
    **Output :** [[8, 9, 10], [7, 8], [1, 2, 3]]
    

**Approach #1 :** Pythonic naive

This is a naive approach which uses an extra input list space. It makes use of
a for loop and in every iteration, it checks if the next element increments
from previous by 1. If yes, append it to the current sublist, otherwise,
create another sublist.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to Find groups

# of strictly increasing numbers within 

 

def groupSequence(lst):

 res = [[lst[0]]]

 

 for i in range(1, len(lst)):

 if lst[i-1]+1 == lst[i]:

 res[-1].append(lst[i])

 

 else:

 res.append([lst[i]])

 return res

 

# Driver program 

l = [8, 9, 10, 7, 8, 1, 2, 3]

print(groupSequence(l))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    [[8, 9, 10], [7, 8], [1, 2, 3]]
    

