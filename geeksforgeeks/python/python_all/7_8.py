Python Program to Swap dictionary item’s position



Given a Dictionary, the task is to write a python program to swap positions of
dictionary items. The code given below takes two indices and swap values at
those indices.

> **Input :** test_dict = {‘Gfg’ : 4, ‘is’ : 1, ‘best’ : 8, ‘for’ : 10,
> ‘geeks’ : 9}, i, j = 1, 3
>
>  **Output :** {‘Gfg’: 4, ‘for’: 10, ‘best’: 8, ‘is’: 1, ‘geeks’: 9}
>
>  **Explanation :** (for : 10) and (is : 1) swapped order.
>
>  **Input :** test_dict = {‘Gfg’ : 4, ‘is’ : 1, ‘best’ : 8, ‘for’ : 10,
> ‘geeks’ : 9}, i, j = 2, 3
>
>  
>
>
>  
>
>
>  **Output :** {‘Gfg’: 4, ‘is’: 1, ‘for’: 10, ‘best’: 8, ‘geeks’: 9}
>
>  **Explanation :** (for : 10) and (best : 8) swapped order.

 **Method :** _Using_ _items()_ _and_ _dict()_

This task is achieved in 3 steps:

  * First dictionary is converted to equivalent key value pairs in form of tuples, 
  * Next swap operation is performed in a Pythonic way. 
  * At last, tuple list is converted back to dictionary, in its required format.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing dictionary

test_dict = {'Gfg': 4, 'is': 1, 'best': 8,
'for': 10, 'geeks': 9}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing swap indices

i, j = 1, 3

 

# conversion to tuples

tups = list(test_dict.items())

 

# swapping by indices

tups[i], tups[j] = tups[j], tups[i]

 

# converting back

res = dict(tups)

 

# printing result

print("The swapped dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original dictionary is : {‘Gfg’: 4, ‘is’: 1, ‘best’: 8, ‘for’: 10,
> ‘geeks’: 9}
>
> The swapped dictionary : {‘Gfg’: 4, ‘for’: 10, ‘best’: 8, ‘is’: 1, ‘geeks’:
> 9}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

