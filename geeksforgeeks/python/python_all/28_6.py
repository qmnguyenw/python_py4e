Python – Find occurrences for each value of a particular key



Given a List of dictionaries, for a particular key, find the number of
occurrences for each value of that key.

>  **Input** : test_list = [{‘gfg’ : 3, ‘best’ : 4}, {‘gfg’ : 3, ‘best’ : 5},  
> {‘gfg’ : 4, ‘best’ : 4}, {‘gfg’ : 7, ‘best’ : 4} ], K = ‘gfg’  
> **Output** : [{3: 2}, {4: 1}, {7: 1}]  
> **Explanation** : gfg has 2 occurrences of 3 as values.
>
>  **Input** : test_list = [{‘gfg’ : 3, ‘best’ : 4}, {‘gfg’ : 3, ‘best’ : 5},  
> {‘gfg’ : 4, ‘best’ : 4}, {‘gfg’ : 7, ‘best’ : 4} ], K = ‘best’  
> **Output** : [{4: 3}, {5: 1}]  
> **Explanation** : best has 3 occurrences of 4 as values.

 **Method #1 : Using** **groupby()** **\+ dictionary comprehension**

In this, we perform grouping of key’s values using groupby() and values
frequency is assembled and extracted using dictionary comprehension and len().

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Values Frequency grouping of K in dictionaries

# Using groupby() + dictionary comprehension

from itertools import groupby

 

# initializing list

test_list = [{'gfg' : 3, 'best' : 4}, {'gfg' : 3,
'best' : 5}, 

 {'gfg' : 4, 'best' : 4}, {'gfg' : 7, 'best' :
4} ]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 'gfg'

 

# groupby() used to group values and len() to compute Frequency

res = [{key: len(list(val))} for key, val in
groupby(test_list, lambda sub: sub[K])]

 

# printing result 

print("The Values Frequency : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [{‘gfg’: 3, ‘best’: 4}, {‘gfg’: 3, ‘best’: 5},
> {‘gfg’: 4, ‘best’: 4},  
> {‘gfg’: 7, ‘best’: 4}]  
> The Values Frequency : [{3: 2}, {4: 1}, {7: 1}]

 **Method #2 : Using** **Counter()**

In this, the task of performing frequency check is done using Counter().
Returns result in single dictionary.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Values Frequency grouping of K in dictionaries

# Using Counter()

from collections import Counter

 

# initializing list

test_list = [{'gfg' : 3, 'best' : 4}, {'gfg' : 3,
'best' : 5}, 

 {'gfg' : 4, 'best' : 4}, {'gfg' : 7, 'best' :
4} ]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 'gfg'

 

# groupby() used to group values and len() to compute Frequency

res = dict(Counter(sub[K] for sub in test_list))

 

# printing result 

print("The Values Frequency : " + str(res))  
  
---  
  
 __

 __

**Output:**

> The original list is : [{‘gfg’: 3, ‘best’: 4}, {‘gfg’: 3, ‘best’: 5},
> {‘gfg’: 4, ‘best’: 4},  
> {‘gfg’: 7, ‘best’: 4}]  
> The Values Frequency : [{3: 2}, {4: 1}, {7: 1}]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

