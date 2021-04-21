Python – Filter rows without Space Strings



Given Matrix, extract rows in which Strings don’t have spaces.

 **Examples:**

>  **Input** : test_list = [[“gfg is”, “best”], [“gfg”, “good”], [“gfg is
> cool”], [“love”, “gfg”]]  
> **Output** : [[‘gfg’, ‘good’], [‘love’, ‘gfg’]]  
> **Explanation** : Both the lists have strings don’t have spaces.  
>
>
> **Input** : test_list = [[“gfg is”, “best”], [“gfg “, “good”], [“gfg is
> cool”], [“love”, “gfg”]]  
> **Output** : [[‘love’, ‘gfg’]]  
> **Explanation** : List has strings don’t have spaces.

**Method #1: Using** **list comprehension** **+** **any()** **+** **regex**

  

  

In this, we check for no space in each string using regex, any() is used to
check this for any string found with spaces, that row is not added.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Filter rows without Space Strings

# Using list comprehension + any() + regex

import re

 

# initializing list

test_list = [["gfg is", "best"], ["gfg", "good"],

 ["gfg is cool"], ["love", "gfg"]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# checking for spaces using regex

# not including row if any string has space

res = [row for row in test_list if not any(

 bool(re.search(r"\s", ele)) for ele in row)]

 

# printing result

print("Filtered Rows : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[‘gfg is’, ‘best’], [‘gfg’, ‘good’], [‘gfg is
> cool’], [‘love’, ‘gfg’]]  
> Filtered Rows : [[‘gfg’, ‘good’], [‘love’, ‘gfg’]]

 **Method #2 : Using** **filter()** **+** **lambda** **\+ any() + regex**

In this, we perform task of filtering using filter() and lambda function, rest
all the functionalities are performed alike the above method.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Filter rows without Space Strings

# Using filter() + lambda + any() + regex

import re

 

# initializing list

test_list = [["gfg is", "best"], ["gfg", "good"],

 ["gfg is cool"], ["love", "gfg"]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# checking for spaces using regex

# not including row if any string has space

res = list(filter(lambda row: not
any(bool(re.search(r"\s", ele))

 for ele in row), test_list))

 

# printing result

print("Filtered Rows : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [[‘gfg is’, ‘best’], [‘gfg’, ‘good’], [‘gfg is
> cool’], [‘love’, ‘gfg’]]  
> Filtered Rows : [[‘gfg’, ‘good’], [‘love’, ‘gfg’]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

