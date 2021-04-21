Python – Construct Sum pairs equal to K



Sometimes, while working with Python lists, we can have problem in which we
need to extract pairs which have sum equal to K. This kind of problem is
common and can have application in domains such as web development and day-day
programming. Let’s discuss certain ways in which this task can be performed.

    
    
    **Input** : 
    test_list = [1, 9, 5, 5, 7]
    K = 10
    **Output** : [(1, 9), (5, 5)]
    
    
    **Input** : 
    test_list = [1, 9, 7, 8, 3]
    K = 12
    **Output** : [(9, 3)]
    

**Method #1 : Using list comprehension +sum()**  
The combination of above functions can be used to solve this problem. In this,
we perform the task of finding summation equal to K using sum() and list
comprehension is used to logic and pair building.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Construct Sum pairs equal to K

# Using list comprehension + sum()

 

# initializing list

test_list = [3, 4, 0, 5, 2]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 7

 

# Construct Sum pairs equal to K

# Using list comprehension + sum()

res = [(test_list[idx], test_list[j]) for idx in
range(len(test_list))

 for j in range(idx + 1, len(test_list))

 if sum((test_list[idx], test_list[j])) == K]

 

# printing result 

print("The paired tuples equal to K : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list is : [3, 4, 0, 5, 2]
    The paired tuples equal to K  : [(3, 4), (5, 2)]
    

**Method #2 : Usingcombinations() + sum()**  
The combination of above functions can be used to solve this problem. In this
combination() is used to form pairs equal to K.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Construct Sum pairs equal to K

# Using combinations() + sum()

from itertools import combinations

 

# initializing list

test_list = [3, 4, 0, 5, 2]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 7

 

# Construct Sum pairs equal to K

# Using combinations() + sum()

res = [ele for ele in combinations(test_list, 2) if
sum(ele) == K]

 

# printing result 

print("The paired tuples equal to K : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list is : [3, 4, 0, 5, 2]
    The paired tuples equal to K  : [(3, 4), (5, 2)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

