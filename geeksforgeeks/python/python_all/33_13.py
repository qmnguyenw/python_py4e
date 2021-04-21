Python program to split the string and convert it to dictionary



Given a delimiter (denoted as **delim** in code) separated string, order the
splits in form of dictionary.

 **Examples :**

>  **Input** : test_str = ‘gfg*is*best*for*geeks’, delim = “*”  
> **Output** : {0: ‘gfg’, 1: ‘is’, 2: ‘best’, 3: ‘for’, 4: ‘geeks’}  
>
>
> **Input** : test_str = ‘gfg*is*best’, delim = “*”  
> **Output** : {0: ‘gfg’, 1: ‘is’, 2: ‘best’}  
>

**Method 1 : Using split() + loop**

  

  

This is a brute way in which this task can be performed. In this, the split
sections are stored in a temporary list using split() and then the new
dictionary is created from the temporary list.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Using split() + loop

 

# initializing string

test_str = 'gfg_is_best_for_geeks'

 

# printing original string

print("The original string is : "

 + str(test_str))

 

# initializing delim

delim = "_"

 

# splitting using split()

temp = test_str.split(delim)

 

res = dict()

 

# using loop to reform dictionary with splits

for idx, ele in enumerate(temp):

 res[idx] = ele

 

# printing result

print("Dictionary after splits ordering : "

 + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original string is : gfg_is_best_for_geeks  
> Dictionary after splits ordering : {0: ‘gfg’, 1: ‘is’, 2: ‘best’, 3: ‘for’,
> 4: ‘geeks’}

 **Method 2 : Using dictionary comprehension + split() + enumerate()**

This is a shorthand method with the help of which this task can be performed.
In this, we perform the task of dictionary reconstruction using one-liner
dictionary(dictionary comprehension) and enumerate() is used to help in
ordering.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Using dictionary comprehesion + split() + enumerate()

 

# initializing string

test_str = 'gfg_is_best_for_geeks'

 

# printing original string

print("The original string is : "

 + str(test_str))

 

# initializing delim

delim = "_"

 

# using one liner to rearrange dictionary

res = {idx: ele for idx, ele in

 enumerate(test_str.split(delim))}

 

# printing result

print("Dictionary after splits ordering : "

 + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original string is : gfg_is_best_for_geeks  
> Dictionary after splits ordering : {0: ‘gfg’, 1: ‘is’, 2: ‘best’, 3: ‘for’,
> 4: ‘geeks’}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

