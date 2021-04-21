Python – Create dictionary from the list



Given a list. The task is to convert it to a dictionary with the values as the
list element and keys as the concatenation of the given string K and value.

 **Examples:**

>  **Input** : test_list = [“gfg”, “is”, “best”], K = “pref_”  
> **Output** : {‘pref_gfg’: ‘gfg’, ‘pref_is’: ‘is’, ‘pref_best’: ‘best’}  
> **Explanation** : Keys constructed after concatenating K.
>
>  **Input** : test_list = [“gfg”, “best”], K = “pref_”  
> **Output** : {‘pref_gfg’: ‘gfg’, ‘pref_best’: ‘best’}  
> **Explanation** : Keys constructed after concatenating K.

**Method #1: Using loop**

  

  

This is one of the ways in which this task can be performed. In this, we
perform concatenation using + operator to construct keys and values are
extracted from list.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Values derived Dictionary keys

# Using loop

 

# initializing list

test_list = ["gfg", "is", "best"] 

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = "def_key_"

 

# using loop to construct new Dictionary

# + operator used to concat default key and values 

res = dict()

for ele in test_list:

 res[K + str(ele)] = ele 

 

# printing result 

print("The constructed Dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [‘gfg’, ‘is’, ‘best’]  
> The constructed Dictionary : {‘def_key_gfg’: ‘gfg’, ‘def_key_is’: ‘is’,
> ‘def_key_best’: ‘best’}

 **Method #2: Using** **dictionary comprehension**

This is yet another way in which this task can be performed. In this, we
construct a dictionary using one-liner using dictionary comprehension.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Values derived Dictionary keys

# Using dictionary comprehension

 

# initializing list

test_list = ["gfg", "is", "best"] 

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = "def_key_"

 

# using dictionary comprehension

# + operator used to concat default key and values 

res = {K + str(ele) : ele for ele in test_list}

 

# printing result 

print("The constructed Dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [‘gfg’, ‘is’, ‘best’]  
> The constructed Dictionary : {‘def_key_gfg’: ‘gfg’, ‘def_key_is’: ‘is’,
> ‘def_key_best’: ‘best’}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

