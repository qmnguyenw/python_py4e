Python – Extract Keys with specific Value Type



Given a dictionary, extract all the keys, whose values are of given type.

>  **Input** : test_dict = {‘gfg’ : 2, ‘is’ : ‘hello’, ‘for’ : {‘1’ : 3},
> ‘geeks’ : 4}, targ_type = int  
> **Output** : [‘gfg’, ‘geeks’]  
> **Explanation** : gfg and geeks have integer values.
>
>  **Input** : test_dict = {‘gfg’ : 2, ‘is’ : ‘hello’, ‘for’ : {‘1’ : 3},
> ‘geeks’ : 4}, targ_type = str  
> **Output** : [‘is’]  
> **Explanation** : is has string value.

**Method #1 : Using loop +** **isinstance()** ****

In this, we check for data type using _isinstance()_ , and iterate for all the
values using loop.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract Keys with specific Value Type

# Using loop + isinstance()

 

# initializing dictionary

test_dict = {'gfg': 2, 'is': 'hello', 'best': 2,
'for': {'1': 3}, 'geeks': 4}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing type

targ_type = int

 

res = []

for key, val in test_dict.items():

 

 # checking for values datatype

 if isinstance(val, targ_type):

 res.append(key)

 

# printing result

print("The extracted keys : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original dictionary is : {‘gfg’: 2, ‘is’: ‘hello’, ‘best’: 2, ‘for’:
> {‘1’: 3}, ‘geeks’: 4}  
> The extracted keys : [‘gfg’, ‘best’, ‘geeks’]

 **Method #2 : Using** **list comprehension** **+** **isinstance()**

Similar to above method, one-liner shorthand to solve this problem using list
comprehension.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract Keys with specific Value Type

# Using list comprehension + isinstance()

 

# initializing dictionary

test_dict = {'gfg': 2, 'is': 'hello', 'best': 2,
'for': {'1': 3}, 'geeks': 4}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing type

targ_type = int

 

# one-liner to solve the problem

res = [key for key, val in test_dict.items() if
isinstance(val, targ_type)]

 

# printing result

print("The extracted keys : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original dictionary is : {‘gfg’: 2, ‘is’: ‘hello’, ‘best’: 2, ‘for’:
> {‘1’: 3}, ‘geeks’: 4}  
> The extracted keys : [‘gfg’, ‘best’, ‘geeks’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

