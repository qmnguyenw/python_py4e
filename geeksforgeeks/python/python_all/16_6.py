Python Program to Group Strings by K length Using Suffix



Given Strings List, the task is to write a Python program to group them into K
length suffix.

>  **Input** : test_list = [“food”, “peak”, “geek”, “good”, “weak”, “sneek”],
> K = 3  
> **Output** : {‘ood’: [‘food’, ‘good’], ‘eak’: [‘peak’, ‘weak’], ‘eek’:
> [‘geek’, ‘sneek’]}  
> **Explanation** : words ending with ood are food and good, hence grouped.
>
>  **Input** : test_list = [“peak”, “geek”, “good”, “weak”], K = 3  
> **Output** : {‘ood’: [‘good’], ‘eak’: [‘peak’, ‘weak’], ‘eek’: [‘geek’]}  
> **Explanation** : word ending with ood is good, hence grouped.  
>

**Method 1 :** Using try/except \+ loop

In this, we extract the last K characters and form a string, and append to the
existing key’s list corresponding to it, if not found, it goes through catch
flow and creates a new key with a list with first word initialized.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Group Strings by K length Suffix

# Using try/except + loop

 

# initializing list

test_list = ["food", "peak", "geek",

 "good", "weak", "sneek"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 3

 

res = {}

for ele in test_list:

 

 # extracting suffix

 suff = ele[-K : ]

 

 # appending if key found, else creating new one

 try: 

 res[suff].append(ele)

 except:

 res[suff] = [ele]

 

# printing result 

print("The grouped suffix Strings : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [‘food’, ‘peak’, ‘geek’, ‘good’, ‘weak’, ‘sneek’]  
> The grouped suffix Strings : {‘ood’: [‘food’, ‘good’], ‘eak’: [‘peak’,
> ‘weak’], ‘eek’: [‘geek’, ‘sneek’]}

 **Method 2 :** Using defaultdict() \+ loop.

This method avoids the need of using try/except block as default list
initialization is handled by defaultdict().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Group Strings by K length Suffix

# Using defaultdict() + loop

from collections import defaultdict

 

# initializing list

test_list = ["food", "peak", "geek",

 "good", "weak", "sneek"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 3

 

res = defaultdict(list)

for ele in test_list:

 

 # extracting suffix

 suff = ele[-K : ]

 

 # appending into matched suffix key

 res[suff].append(ele)

 

# printing result 

print("The grouped suffix Strings : " + str(dict(res)))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [‘food’, ‘peak’, ‘geek’, ‘good’, ‘weak’, ‘sneek’]  
> The grouped suffix Strings : {‘ood’: [‘food’, ‘good’], ‘eak’: [‘peak’,
> ‘weak’], ‘eek’: [‘geek’, ‘sneek’]}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

