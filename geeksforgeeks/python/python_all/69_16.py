Python – Unnest single Key Nested Dictionary List



Sometimes, while working with Python data, we can have a problem in which we
need to perform unnesting of all the dictionaries which have single nesting of
keys, i.e a single key and value and can easily be pointed to outer key
directly. This kind of problem is common in domains requiring data
optimization. Let’s discuss certain ways in which this task can be performed.

>  **Input** : test_list = [{‘gfg’ : {‘data’ : 1}}, {‘is’ : {‘data’ : 5,
> ‘geeks’ : 7}}]  
>  **Output** : {‘is’: 5, ‘gfg’: 1}
>
>  **Input** : test_list = [{‘gfg’ : {‘data’ : ‘best’}}]  
>  **Output** : {‘gfg’: ‘best’}

 **Method #1 : Using loop +items()**  
The combination of above methods can be used to solve this problem. In this,
we iterate for the values in list, using loop and extract all dictionary items
using items() and perform new dictionary creation using brute force method.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Unnest single Key Nested Dictionary List

# Using loop + items()

 

# initializing list

test_list = [{'gfg' : {'data' : 1}}, {'is' : {'data'
: 5}}, {'best' : {'data' : 4}}]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing key 

data_key = 'data'

 

# Unnest single Key Nested Dictionary List

# Using loop + items()

res = dict()

for sub in test_list:

 for key, val in sub.items():

 res[key] = sub[key][data_key]

 

# printing result 

print("The constructed Dictionary list : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

> The original list is : [{‘gfg’: {‘data’: 1}}, {‘is’: {‘data’: 5}}, {‘best’:
> {‘data’: 4}}]  
> The constructed Dictionary list : {‘gfg’: 1, ‘best’: 4, ‘is’: 5}

