Python program to right rotate n-numbers by 1



Given a number n. The task is to print n-integers n-times (starting from 1)
and right rotate the integers by after each iteration.  
 **Examples:**  

    
    
    **Input :** 6
    **Output :**
    1 2 3 4 5 6
    2 3 4 5 6 1
    3 4 5 6 1 2
    4 5 6 1 2 3
    5 6 1 2 3 4
    6 1 2 3 4 5
    
    **Input :** 3
    **Output :**
    1 2 3 
    2 3 1 
    3 1 2
    
    
    

Below is the implementation.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

def print_pattern(n):

 for i in range(1, n+1, 1):

 for j in range(1, n+1, 1):

 # check that if index i is

 # equal to j

 if i == j:

 print(j, end=" ")

 # if index i is less than j

 if i <= j:

 for k in range(j+1, n+1, 1):

 print(k, end=" ")

 for p in range(1, j, 1):

 print(p, end=" ")

 # print new line

 print()

# Driver's code

print_pattern(3)  
  
---  
  
 __

 __

 **Output:**  

    
    
    1 2 3 
    2 3 1 
    3 1 2 
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

