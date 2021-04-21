Python – Extract tuple supersets from List



Sometimes, while working with Python tuples, we can have a problem in which we
need to extract all the tuples, which have all the elements in target tuple.
This problem can have application in domains such as web development. Let’s
discuss certain way in which this problem can be solved.

>  **Input** :  
> test_list = [(5, 6, 6), (4, 2, 7), (9, 6, 5, 6)]  
> test_tuple = (6, 6)  
>  **Output** : [(5, 6, 6), (9, 6, 5, 6)]
>
>  **Input** :  
> test_list = [(5, 6, 6), (4, 2, 6), (9, 6, 5, 6)]  
> test_tuple = (6, )  
>  **Output** : [(5, 6, 6), (4, 2, 6), (9, 6, 5, 6)]

 **Method : UsingCounter() + list comprehension + all()**  
The combination of above functions can be used to solve this problem. In this,
we perform the task of counting using Counter(). The all(), is used to check
if all elements form the subset and list comprehension is used to bind all the
logic in one block.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract tuple supersets from List

# Using all() + list comprehension + Counter

from collections import Counter

 

# initializing list

test_list = [(5, 6, 8), (4, 2, 7), (9, 6,
5, 6)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing tuple

test_tup = (6, 6, 5)

 

# Extract tuple supersets from List

# Using all() + list comprehension + Counter

res = [sub for sub in test_list if

 all(Counter(sub)[x] >= Counter(test_tup)[x]

 for x in Counter(test_tup))]

 

# printing result 

print("The superset tuples : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list is : [(5, 6, 8), (4, 2, 7), (9, 6, 5, 6)]
    The superset tuples : [(9, 6, 5, 6)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

