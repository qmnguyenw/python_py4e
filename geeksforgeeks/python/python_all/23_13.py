Python – Remove Dictionaries with Matching Values with K Key



Given two dictionary lists, remove all the dictionaries which have similar
value of K key from other dictionary list.

>  **Input** : test_list = [{‘Gfg’ : 3, “is” : 3, “best” : 9},  
> {‘Gfg’ : 8, “is” : 4, “best” : 2},  
> {‘Gfg’ : 9, “is” : 2, “best” : 4},  
> {‘Gfg’ : 8, “is” : 10, “best” : 3},  
> {‘Gfg’ : 7, “is” : 1, “best” : 7}], check_list = [{‘Gfg’ : 8, “Best” : 1},
> {“Best” : 2, “Gfg” : 7}], K = “Gfg”  
> **Output** : [{‘Gfg’: 3, ‘is’: 3, ‘best’: 9}, {‘Gfg’: 9, ‘is’: 10, ‘best’:
> 3}]  
> **Explanation** : All dictionaries with “Gfg”‘s value as 8 or 7 is removed.  
>
>
> **Input** : test_list = [{‘Gfg’ : 3, “is” : 3, “best” : 9},  
> {‘Gfg’ : 8, “is” : 4, “best” : 2}], check_list = [{‘Gfg’ : 8, “Best” : 1},
> {“Best” : 2, “Gfg” : 7}], K = “Gfg”  
> **Output** : [{‘Gfg’: 3, ‘is’: 3, ‘best’: 9}]  
> **Explanation** : All dictionaries with “Gfg”‘s value as 8 or 7 is removed.

**Approach: Using list comprehension + dictionary comprehension**

In this, we perform tasks of getting a set of elements using dictionary
comprehension, and then a new list is constructed using list comprehension by
testing K key’s values absence in the constructed set of values.

  

  

The whole task is conducted in two steps,

  * All the unique values are extracted from _check_list_ corresponding to key _K_ using _set()_.
  * Each dictionary in test list is checked for key _K_ ‘s value, if it is present in set created in first step, then that dictionary is omitted in result, else dictionary is added as result.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove Dictionaries with Matching Values with K Key

# Using dictionary comprehension + list comprehension

 

# initializing list

test_list = [{'Gfg': 3, "is": 3, "best": 9},

 {'Gfg': 8, "is": 4, "best": 2},

 {'Gfg': 1, "is": 2, "best": 4},

 {'Gfg': 9, "is": 10, "best": 3},

 {'Gfg': 7, "is": 1, "best": 7}]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing check dictionary list

check_list = [{'Gfg': 8, "Best": 1}, {"Best": 2,
"Gfg": 7}]

 

# initializing Key

K = "Gfg"

 

# getting set of values

temp = {sub[K] for sub in check_list}

 

# checking for value occurrence in test dictionary using in

# filtering only with no matching values

res = [sub for sub in test_list if sub[K] not in temp]

 

# printing result

print("Dictionary list after removal : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [{‘Gfg’: 3, ‘is’: 3, ‘best’: 9}, {‘Gfg’: 8, ‘is’: 4,
> ‘best’: 2}, {‘Gfg’: 1, ‘is’: 2, ‘best’: 4}, {‘Gfg’: 9, ‘is’: 10, ‘best’: 3},
> {‘Gfg’: 7, ‘is’: 1, ‘best’: 7}]  
> Dictionary list after removal : [{‘Gfg’: 3, ‘is’: 3, ‘best’: 9}, {‘Gfg’: 1,
> ‘is’: 2, ‘best’: 4}, {‘Gfg’: 9, ‘is’: 10, ‘best’: 3}]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

