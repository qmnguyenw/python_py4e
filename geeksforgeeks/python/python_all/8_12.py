Python – Most common Combination in Matrix



Given a matrix, the task is to write a python program to extract the most
common occurrence of any combination of elements size greater than 2.

 **Examples:**

>  **Input:** test_list = [[4, 5, 6, 2], [7, 6, 3, 2], [4, 2, 6, 7], [1, 2, 4,
> 6]]
>
>  **Output:** [(2, 6)]
>
>  **Explanation:** [2, 6] in combination occurs 4 times, maximum of all.
>
>  
>
>
>  
>
>
> **Input:** test_list = [[4, 5, 6, 2], [7, 6, 3, 2], [4, 2, 6, 7], [1, 2, 4,
> 7]]
>
>  **Output:** [(2, 4), (2, 6), (2, 7)]
>
>  **Explanation:** [2, 6], [2, 4] and [2, 7] in combination occur 3 times
> each, maximum of all.

**Approach:** Using combinations() \+ Counter() \+ most_common() \+ list
comprehension

In this, combinations are computed using _combinations()_ , _Counter()_ ,
keeps track of frequencies of each combination. At last, _most_common()_ is
used to extract the maximum frequency of combinations occurred.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Most common Combination in Matrix

 

# import required modules

from collections import Counter

from itertools import combinations

 

# initializing list

test_list = [[4, 5, 6, 2], [7, 6, 3, 2],

 [4, 2, 6, 7], [1, 2, 4, 6]]

 

# printing original list

print("The original list is : " + str(test_list))

 

res = Counter()

for sub in test_list:

 

 # ignoring 1 sized substring

 if len(sub) < 2:

 continue

 

 # sorting for common ordering

 sub.sort()

 

 # getting and storing combinations

 for size in range(2, len(sub) + 1):

 for comb in combinations(sub, size):

 res[comb] += 1

 

# getting most common combinations

res = [cmb for cmb, 

 cnt in res.items() if cnt ==
res.most_common(1)[0][1]]

 

# printing result

print("The Most common combination : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [[4, 5, 6, 2], [7, 6, 3, 2], [4, 2, 6, 7], [1, 2, 4, 6]]
    The Most common combination : [(2, 6)]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

