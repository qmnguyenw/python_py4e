Python – All combination Dictionary List



Given 2 lists, form all possible combination of dictionaries that can be
formed by taking keys from list1 and values from list2.

>  **Input** : test_list1 = [“Gfg”, “is”, “Best”], test_list2 = [4]  
> **Output** : [{‘Gfg’: 4, ‘is’: 4, ‘Best’: 4}]  
>  **Explanation** : All combinations dictionary list extracted.  
>
>
> **Input** : test_list1 = [“Gfg”, “is”, “Best”], test_list2 = [5, 6]  
> **Output** : [{‘Gfg’: 5, ‘is’: 5, ‘Best’: 5}, {‘Gfg’: 5, ‘is’: 5, ‘Best’:
> 6}, {‘Gfg’: 5, ‘is’: 6, ‘Best’: 5}, {‘Gfg’: 5, ‘is’: 6, ‘Best’: 6}, {‘Gfg’:
> 6, ‘is’: 5, ‘Best’: 5}, {‘Gfg’: 6, ‘is’: 5, ‘Best’: 6}, {‘Gfg’: 6, ‘is’: 6,
> ‘Best’: 5}, {‘Gfg’: 6, ‘is’: 6, ‘Best’: 6}]  
> **Explanation** : All combinations dictionary list extracted.  
>

**Method #1 : Using product() + dictionary comprehension + list
comprehension**

In this, we get all the combination possible using product() and dictionary
comprehension generates each dictionary, list comprehension is used to iterate
combinations generated.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# All combination Dictionary List

# Using product() + list comprehension + dictionary comprehension

from itertools import product

 

# initializing lists

test_list1 = ["Gfg", "is", "Best"]

test_list2 = [4, 5]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# generating combinations

temp = product(test_list2, repeat = len(test_list1))

 

# constructing dicts using combinations

res = [{key : val for (key , val) in zip(test_list1, ele)}
for ele in temp]

 

# printing result 

print("The combinations dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list 1 is : [‘Gfg’, ‘is’, ‘Best’]  
> The original list 2 is : [4, 5]  
> The combinations dictionary : [{‘Gfg’: 4, ‘is’: 4, ‘Best’: 4}, {‘Gfg’: 4,
> ‘is’: 4, ‘Best’: 5}, {‘Gfg’: 4, ‘is’: 5, ‘Best’: 4}, {‘Gfg’: 4, ‘is’: 5,
> ‘Best’: 5}, {‘Gfg’: 5, ‘is’: 4, ‘Best’: 4}, {‘Gfg’: 5, ‘is’: 4, ‘Best’: 5},
> {‘Gfg’: 5, ‘is’: 5, ‘Best’: 4}, {‘Gfg’: 5, ‘is’: 5, ‘Best’: 5}]

 **Method #2 : Using permutations() + dictionary comprehension + list
comprehension [ For unique elements ]**

If we require values to be all unique, permutations() can be used inplace of
product() to achieve this task.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# All combination Dictionary List

# Using product() + list comprehension + dictionary comprehension

from itertools import permutations

 

# initializing lists

test_list1 = ["Gfg", "is", "Best"]

test_list2 = [4, 5, 6]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# generating combinations

temp = list(permutations(test_list2, len(test_list1)))

 

# constructing dicts using combinations

res = [{key: val for (key, val) in zip(test_list1, ele)} for
ele in temp]

 

# printing result

print("The combinations dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list 1 is : [‘Gfg’, ‘is’, ‘Best’]  
> The original list 2 is : [4, 5, 6]  
> The combinations dictionary : [{‘Gfg’: 4, ‘is’: 5, ‘Best’: 6}, {‘Gfg’: 4,
> ‘is’: 6, ‘Best’: 5}, {‘Gfg’: 5, ‘is’: 4, ‘Best’: 6}, {‘Gfg’: 5, ‘is’: 6,
> ‘Best’: 4}, {‘Gfg’: 6, ‘is’: 4, ‘Best’: 5}, {‘Gfg’: 6, ‘is’: 5, ‘Best’: 4}]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

