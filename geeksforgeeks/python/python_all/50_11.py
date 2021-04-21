Python – Flatten Dictionary with List



Given a list and dictionary, flatten dictionary with keys and values at
position of available element of key in list.

>  **Input** : test_list = [“Gfg”, “is”, “Best”, “For”, “Geeks”], subs_dict =
> {“Gfg” : 7}  
>  **Output** : [‘Gfg’, 7, ‘is’, ‘Best’, ‘For’, ‘Geeks’]  
>  **Explanation** : “Gfg” is replaced, followed by its value in dictionary.
>
>  **Input** : test_list = [“Gfg”, “is”, “Best”, “For”, “Geeks”], subs_dict =
> {“gfg” : 7, “best” : 8}  
>  **Output** : [‘Gfg’, ‘is’, ‘Best’, ‘For’, ‘Geeks’]  
>  **Explanation** : No replacement. No matching values.

 **Method #1 : Using list comprehension + get()**

The combination of above functionalities can be used to solve this problem. In
this, we append all the key if present checking using get(), along with values
in list.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Flatten Dictionary with List

# Using get() + list comprehension

 

# initializing list

test_list = ["Gfg", "is", "Best", "For", "Geeks"]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing subs. Dictionary

subs_dict = {"Gfg" : 7, "Geeks" : 8}

 

# get() to perform presence checks and assign value

temp = object()

res = [ele for sub in ((ele, subs_dict.get(ele, temp))

 for ele in test_list) for ele in sub if ele !=
temp]

 

# printing result 

print("The list after substitution : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : ['Gfg', 'is', 'Best', 'For', 'Geeks']
    The list after substitution : ['Gfg', 7, 'is', 'Best', 'For', 'Geeks', 8]
    

**Method #2 : Using chain.from_iterable() + list comprehension**

This is yet another way in which this task can be performed. In this, we form
key value pair list and append if present and if not retain the element. Next,
the flattening of key-value lists is performed using chain.from_iterable().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Flatten Dictionary with List

# Using chain.from_iterable() + list comprehension 

from itertools import chain

 

# initializing list

test_list = ["Gfg", "is", "Best", "For", "Geeks"]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing subs. Dictionary

subs_dict = {"Gfg" : 7, "Geeks" : 8}

 

temp = ([ele, subs_dict[ele]] if ele in subs_dict 

 else [ele] for ele in test_list)

 

# chain.from_iterable() for flattening 

res = list(chain.from_iterable(temp))

 

# printing result 

print("The list after substitution : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : ['Gfg', 'is', 'Best', 'For', 'Geeks']
    The list after substitution : ['Gfg', 7, 'is', 'Best', 'For', 'Geeks', 8]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

