Python | Value summation of key in dictionary



Many operations such as grouping and conversions are possible using Python
dictionaries. But sometimes, we can also have a problem in which we need to
perform the aggregation of values of key in dictionary list. This task is
common in day-day programming. Let’s discuss certain ways in which this task
can be performed.

 **Method #1 : Using sum() \+ list comprehension**

This is the one-liner approach to perform the task of getting the sum of
particular key while iterating to the similar keys in list of dictionaries
using list comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Value summation of key in dictionary

# Using sum() + list comprehension

 

# Initialize list

test_list = [{'gfg' : 1, 'is' : 2, 'best' : 3},

 {'gfg' : 7, 'is' : 3, 'best' : 5},

 {'gfg' : 9, 'is' : 8, 'best' : 6}] 

 

# printing original list

print("The original list is : " + str(test_list))

 

# Value summation of key in dictionary

# Using sum() + list comprehension

res = sum(sub['gfg'] for sub in test_list)

 

# printing result

print("The sum of particular key is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list is : [{‘best’: 3, ‘gfg’: 1, ‘is’: 2}, {‘best’: 5, ‘gfg’:
> 7, ‘is’: 3}, {‘best’: 6, ‘gfg’: 9, ‘is’: 8}]  
> The sum of particular key is : 17
>
>  
>
>
>  
>

**Method #2 : Usingsum() + itemgetter() + map()**  
The combination of these functions can also be used to perform this task. In
this, the main difference is that the comprehension task is done by map()
and the key access task is done by the itemgetter().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Value summation of key in dictionary

# Using sum() + itemgetter() + map()

import operator

 

# Initialize list

test_list = [{'gfg' : 1, 'is' : 2, 'best' : 3},

 {'gfg' : 7, 'is' : 3, 'best' : 5},

 {'gfg' : 9, 'is' : 8, 'best' : 6}] 

 

# printing original list

print("The original list is : " + str(test_list))

 

# Value summation of key in dictionary

# Using sum() + itemgetter() + map()

res = sum(map(operator.itemgetter('gfg'), test_list))

 

# printing result

print("The sum of particular key is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list is : [{‘best’: 3, ‘gfg’: 1, ‘is’: 2}, {‘best’: 5, ‘gfg’:
> 7, ‘is’: 3}, {‘best’: 6, ‘gfg’: 9, ‘is’: 8}]  
> The sum of particular key is : 17

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

