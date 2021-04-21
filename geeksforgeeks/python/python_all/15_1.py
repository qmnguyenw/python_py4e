Python – Value limits to keys in Dictionaries List



Given a Dictionaries list, write a Python program to assign limits to each key
in dictionary list.( each having all keys ).

 **Examples:**

>  **Input** : test_list = [{“gfg” : 4, “is” : 7, “best” : 10}, {“gfg” : 2,
> “is” : 5, “best” : 9}, {“gfg” : 1, “is” : 2, “best” : 6}]  
> **Output** : {‘gfg’: [1, 4], ‘is’: [2, 7], ‘best’: [6, 10]}  
> **Explanation** : gfg has min. value to be 1 and maximum to be 4.  
>
>
> **Input** : test_list = [{“gfg” : 4, “best” : 10}, {“gfg” : 2, “best” : 9},
> {“gfg” : 1, “best” : 6}]  
> **Output** : {‘gfg’: [1, 4], ‘best’: [6, 10]}  
> **Explanation** : best has min. value to be 6 and maximum to be 10.

**Method #1 : Using** **max()** **+** **min()** **\+ loop +** **keys()**

  

  

In this, we perform task of getting all keys using keys(), and min and max
values for limits are computed using min() and max(). The iteration of all the
dictionaries is carried out using loop.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Value limits to keys in Dictionaries List

# Using max() + min() + loop + keys()

 

# initializing Matrix

test_list = [{"gfg": 4, "is": 7, "best": 10},

 {"gfg": 2, "is": 5, "best": 9},

 {"gfg": 1, "is": 2, "best": 6}]

 

# printing original list

print("The original list is : " + str(test_list))

 

res = dict()

 

# extraction of all keys

keys = list(test_list[0].keys())

 

for key in keys:

 

 # assigning ranges to each key

 res[key] = [min(sub[key] for sub in test_list),
max(sub[key]

 for sub in test_list)]

 

# printing result

print("Keys Ranges : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [{‘gfg’: 4, ‘is’: 7, ‘best’: 10}, {‘gfg’: 2, ‘is’: 5,
> ‘best’: 9}, {‘gfg’: 1, ‘is’: 2, ‘best’: 6}]  
> Keys Ranges : {‘gfg’: [1, 4], ‘is’: [2, 7], ‘best’: [6, 10]}

 **Method #2 : Using** **dictionary comprehension** **\+ min() + max() +**
**keys()**

In this, we perform task of iteration using one liner dictionary
comprehension, just similar method as above method but a shorthand.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Value limits to keys in Dictionaries List

# Using list comprehension + min() + max() + keys()

 

# initializing Matrix

test_list = [{"gfg": 4, "is": 7, "best": 10},

 {"gfg": 2, "is": 5, "best": 9},

 {"gfg": 1, "is": 2, "best": 6}]

 

# printing original list

print("The original list is : " + str(test_list))

 

# extraction of all keys

keys = list(test_list[0].keys())

 

# Dictionary comprehension used as one liner to perform task

res = {key: [min(sub[key] for sub in test_list),
max(sub[key]

 for sub in test_list)] for key in keys}

 

# printing result

print("Keys Ranges : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [{‘gfg’: 4, ‘is’: 7, ‘best’: 10}, {‘gfg’: 2, ‘is’: 5,
> ‘best’: 9}, {‘gfg’: 1, ‘is’: 2, ‘best’: 6}]  
> Keys Ranges : {‘gfg’: [1, 4], ‘is’: [2, 7], ‘best’: [6, 10]}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

