Python Program to get all possible differences between set elements



Given a set, the task is to write a Python program to get all possible
differences between its elements.

    
    
     **Input :** test_set = {1, 5, 2, 7, 3, 4, 10, 14}
    **Output :** {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}
    **Explanation :** All possible differences are computed.
    
    **Input :** test_set = {1, 5, 2, 7}
    **Output :** {1, 2, 3, 4, 5, 6}
    **Explanation :** All possible differences are computed.

 **Method #1 : Using** **combinations()** **+** **abs()** **\+ loop**

In this, all the possible pairs are extracted using combinations(). Then loop
is used to traverse and abs() is used to get difference.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# All elements difference in Set

# Using combinations + abs() + loop

from itertools import combinations

 

# initializing strings set

test_set = {1, 5, 2, 7, 3, 4, 10, 14}

 

# printing original string

print("The original set is : " + str(test_set))

 

# getting combinations

combos = combinations(test_set, 2)

 

res = set()

 

# adding differences in set

for x, y in combos:

 res.add(abs(x - y))

 

# printing result

print("All possible differences : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original set is : {1, 2, 3, 4, 5, 7, 10, 14}
>
>  
>
>
>  
>
>
> All possible differences : {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}

 **Method #2 : Using set comprehension + combinations() + abs()**

In this, we perform task of getting and setting all elements using set
comprehension as one liner approach to solve the problem.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# All elements difference in Set

# Using set comprehension + combinations() + abs()

from itertools import combinations

 

# initializing strings set

test_set = {1, 5, 2, 7, 3, 4, 10, 14}

 

# printing original string

print("The original set is : " + str(test_set))

 

# set comprehension providing consize solution

res = {abs(x - y) for x, y in combinations(test_set,
2)}

 

# printing result

print("All possible differences : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original set is : {1, 2, 3, 4, 5, 7, 10, 14}
>
> All possible differences : {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

