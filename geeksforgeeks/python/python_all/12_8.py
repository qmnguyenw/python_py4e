Python program to get maximum of each key Dictionary List



Given list of dictionaries, write a Python program to get maximum of each key.

 **Examples:**

>  **Input** : test_list = [{“Gfg” : 8, “is” : 1, “Best” : 9}, {“Gfg” : 2,
> “is” : 9, “Best” : 1}, {“Gfg” : 5, “is” : 10, “Best” : 7}]  
> **Output** : {‘Gfg’: 8, ‘is’: 10, ‘Best’: 9}  
> **Explanation** : Maximum of Gfg key is 8 among possible 8, 2 and 5.
>
> **Input** : test_list = [{“Gfg” : 8, “is” : 1, “Best” : 9}, {“Gfg” : 5, “is”
> : 10, “Best” : 7}]  
> **Output** : {‘Gfg’: 8, ‘is’: 10, ‘Best’: 9}  
> **Explanation** : Maximum of Best key is 7 among possible 9, 7.

**Method #1 : Using** **items()** **\+ loop +** **max()**

  

  

In this, we iterate for each dictionary and keys in them using loop and keep
updating maximum values for each key using max().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# All Keys Maximum in Dictionary List

# Using items() + loop + max()

 

# initializing Matrix

test_list = [{"Gfg": 8, "is": 1, "Best": 9},

 {"Gfg": 2, "is": 9, "Best": 1},

 {"Gfg": 5, "is": 10, "Best": 7}]

 

# printing original list

print("The original list is : " + str(test_list))

 

 

res = {}

for dic in test_list:

 for key, val in dic.items():

 

 # checking for key presence and updating max

 if key in res:

 res[key] = max(res[key], val)

 else:

 res[key] = val

 

# printing result

print("All keys maximum : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [{‘Gfg’: 8, ‘is’: 1, ‘Best’: 9}, {‘Gfg’: 2, ‘is’: 9,
> ‘Best’: 1},  
> {‘Gfg’: 5, ‘is’: 10, ‘Best’: 7}]  
> All keys maximum : {‘Gfg’: 8, ‘is’: 10, ‘Best’: 9}The original list is :
> [{‘Gfg’: 8, ‘is’: 1, ‘Best’: 9},  
> {‘Gfg’: 2, ‘is’: 9, ‘Best’: 1}, {‘Gfg’: 5, ‘is’: 10, ‘Best’: 7}]  
> All keys maximum : {‘Gfg’: 8, ‘is’: 10, ‘Best’: 9}

 **Method #2 : Using** **defaultdict()**

In this, we omit step of conditional check for key existence by using
defaultdict(). Rest all the functionalities are similar to above method.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# All Keys Maximum in Dictionary List

# Using defaultdict()

from collections import defaultdict

 

# initializing Matrix

test_list = [{"Gfg": 8, "is": 1, "Best": 9},

 {"Gfg": 2, "is": 9, "Best": 1},

 {"Gfg": 5, "is": 10, "Best": 7}]

 

# printing original list

print("The original list is : " + str(test_list))

 

 

res = defaultdict(int)

for dic in test_list:

 for key, val in dic.items():

 

 # defaultdict helps to avoid conditional check here

 res[key] = max(res[key], val)

 

# printing result

print("All keys maximum : " + str(dict(res)))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [{‘Gfg’: 8, ‘is’: 1, ‘Best’: 9}, {‘Gfg’: 2, ‘is’: 9,
> ‘Best’: 1},  
> {‘Gfg’: 5, ‘is’: 10, ‘Best’: 7}]  
> All keys maximum : {‘Gfg’: 8, ‘is’: 10, ‘Best’: 9}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

