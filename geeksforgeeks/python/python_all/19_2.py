Python – Reorder for consecutive elements



Given a List perform reordering to get similar elements in consecution.

>  **Input** : test_list = [4, 7, 5, 4, 1, 4, 1, 6, 7, 5]  
> **Output** : [4, 4, 4, 7, 7, 5, 5, 1, 1, 6]  
> **Explanation** : All similar elements are assigned to be consecutive.
>
>  **Input** : test_list = [4, 7, 5, 1, 4, 1, 6, 7, 5]  
> **Output** : [4, 4, 7, 7, 5, 5, 1, 1, 6]  
> **Explanation** : All similar elements are assigned to be consecutive.  
>

**Method #1 : Using Counter() + loop + items()**

In this, we perform the task of computing frequency using Counter(), and loop
and items() are used to reorder elements according to count, and access
frequencies respectively.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Reorder for consecutive elements

# Using Counter() + loop + items()

from collections import Counter

 

# initializing list

test_list = [4, 7, 5, 4, 1, 4, 1, 6,
7, 5]

 

# printing original lists

print("The original list is : " + str(test_list))

 

# getting frequency

freqs = Counter(test_list)

res = []

 

# reordering basis of frequency

for val, cnt in freqs.items():

 res.extend([val]*cnt)

 

# printing result 

print("Reordered List : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [4, 7, 5, 4, 1, 4, 1, 6, 7, 5]
    Reordered List : [4, 4, 4, 7, 7, 5, 5, 1, 1, 6]
    

**Method #2 : Using Counter() + elements()**

In this, we perform the task of reordering the counted frequencies using
elements(), providing a concise solution.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Reorder for consecutive elements

# Using Counter() + elements()

from collections import Counter

 

# initializing list

test_list = [4, 7, 5, 4, 1, 4, 1, 6,
7, 5]

 

# printing original lists

print("The original list is : " + str(test_list))

 

# reordering using elements()

res = list(Counter(test_list).elements())

 

# printing result 

print("Reordered List : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [4, 7, 5, 4, 1, 4, 1, 6, 7, 5]
    Reordered List : [4, 4, 4, 7, 7, 5, 5, 1, 1, 6]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

