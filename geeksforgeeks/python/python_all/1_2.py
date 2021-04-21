Python – Cumulative Mean of Dictionary keys



Given the dictionary list, our task is to write a Python Program to extract
the mean of all keys.

> **Input :** test_list = [{‘gfg’ : 34, ‘is’ : 8, ‘best’ : 10},
>
> {‘gfg’ : 1, ‘for’ : 10, ‘geeks’ : 9, ‘and’ : 5, ‘best’ : 12},
>
> {‘geeks’ : 8, ‘find’ : 3, ‘gfg’ : 3, ‘best’ : 8}]
>
>  **Output :** {‘gfg’: 12.666666666666666, ‘is’: 8, ‘best’: 10, ‘for’: 10,
> ‘geeks’: 8.5, ‘and’: 5, ‘find’: 3}
>
>  
>
>
>  
>
>
>  **Explanation :** best has 3 values, 10, 8 and 12, their mean computed to
> 10, hence in result.
>
>  **Input :** test_list = [{‘gfg’ : 34, ‘is’ : 8, ‘best’ : 10},
>
> {‘gfg’ : 1, ‘for’ : 10, ‘and’ : 5, ‘best’ : 12},
>
> { ‘find’ : 3, ‘gfg’ : 3, ‘best’ : 8}]
>
>  **Output :** {‘gfg’: 12.666666666666666, ‘is’: 8, ‘best’: 10, ‘for’: 10,
> ‘and’: 5, ‘find’: 3}
>
>  **Explanation :** best has 3 values, 10, 8 and 12, their mean computed to
> 10, hence in result.

 **Method #1 : Using** **mean()** **+** **loop** ****

In this, for extracting each list loop is used and all the values are summed
and memorized using a dictionary. Mean is extracted later by dividing by the
occurrence of each key.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Cumulative Keys Mean in Dictionary List

# Using loop + mean()

from statistics import mean

 

# initializing list

test_list = [{'gfg' : 34, 'is' : 8, 'best' :
10},

 {'gfg' : 1, 'for' : 10, 'geeks' : 9, 'and' :
5, 'best' : 12},

 {'geeks' : 8, 'find' : 3, 'gfg' : 3, 'best' :
8}]

 

# printing original list

print("The original list is : " + str(test_list))

 

res = dict()

for sub in test_list:

 for key, val in sub.items():

 if key in res:

 

 # combining each key to all values in

 # all dictionaries

 res[key].append(val)

 else:

 res[key] = [val]

 

for key, num_l in res.items():

 res[key] = mean(num_l)

 

# printing result

print("The Extracted average : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [{‘gfg’: 34, ‘is’: 8, ‘best’: 10}, {‘gfg’: 1, ‘for’:
> 10, ‘geeks’: 9, ‘and’: 5, ‘best’: 12}, {‘geeks’: 8, ‘find’: 3, ‘gfg’: 3,
> ‘best’: 8}]
>
> The Extracted average : {‘gfg’: 12.666666666666666, ‘is’: 8, ‘best’: 10,
> ‘for’: 10, ‘geeks’: 8.5, ‘and’: 5, ‘find’: 3}

 **Method #2 : Using** **defaultdict()** **\+ mean()**

In this, the task of memorizing is done using defaultdict(). This reduces one
conditional check and makes the code more concise.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Cumulative Keys Mean in Dictionary List

# Using defaultdict() + mean()

from statistics import mean

from collections import defaultdict

 

# initializing list

test_list = [{'gfg' : 34, 'is' : 8, 'best' :
10},

 {'gfg' : 1, 'for' : 10, 'geeks' : 9, 'and' :
5, 'best' : 12},

 {'geeks' : 8, 'find' : 3, 'gfg' : 3, 'best' :
8}]

 

# printing original list

print("The original list is : " + str(test_list))

 

# defaultdict reduces step to memoize.

res = defaultdict(list)

for sub in test_list:

 for key, val in sub.items():

 res[key].append(val)

 

res = dict(res)

for key, num_l in res.items():

 

 # computing mean

 res[key] = mean(num_l)

 

# printing result

print("The Extracted average : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [{‘gfg’: 34, ‘is’: 8, ‘best’: 10}, {‘gfg’: 1, ‘for’:
> 10, ‘geeks’: 9, ‘and’: 5, ‘best’: 12}, {‘geeks’: 8, ‘find’: 3, ‘gfg’: 3,
> ‘best’: 8}]
>
> The Extracted average : {‘gfg’: 12.666666666666666, ‘is’: 8, ‘best’: 10,
> ‘for’: 10, ‘geeks’: 8.5, ‘and’: 5, ‘find’: 3}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

