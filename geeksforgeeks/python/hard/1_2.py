Python Program to Convert String Matrix Representation to Matrix



Given a String with matrix representation, the task here is to write a python
program that converts it to a matrix.

>  **Input :** test_str = “[gfg,is],[best,for],[all,geeks]”
>
>  **Output :** [[‘gfg’, ‘is’], [‘best’, ‘for’], [‘all’, ‘geeks’]]
>
>  **Explanation :** Required String Matrix is converted to Matrix with list
> as data type.
>
>  **Input :** test_str = “[gfg,is],[for],[all,geeks]”
>
>  
>
>
>  
>
>
>  **Output :** [[‘gfg’, ‘is’], [‘for’], [‘all’, ‘geeks’]]
>
>  **Explanation :** Required String Matrix is converted to Matrix with list
> as data type.

 **Method 1 :** Using split() and regex expression

In this, a plain list is constructed using appropriate regex expression and
split() performs the task of getting inner dimension for 2D Matrix.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import re

 

# initializing string

test_str = "[gfg,is],[best,for],[all,geeks]"

 

# printing original string

print("The original string is : " + str(test_str))

 

flat_1 = re.findall(r"\[(.+?)\]", test_str)

res = [sub.split(",") for sub in flat_1]

 

# printing result

print("The type of result : " + str(type(res)))

print("Converted Matrix : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original string is : [gfg,is],[best,for],[all,geeks]
>
> The type of result : <class ‘list’>
>
>  
>
>
>  
>
>
> Converted Matrix : [[‘gfg’, ‘is’], [‘best’, ‘for’], [‘all’, ‘geeks’]]

 **Method 2 :** Using json.loads()

In this, the task of conversion to the matrix is done using the unbuilt method
of loads() of JSON library.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert String Matrix Representation to Matrix

# Using json.loads()

import json

 

# initializing string

test_str = '[["gfg", "is"], ["best", "for"], ["all", "geeks"]]'

 

# printing original string

print("The original string is : " + str(test_str))

 

# inbuild function performing task of conversion

# notice input

res = json.loads(test_str)

 

# printing result

print("The type of result : " + str(type(res)))

print("Converted Matrix : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original string is : [[“gfg”, “is”], [“best”, “for”], [“all”, “geeks”]]
>
> The type of result : <class ‘list’>
>
> Converted Matrix : [[‘gfg’, ‘is’], [‘best’, ‘for’], [‘all’, ‘geeks’]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

