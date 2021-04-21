Python – Remove K valued key from Nested Dictionary



Sometimes, while working with records, we can have a problem in which we need
to perform the removal of a key from nested dictionary whose value us specific
to K. This is a common problem and has its application in data domains such as
web development. Lets discuss certain ways in which this task can be
performed.

>  **Input** : test_dict = {‘CS’: {‘priceless’: 6}, ‘is’: {‘better’: 6},
> ‘gfg’: {‘best’: 6}}  
>  **Output** : {‘CS’: {}, ‘gfg’: {}, ‘is’: {}}
>
>  **Input** : test_dict = {‘CS’: {‘priceless’: 9}, ‘is’: {‘better’: 8},
> ‘gfg’: {‘best’: 7}}  
>  **Output** : {‘CS’: {‘priceless’: 9}, ‘is’: {‘better’: 8}, ‘gfg’: {‘best’:
> 7}}

 **Method #1 : Using loop + isinstance() +filter()**  
The combination of above functions can be used to solve this problem. In this,
we perform the task of K value using filter() and isinstance() is used to test
for nesting dictionary. The dictionary construction is done using loop.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove K valued key from Nested Dictionary

# Using loop + isinstance() + filter()

 

# initializing dictionary

test_dict = {'gfg' : {'best' : 4, 'good' : 5}, 

 'is' : {'better' : 6, 'educational' : 4},

 'CS' : {'priceless' : 6}}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# initializing rem_val

rem_val = 6

 

# Remove K valued key from Nested Dictionary

# Using loop + isinstance() + filter()

def rem_vals(ele):

 global rem_val

 key, val = ele

 return val != rem_val

 

res = dict()

for key, val in test_dict.items():

 if isinstance(val, dict):

 res[key] = dict(filter(rem_vals, val.items()))

 else:

 res[key] = val

 

# printing result 

print("Dictionary after removal : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

> The original dictionary : {‘is’: {‘educational’: 4, ‘better’: 6}, ‘gfg’:
> {‘best’: 4, ‘good’: 5}, ‘CS’: {‘priceless’: 6}}  
> Dictionary after removal : {‘is’: {‘educational’: 4}, ‘gfg’: {‘best’: 4,
> ‘good’: 5}, ‘CS’: {}}

