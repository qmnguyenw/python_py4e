Python – All possible pairs in List



Sometimes, while working with Python list, we can have a problem in which we
need to extract all the possible pairs that can be performed from integers
from list. This kind of problem can occur in many domains such as day-day
programming and web development. Let’s discuss certain ways in which this task
can be performed.

>  **Input** : test_list = [1, 7, 4]  
>  **Output** : [(1, 7), (1, 4), (7, 4)]
>
>  **Input** : test_list = [7, 4]  
>  **Output** : [(7, 4)]

 **Method #1 : Using list comprehension +enumerate()**  
This is one of the ways in which this task can be performed. In this, we
perform the task of pairing using nested loops in list comprehension recipe,
and enumerate() is used to check with the next indices while iteration.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# All possible pairs in List

# Using list comprehension + enumerate()

 

# initializing list

test_list = [1, 7, 4, 3]

 

# printing original list 

print("The original list : " + str(test_list))

 

# All possible pairs in List

# Using list comprehension + enumerate()

res = [(a, b) for idx, a in enumerate(test_list) for b
in test_list[idx + 1:]]

 

# printing result 

print("All possible pairs : " + str(res))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    The original list : [1, 7, 4, 3]
    All possible pairs : [(1, 7), (1, 4), (1, 3), (7, 4), (7, 3), (4, 3)]
    

