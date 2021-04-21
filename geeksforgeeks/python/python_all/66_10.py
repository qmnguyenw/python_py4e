Python – Extract Similar pairs from List



Sometimes, while working with Python lists, we can have a problem in which we
need to perform extraction of all the elements pairs in list. This kind of
problem can have application in domains such as web development and day-day
programming. Let’s discuss certain ways in which this task can be performed.

>  **Input** : test_list = [1, 2, 3, 4]  
>  **Output** : []
>
>  **Input** : test_list = [2, 2, 2, 2, 3, 3, 4]  
>  **Output** : [(2, 2), (2, 2), (3, 3)]

 **Method #1 : UsingCounter() \+ list comprehension**  
The combination of above functions can be used to solve this problem. In this,
frequencies are extracted using Counter() and pairs construction is done used
list comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract Similar pairs from List

# Using Counter() + list comprehension

from collections import Counter

 

# initializing list

test_list = [4, 6, 7, 4, 2, 6, 2, 8]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Extract Similar pairs from List

# Using Counter() + list comprehension

res = [(key, key) for key, val in Counter(test_list).items() 

 for _ in range(val // 2)]

 

# printing result 

print("The records after pairing : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original list is : [4, 6, 7, 4, 2, 6, 2, 8]
    The records after pairing : [(4, 4), (6, 6), (2, 2)]
    

