Python – Sort given list of strings by part the numeric part of string



Given a list of strings. The task is to sort the list by the numeric part of
the string.

 **Examples:**

>  **Input** : test_list = [“Gfg34”, “is67”, “be3st”, “f23or”, “ge9eks”]  
> **Output** : [‘be3st’, ‘ge9eks’, ‘f23or’, ‘Gfg34’, ‘is67’]  
> **Explanation** : 3 < 9 < 23 < 34 < 67, numbers extracted from strings.
>
>  **Input** : test_list = [“Gfg4”, “is67”, “be3st”, “f23or”, “ge9eks”]  
> **Output** : [‘be3st’, ‘Gfg4’, ‘ge9eks’, ‘f23or’, ‘is67’]  
> **Explanation** : 3 < 4 < 9 < 23 < 67, numbers extracted from strings.

**Method #1 : Using sort() + re.findall()**

  

  

In this, we perform the task of sorting using sort(), the explicit function is
used to extract numbers using findall().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort Strings on numerical substrings

# Using sort() + findall()

import re

 

# helper function to perform sort

def num_sort(test_string):

 return list(map(int, re.findall(r'\d+',
test_string)))[0]

 

# initializing list

test_list = ["Gfg34", "is67", "be3st", "f23or",
"ge9eks"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# calling function

test_list.sort(key=num_sort) 

 

# printing result 

print("Strings after numercial Sort : " + str(test_list))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [‘Gfg34’, ‘is67’, ‘be3st’, ‘f23or’, ‘ge9eks’]  
> Strings after numercial Sort : [‘be3st’, ‘ge9eks’, ‘f23or’, ‘Gfg34’, ‘is67’]

 **Method #2 : Using sort() +** **lambda** **\+ findall()**

In this, we perform a similar function, but the difference being we use lambda
function rather than an external function to perform the task of sorting.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort Strings on numerical substrings

# Using sort() + lambda + findall()

import re

 

# initializing list

test_list = ["Gfg34", "is67", "be3st", "f23or",
"ge9eks"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# findall() getting all integers.

# conversion to integers using map()

test_list.sort(key=lambda test_string : list(

 map(int, re.findall(r'\d+', test_string)))[0]) 

 

# printing result 

print("Strings after numercial Sort : " + str(test_list))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [‘Gfg34’, ‘is67’, ‘be3st’, ‘f23or’, ‘ge9eks’]  
> Strings after numercial Sort : [‘be3st’, ‘ge9eks’, ‘f23or’, ‘Gfg34’, ‘is67’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

