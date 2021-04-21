Python program to convert URL Parameters to Dictionary items



Given URL Parameters string, convert to dictionary items.

>  **Input** : test_str = ‘gfg=4&is;=5’  
> **Output** : {‘gfg’: [‘4’], ‘is’: [‘5’]}  
> **Explanation** : gfg’s value is 4.
>
>  **Input** : test_str = ‘gfg=4’  
> **Output** : {‘gfg’: [‘4’]}  
> **Explanation** : gfg’s value is 4 as param.  
>

**Method #1 : Using urllib.parse.parse_qs()**

This is default inbuilt function which performs this task, it parses and the
keys are formed from LHS of “=” and return list of values that are in RHS
values for the parameters. Thus, import external urllib.parse(), to enable
this to work.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# import module

import urllib.parse

 

# initializing string

test_str = 'gfg=4&is;=5&best;=yes'

 

# printing original string

print("The original string is : " + str(test_str))

 

# parse_qs gets the Dictionary and value list

res = urllib.parse.parse_qs(test_str)

 

# printing result

print("The parsed URL Params : " + str(res))  
  
---  
  
 __

 __

 **Output**

> The original string is : gfg=4&is;=5&best;=yes  
> The parsed URL Params : {‘gfg’: [‘4’], ‘is’: [‘5’], ‘best’: [‘yes’]}

 **Method #2 : Using findall() + setdefault()**

In this, we get all the parameters using findall(), and then assign keys and
values using setdefault() and loop.

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

test_str = 'gfg=4&is;=5&best;=yes'

 

# printing original string

print("The original string is : " + str(test_str))

 

# getting all params

params = re.findall(r'([^=&]+)=([^=&]+)', test_str)

 

# assigning keys with values

res = dict()

for key, val in params:

 

 res.setdefault(key, []).append(val)

 

# printing result

print("The parsed URL Params : " + str(res))  
  
---  
  
 __

 __

 **Output**

> The original string is : gfg=4&is;=5&best;=yes  
> The parsed URL Params : {‘gfg’: [‘4’], ‘is’: [‘5’], ‘best’: [‘yes’]}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

