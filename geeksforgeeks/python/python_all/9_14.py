Python program to Remove Duplicity from a Dictionary



Given a dictionary with value as lists, the task is to write a Python program
that can remove contents of the dictionary irrespective of the fact that they
are keys or values that occur more than once.

>  **Input :** {‘gfg’ : [‘gfg’, ‘is’, ‘best’], ‘best’ : [‘gfg’], ‘apple’ :
> [‘good’]}
>
>  **Output :** {‘gfg’: [‘gfg’, ‘is’, ‘best’], ‘apple’: [‘good’]}
>
>  **Explanation** : best key is omitted as it is already as value of 1st key.
>
> **Input :** {‘gfg’ : [‘gfg’, ‘is’, ‘best’, ‘apple’], ‘best’ : [‘gfg’],
> ‘apple’ : [‘good’]}
>
>  
>
>
>  
>
>
>  **Output :** {‘gfg’: [‘gfg’, ‘is’, ‘best’, ‘apple’]}
>
>  **Explanation :** best and apple keys are omitted as it is already as value
> of 1st key.

**Approach :** _Using_ _loop_ _and items()_

In this, we iterate for each key and its value is extracted using items(), and
memorize them, keys and values are omitted to be added/created in case they
have already occurred.

 **Program:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing dictionary

test_dict = {'gfg': ['gfg', 'is', 'best'],

 'best': ['gfg'],

 'apple': ['good']}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

res = dict()

for key, val in test_dict.items():

 

 flag = True

 for key1, val1 in res.items():

 

 # filtering value from memoised values

 if key in val1:

 flag = False

 if flag:

 res[key] = val

 

# printing result

print("The filtered dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original dictionary is : {‘gfg’: [‘gfg’, ‘is’, ‘best’], ‘best’: [‘gfg’],
> ‘apple’: [‘good’]}
>
> The filtered dictionary : {‘gfg’: [‘gfg’, ‘is’, ‘best’], ‘apple’: [‘good’]}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

