Python program that renders a dictionary from two list with K values



Given two list, one will be used to provide keys to dictionary and the other
for values. The following program takes K values from second list and assigns
it to each key, creating a dictionary of the following kind:

>  **Input** : test_list = [“gfg”, “best”], val_list = [1, 4, 5, 6, 7, 8, 8,
> 5], K = 4  
> **Output** : {‘gfg’: [1, 4, 5, 6], ‘best’: [7, 8, 8, 5]}  
> **Explanation** : Equal elements paired to each key.  
>  **Input** : test_list = [“gfg”], val_list = [1, 4, 5, 6], K = 4  
> **Output** : {‘gfg’: [1, 4, 5, 6]}  
> **Explanation** : All elements assigned to only key.

**Method :** _Using_ _loop_ _and_ _slicing_ __

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from collections import defaultdict

 

# initializing list

test_list = ["gfg", "is", "best", "good"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing values list 

val_list = [1, 4, 5, 6, 7, 8, 8, 5,
4]

 

# initializing K 

K = 2

 

# work list

val_list = val_list[:(len(test_list) * K)]

 

# gets requried dictionary list 

res = defaultdict(list)

key_cnt = 0

for idx in range(0, len(val_list)):

 

 # append values to required keys 

 res[test_list[key_cnt]].append(val_list[idx])

 

 # increment keys when K

 if (idx + 1) % K == 0:

 key_cnt += 1

 

# printing result 

print("The constructed dictionary : " + str(dict(res)))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [‘gfg’, ‘is’, ‘best’, ‘good’]
>
>  
>
>
>  
>
>
> The constructed dictionary : {‘gfg’: [1, 4], ‘is’: [5, 6], ‘best’: [7, 8],
> ‘good’: [8, 5]}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

