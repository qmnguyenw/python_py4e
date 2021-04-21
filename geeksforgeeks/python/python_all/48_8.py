Python – Group single item dictionaries into List values



Given List of single item dictionaries, group them into dictionary value lists
according to similar values.

> **Input** : [{“Gfg” : 3}, {“is”: 8}, {“Gfg”: 18}, {“Best”: 33}]  
>  **Output** : {‘Gfg’: [3, 18], ‘is’: [8], ‘Best’: [33]}  
>  **Explanation** : Each key converted to list values and dictionary.
>
>  **Input** : [{“Gfg” : 3}, {“Gfg”: 8}, {“Gfg”: 18}, {“Best”: 33}]  
>  **Output** : {‘Gfg’: [3, 18, 8], ‘Best’: [33]}  
>  **Explanation** : Each key converted to list values and dictionary.

 **Method #1 : Using setdefault() + loop**

This is brute way in which this task can be performed. In this, we use to loop
through all the dictionary values and setdefault() is used to assign common
key its corresponding grouped value lists.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Group single item dictionaries into List values

# Using setdefault() + loop

 

# initializing lists

test_list = [{"Gfg" : 3}, {"is": 8}, {"Best":
10}, {"Gfg": 18}, {"Best": 33}]

 

# printing original list

print("The original list : " + str(test_list))

 

res = {}

 

# using loop to loop through each dictionary

for idx in test_list:

 

 # items() to extract item

 for key, val in idx.items():

 

 # setdefault performs task of setting empty list value as default

 res.setdefault(key, []).append(val)

 

# printing result 

print("The constructed dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [{'Gfg': 3}, {'is': 8}, {'Best': 10}, {'Gfg': 18}, {'Best': 33}]
    The constructed dictionary : {'Gfg': [3, 18], 'is': [8], 'Best': [10, 33]}
    

**Method #2 : Using defaultdict() + * operator + loop**

This is yet another way in which this task can be performed. In this, we use
defaultdict() for empty list initialization. The * operator is used to unpack
the dictionary item and loop is used to loop through dictionaries.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Group single item dictionaries into List values

# Using defaultdict() + * operator + loop

from collections import defaultdict

 

# initializing lists

test_list = [{"Gfg" : 3}, {"is": 8}, {"Best":
10}, {"Gfg": 18}, {"Best": 33}]

 

# printing original list

print("The original list : " + str(test_list))

 

res = defaultdict(list)

for ele in test_list:

 

 # using * operator to unpack

 # reducing one loop

 key, val = tuple(*ele.items())

 res[key].append(val)

 

# printing result 

print("The constructed dictionary : " + str(dict(res)))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [{'Gfg': 3}, {'is': 8}, {'Best': 10}, {'Gfg': 18}, {'Best': 33}]
    The constructed dictionary : {'Gfg': [3, 18], 'is': [8], 'Best': [10, 33]}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

