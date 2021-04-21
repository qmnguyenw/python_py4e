Python – List of N size increasing lists



Given integer N and M, construct increasing list till M, each list being N
size i.e all combinations lists.

>  **Input** : N = 2, M = 3  
>  **Output** : [(1, 2), (1, 3), (2, 3)]  
>  **Explanation** : Increasing paired elements.
>
>  **Input** : N = 1, M = 4  
>  **Output** : [(1, ), (2, ), (3, ), (4, )]  
>  **Explanation** : Increasing paired elements.

 **Method #1 : Using loop**

This is one brute force way in which this task can be performed. In this we
iterate for elements till M, and form lists with N size. The drawback is that
we are restricted to limited sized lists.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# List of N size increasing lists

# Using loop

 

# initializing N

N = 2

 

# initializing M

M = 4

 

# outer loop manages lists

res = []

for idx in range(1, M):

 

 # inner loop manages inner elements

 for j in range(idx + 1, M + 1):

 res.append((idx, j))

 

# printing result 

print("The constructed combinations : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The constructed combinations : [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
    

**Method #2 : Using combinations()**

This is inbuild function offering exact functionality required for this
solution. Solves the problem in one liner of getting increasing lists.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# List of N size increasing lists

# Using combinations()

from itertools import combinations

 

# initializing N

N = 2

 

# initializing M

M = 4

 

# using combinations to perform task 

res = list(combinations(list(range(1, M + 1)), N))

 

# printing result 

print("The constructed combinations : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The constructed combinations : [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

