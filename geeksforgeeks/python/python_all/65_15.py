Python – Adjacent Coordinates in N dimension



Sometimes, while working with Python Matrix, we can have a problem in which we
need to extract all the adjacent coordinates of the given coordinate. This
kind of problem can have application in many domains such as web development
and school programming. Lets discuss certain way in which this task can be
performed.

>  **Input** : test_tup = (1, 2, 3)  
>  **Output** : [[0, 1, 2], [0, 1, 3], [0, 1, 4], [0, 2, 2], [0, 2, 3], [0, 2,
> 4], [0, 3, 2], [0, 3, 3], [0, 3, 4], [1, 1, 2], [1, 1, 3], [1, 1, 4], [1, 2,
> 2], [1, 2, 3], [1, 2, 4], [1, 3, 2], [1, 3, 3], [1, 3, 4], [2, 1, 2], [2, 1,
> 3], [2, 1, 4], [2, 2, 2], [2, 2, 3], [2, 2, 4], [2, 3, 2], [2, 3, 3], [2, 3,
> 4]]  
>  **Input** : test_tup = (5, 6)  
>  **Output** : [[4, 5], [4, 6], [4, 7], [5, 5], [5, 6], [5, 7], [6, 5], [6,
> 6], [6, 7]]

 **Method : Using recursion +yield**  
The combination of above functionalities can be used to solve this problem. In
this, we extract the elements dynamically using yield for the coordinates
around the query coordinate and using recursion, process for next column and
row.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Adjacent Coordinates in N dimension

# Using recursion + yield

 

# helper_fnc

def adjac(ele, sub = []):

 if not ele:

 yield sub

 else:

 yield from [idx for j in range(ele[0] - 1,
ele[0] + 2)

 for idx in adjac(ele[1:], sub + [j])]

 

# initializing tuple

test_tup = (3, 4)

 

# printing original tuple

print("The original tuple : " + str(test_tup))

 

# Initialize dictionary keys with Matrix

# Using deepcopy()

res = list(adjac(test_tup))

 

# printing result 

print("The adjacent Coordinates : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original tuple : (3, 4)
    The adjacent Coordinates : [[2, 3], [2, 4], [2, 5], [3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5]]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

