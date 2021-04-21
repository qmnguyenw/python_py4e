Python program to unique keys count for Value in Tuple List



Given dual tuples, get a count of unique keys for each value present in the
tuple.

>  **Input** : test_list = [(3, 4), (1, 2), (2, 4), (8, 2), (7, 2), (8, 1),
> (9, 1), (8, 4), (10, 4)]  
> **Output** : {4: 4, 2: 3, 1: 2}  
> **Explanation** : 3, 2, 8 and 10 are keys for value 4.
>
>  **Input** : test_list = [(3, 4), (1, 2), (8, 1), (9, 1), (8, 4), (10, 4)]  
> **Output** : {4: 3, 2: 1, 1: 2}  
> **Explanation** : 3, 8 and 10 are keys for value 4.  
>

**Method #1 : Using loop + defaultdict()**

In this, we iterate for each tuple element, having key as tuple value, and
increment it with each different key encountered in the dictionary value list.
Next, frequency is computed using another iteration by getting length of
mapped value list, converting to set to get a unique count.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Unique keys count for Value in Tuple List

# Using loop + defaultdict()

from collections import defaultdict

 

# initializing list

test_list = [(3, 4), (1, 2), (2, 4), (8,
2), (7, 2), (8, 1), (9, 1), (8, 4),
(10, 4)]

 

# printing original list

print("The original list is : " + str(test_list))

 

 

res = defaultdict(list)

for sub in test_list:

 

 # getting all keys to values

 res[sub[1]].append(sub[0])

 

 

res = dict(res)

 

 

res_dict = dict()

for key in res:

 

 # getting unique key counts for each value

 res_dict[key] = len(list(set(res[key])))

 

 

# printing result 

print("Unique keys for values : " + str(res_dict))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [(3, 4), (1, 2), (2, 4), (8, 2), (7, 2), (8, 1), (9,
> 1), (8, 4), (10, 4)]
>
> Unique keys for values : {4: 4, 2: 3, 1: 2}

 **Method #2 : Using loop + defaultdict() + Counter()**

In this, in order to reduce a computation loop, the list is constructed
dynamically having just unique values. Then Counter() is used to get unique
value dictionary.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# loop + defaultdict() + Counter()

# Using loop + defaultdict() + Counter()

from collections import defaultdict, Counter

 

# initializing list

test_list = [(3, 4), (1, 2), (2, 4), (8,
2), (7, 2),

 (8, 1), (9, 1), (8, 4), (10, 4)]

 

# printing original list

print("The original list is : " + str(test_list))

 

mem_dict = defaultdict(list)

res = []

for sub in test_list:

 

 # if not in dict, add value 

 if sub[0] not in mem_dict[sub[1]]:

 mem_dict[sub[1]].append(sub[0])

 res.append(sub[1])

 

# getting frequency 

res = dict(Counter(res))

 

# printing result 

print("Unique keys for values : " + str(res))  
  
---  
  
 __

 __

 **Output:**

The original list is : [(3, 4), (1, 2), (2, 4), (8, 2), (7, 2), (8, 1), (9,
1), (8, 4), (10, 4)]  
Unique keys for values : {4: 4, 2: 3, 1: 2}

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Unique keys count for Value in Tuple List

# Using loop + defaultdict()

from collections import defaultdict

 

# initializing list

test_list = [(3, 4), (1, 2), (2, 4), (8,
2), (7, 2), 

 (8, 1), (9, 1), (8, 4), (10, 4)]

 

# printing original list

print("The original list is : " + str(test_list))

 

 

res = defaultdict(list)

for sub in test_list:

 

 # getting all keys to values

 res[sub[1]].append(sub[0])

 

 

res = dict(res)

 

 

res_dict = dict()

for key in res:

 

 # getting unique key counts for each value

 res_dict[key] = len(list(set(res[key])))

 

 

# printing result 

print("Unique keys for values : " + str(res_dict))  
  
---  
  
 __

 __

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

