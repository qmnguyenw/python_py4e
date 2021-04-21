Python | Check if a list is contained in another list



Given two lists A and B, write a Python program to Check if list A is
contained in list B without breaking A’s order.

 **Examples:**

    
    
    **Input :** A = [1, 2], B = [1, 2, 3, 1, 1, 2, 2]
    **Output :** True
    
    **Input :** A = ['x', 'y', 'z'], B = ['x', 'a', 'y', 'x', 'b', 'z']
    **Output :** False
    

  
**Approach #1 :** Naive Approach

A simple naive approach is to use two for loops and check if the whole list A
is contained within list B or not. If such a position is met in list A, then
break the loop and return true, otherwise false

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to Check if a list is

# contained in another list without breaking order

 

def removeElements(A, B):

 for i in range(len(B)-len(A)+1):

 for j in range(len(A)):

 if B[i + j] != A[j]:

 break

 else:

 return True

 return False

 

# Driver code

A = [1, 2]

B = [1, 2, 3, 1, 1, 2, 2]

print(removeElements(A, B))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    True
    

