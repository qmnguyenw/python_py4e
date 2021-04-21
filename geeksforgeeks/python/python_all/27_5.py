Python program to extract the Unique Dictionary Value List elements



Given Dictionary with value lists, extract all unique values.

> **Input** : test_dict = {“Gfg” : [6, 7, 4, 6], “Geeks” : [6, 8, 5, 2]}  
> **Output** : [6, 7, 4, 8, 5, 2]  
> **Explanation** : All distincts elements extracted.
>
>  **Input** : test_dict = {“Gfg” : [6, 7, 6], “Geeks” : [6, 8, 5, 2]}  
> **Output** : [6, 7, 8, 5, 2]  
> **Explanation** : All distincts elements extracted.

**Method #1 : Using loop**

This is brute way in which this task can be performed. In this, we memoize
elements when they occur and prevent them from re enter to result list.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Unique Dictionary Value List elements

# Using loop

 

# initializing dictionary

test_dict = {"Gfg" : [6, 7, 4, 6], 

 "is" : [8, 9, 5], 

 "for" : [2, 5, 3, 7], 

 "Geeks" : [6, 8, 5, 2]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# list to memorize elements and insert result

res = []

for sub in test_dict:

 for ele in test_dict[sub]:

 

 # testing for existence

 if ele not in res:

 res.append(ele)

 

# printing result 

print("Extracted items : " + str(res))   
  
---  
  
__

__

**Output:**

> The original dictionary is : {‘Gfg’: [6, 7, 4, 6], ‘is’: [8, 9, 5], ‘for’:
> [2, 5, 3, 7], ‘Geeks’: [6, 8, 5, 2]}
>
> Extracted items : [6, 7, 4, 8, 9, 5, 2, 3]

 **Method #2 : Using** **set()** **+** **union()**

The combination of the above functions can be used to solve this problem. In
this, we convert all lists using set() and then perform a union of all
elements across all keys to get the desired result.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Unique Dictionary Value List elements

# Using set() + union()

 

# initializing dictionary

test_dict = {"Gfg" : [6, 7, 4, 6], 

 "is" : [8, 9, 5], 

 "for" : [2, 5, 3, 7], 

 "Geeks" : [6, 8, 5, 2]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# using * operator to get union 

res = list(set().union(*test_dict.values()))

 

# printing result 

print("Extracted items : " + str(res))   
  
---  
  
__

__

**Output:**

> The original dictionary is : {‘Gfg’: [6, 7, 4, 6], ‘is’: [8, 9, 5], ‘for’:
> [2, 5, 3, 7], ‘Geeks’: [6, 8, 5, 2]}
>
> Extracted items : [6, 7, 4, 8, 9, 5, 2, 3

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

