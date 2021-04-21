Python – Merge keys by values



Given a dictionary, merge the keys to map to common values.

 **Examples:**

>  **Input** : test_dict = {1:6, 8:1, 9:3, 10:3, 12:6, 4:9, 2:3}  
> **Output** : {‘1-12’: 6, ‘2-9-10’: 3, ‘4’: 9, ‘8’: 1}  
> **Explanation** : All the similar valued keys merged.
>
>  **Input** : test_dict = {1:6, 8:1, 9:3, 4:9, 2:3}  
> **Output** : {‘1’: 6, ‘2-9’: 3, ‘4’: 9, ‘8’: 1}  
> **Explanation** : All the similar valued keys merged.

**Approach : Using** **defauldict()** **\+ loop**

  

  

This task is performed in 2 steps, first, group all the values and storing
keys, and in 2nd step map merged keys to common values.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Merge keys by values

# Using defaultdict() + loop

from collections import defaultdict

 

# initializing dictionary

test_dict = {1: 6, 8: 1, 9: 3, 10: 3,
12: 6, 4: 9, 2: 3}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# grouping values

temp = defaultdict(list)

for key, val in sorted(test_dict.items()):

 temp[val].append(key)

 

res = dict()

# merge keys

for key in temp:

 res['-'.join([str(ele) for ele in temp[key]])] = key

 

# printing result

print("The required result : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original dictionary is : {1: 6, 8: 1, 9: 3, 10: 3, 12: 6, 4: 9, 2: 3}  
> The required result : {‘1-12’: 6, ‘2-9-10’: 3, ‘4’: 9, ‘8’: 1}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

