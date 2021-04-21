Python program to extract Keywords from a list



Given List of strings, extract all the words that are keywords.

>  **Input** : test_list = [“Gfg is True”, “Its a global win”, “try Gfg”],  
> **Output** : [‘is’, ‘True’, ‘global’, ‘try’]  
> **Explanation** : All strings in result list is valid Python keyword.
>
>  **Input** : test_list = [“try Gfg”],  
> **Output** : [‘try’]  
> **Explanation** : try is used in try/except block, hence a keyword.

**Method #1 : Using iskeyword() + split() + loop**

This is one of the ways in which this task can be performed. In this, we check
for keyword using iskeyword() and convert a string to words using split(). The
logic of extension to all strings happens using loop.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract Keywords from String List

 

# Using iskeyword() + loop + split()

import keyword

 

# initializing list

test_list = ["Gfg is True", "Gfg will yield a return",

 "Its a global win", "try Gfg"]

 

# printing original list

print("The original list is : " + str(test_list))

 

 

# iterating using loop

res = []

for sub in test_list:

 for word in sub.split():

 

 # check for keyword using iskeyword()

 if keyword.iskeyword(word):

 res.append(word)

 

# printing result

print("Extracted Keywords : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [‘Gfg is True’, ‘Gfg will yield a return’, ‘Its a
> global win’, ‘try Gfg’]  
> Extracted Keywords : [‘is’, ‘True’, ‘yield’, ‘return’, ‘global’, ‘try’]

 **Method #2: Using list comprehension**

This is yet another way in which this task can be performed. Similar to the
above method but much compact on paper, use similar functionalities as the
above method.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract Keywords from String List

 

# Using list comprehension

import keyword

 

# initializing list

test_list = ["Gfg is True", "Gfg will yield a return",

 "Its a global win", "try Gfg"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# One-liner using list comprehension

res = [ele for sub in test_list for ele in sub.split()
if keyword.iskeyword(ele)]

 

# printing result

print("Extracted Keywords : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original list is : [‘Gfg is True’, ‘Gfg will yield a return’, ‘Its a
> global win’, ‘try Gfg’]  
> Extracted Keywords : [‘is’, ‘True’, ‘yield’, ‘return’, ‘global’, ‘try’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

