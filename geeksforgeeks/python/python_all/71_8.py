Python – Custom order dictionary



Sometimes, while working with Python dictionaries, we can have a problem in
which we need to perform the custom ordering of keys of dictionary. This is
quite popular problem, with the advent of newer version of Python, where keys
are ordered in Dictionaries, there might be requirement to reorder dictionary
keys. Let’s discuss certain ways in which this task can be performed.

>  **Input** : test_dict = {‘gfg’: 1, ‘is’: 2, ‘best’: 3, ‘for’: 4, ‘geeks’:
> 5}  
>  **Output** : {‘gfg’: 1, ‘is’: 2, ‘best’: 3, ‘for’: 4, ‘geeks’: 5}
>
>  **Input** : test_dict = {‘geeks’: 5, ‘for’: 4, ‘best’: 3, ‘is’: 2, ‘gfg’:
> 1}  
>  **Output** : {‘gfg’: 1, ‘is’: 2, ‘best’: 3, ‘for’: 4, ‘geeks’: 5}

 **Method #1 : Using loop**  
This is brute force way to solve this problem. In this, we construct the newer
dictionary by appending the keys in order list, mapping with keys in original
dictionary. Works with Python >= 3.6.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Custom order dictionary

# Using loop

 

# initializing dictionary

test_dict = {'is' : 2, 'for' : 4, 'gfg' : 1,
'best' : 3, 'geeks' : 5} 

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing order

ord_list = ['gfg', 'is', 'best', 'for', 'geeks']

 

# Custom order dictionary

# Using loop

res = dict()

for key in ord_list:

 res[key] = test_dict[key]

 

# printing result 

print("Ordered dictionary is : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

> The original dictionary is : {‘is’: 2, ‘for’: 4, ‘gfg’: 1, ‘best’: 3,
> ‘geeks’: 5}  
> Ordered dictionary is : {‘gfg’: 1, ‘is’: 2, ‘best’: 3, ‘for’: 4, ‘geeks’: 5}

