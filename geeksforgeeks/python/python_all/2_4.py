Python Program to Find Duplicate sets in list of sets



Given a list of sets, the task is to write a Python program to find duplicate
sets.

>  **Input :** test_list = [{4, 5, 6, 1}, {6, 4, 1, 5}, {1, 3, 4, 3}, {1, 4,
> 3}, {7, 8, 9}]
>
>  **Output :** [frozenset({1, 4, 5, 6}), frozenset({1, 3, 4})]
>
>  **Explanation :** {1, 4, 5, 6} is similar to {6, 4, 1, 5} hence part of
> result.
>
>  **Input :** test_list = [{4, 5, 6, 9}, {6, 4, 1, 5}, {1, 3, 4, 3}, {1, 4,
> 3}, {7, 8, 9}]
>
>  
>
>
>  
>
>
>  **Output :** [frozenset({1, 3, 4})]
>
>  **Explanation :** {1, 3, 4} ({1, 3, 4, 3}) is similar to {1, 4, 3} hence
> part of result.

 **Method #1 : Using** **Counter()** **\+ count() +** **frozenset()** **\+
loop**

In this, all the sets are hashed by converting them into frozenset() [ to get
hashable type ] into frequency using Counter(). Then count() is used to get
count of all the present sets from frequency counter created.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Duplicate sets in list of sets

# Using Counter() + count() + frozenset() + loop

from collections import Counter

 

# initializing list

test_list = [{4, 5, 6, 1}, {6, 4, 1, 5},
{1, 3, 4, 3}, 

 {1, 4, 3}, {7, 8, 9}]

 

# printing original list

print("The original list is : " + str(test_list))

 

# getting frequency using Counter()

freqs = Counter(frozenset(sub) for sub in test_list)

 

res = []

for key, val in freqs.items():

 

 # if frequency greater than 1, set is appended 

 # [duplicate]

 if val > 1 :

 res.append(key)

 

# printing result

print("Duplicate sets list : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [{1, 4, 5, 6}, {1, 4, 5, 6}, {1, 3, 4}, {1, 3, 4},
> {8, 9, 7}]
>
> Duplicate sets list : [frozenset({1, 4, 5, 6}), frozenset({1, 3, 4})]

 **Method #2 : Using** **list comprehension** **\+ Counter()**

In this, we perform similar task, only difference being list comprehension is
used as one liner to extract duplicates based on frequency dictionary.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Duplicate sets in list of sets

# Using list comprehension + Counter()

from collections import Counter

 

# initializing list

test_list = [{4, 5, 6, 1}, {6, 4, 1, 5},
{1, 3, 4, 3}, {1, 4, 3}, {7, 8, 9}]

 

# printing original list

print("The original list is : " + str(test_list))

 

# getting frequency using Counter()

freqs = Counter(frozenset(sub) for sub in test_list)

 

# list comprehension provides shorthand solution

res = [key for key, val in freqs.items() if val > 1]

 

# printing result

print("Duplicate sets list : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [{1, 4, 5, 6}, {1, 4, 5, 6}, {1, 3, 4}, {1, 3, 4},
> {8, 9, 7}]
>
> Duplicate sets list : [frozenset({1, 4, 5, 6}), frozenset({1, 3, 4})]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

