Python – Inverse Dictionary Values List



Given a Dictionary as value lists, inverse it, i.e map elements in list to
keys and create new values list.

>  **Input** : test_dict = {1: [2, 3], 2: [3], 3: [1]}  
>  **Output** : {2: [1], 3: [1, 2], 1: [3]}  
>  **Explanation** : List elements mapped with their keys.
>
>  **Input** : test_dict = {1: [2, 3, 4]}  
>  **Output** : {2: [1], 3: [1], 4: [1]}  
>  **Explanation** : List elements mapped with their keys.

 **Method : Using defaultdict() + loop**

This is a way in which this task can be performed. In this, we initialize
result keys with dictionary list, and iterate using loop to assign each value
its keys, and reform the result dictionary values list.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Inverse Dictionary Values List

# Using 

from collections import defaultdict

 

# initializing dictionary

test_dict = {1: [2, 3], 2: [3], 3: [1],
4: [2, 1]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing empty list as Values

res = defaultdict(list) 

 

# using loop to perform reverse mapping

for keys, vals in test_dict.items(): 

 for val in vals: 

 res[val].append(keys)

 

# printing result 

print("The required result : " + str(dict(res)))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {1: [2, 3], 2: [3], 3: [1], 4: [2, 1]}
    The required result : {2: [1, 4], 3: [1, 2], 1: [3, 4]}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

