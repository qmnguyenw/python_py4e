Python | Check if list contains consecutive numbers



Given a list of numbers, write a Python program to check if the list contains
consecutive integers.

 **Examples:**

    
    
    **Input :** [2, 3, 1, 4, 5]
    **Output :** True
    
    **Input :** [1, 2, 3, 5, 6]
    **Output :** False
    

Let’s discuss the few ways we can do this task.  
  
**Approach #1 :** using sorted()

This approach uses sorted() function of Python. We compare the sorted list
with list of range of minimum and maximum integer of the list and return it.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 Program to Create list

# with integers within given range 

 

def checkConsecutive(l):

 return sorted(l) == list(range(min(l),
max(l)+1))

 

# Driver Code

lst = [2, 3, 1, 4, 5]

print(checkConsecutive(lst))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    True
    

