Python – Extract selective keys’ values Including Nested Keys



Sometimes, while working with Python dictionaries, we can have a problem in
which we need to extract selective keys’ values. This problem has been solved
earlier, but sometimes, we can have multiple nestings and certain keys may be
present in inner records. This problem caters all the nestings for extraction
of keys’ values. Let’s discuss certain way in which this task can be solved.

>  **Input** :  
> test_dict = {‘gfg’: {‘geeks’: {‘best’ : 3}}}  
> key_list = [‘best’, ‘geeks’]  
>  **Output** : {‘geeks’: {‘best’: 3}, ‘best’: 3}
>
>  **Input** :  
> test_dict = {‘gfg’: {‘geek’: {‘good’ : 3}}}  
> key_list = [‘best’, ‘geeks’]  
>  **Output** : {}

 **Method : Using recursion + loop + yield**  
The combination of above functionalities can be used to solve this problem. In
this, we perform the task of checking for key using conditional statements and
check for nestings using recursion. The yield operator is used to dynamically
return the key for sssignment as it occurs.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract selective keys' values [ Including Nested Keys ]

# Using recursion + loop + yield

 

def get_vals(test_dict, key_list):

 for i, j in test_dict.items():

 if i in key_list:

 yield (i, j)

 yield from [] if not isinstance(j, dict) else
get_vals(j, key_list)

 

# initializing dictionary

test_dict = {'gfg': {'is': {'best' : 3}}, 'for':
{'all' : 4}, 'geeks': 5}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing keys list 

key_list = ['best', 'geeks']

 

# Extract selective keys' values [ Including Nested Keys ]

# Using recursion + loop + yield

res = dict(get_vals(test_dict, key_list))

 

# printing result 

print("The extracted values : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original dictionary is : {'gfg': {'is': {'best': 3}}, 'for': {'all': 4}, 'geeks': 5}
    The extracted values : {'best': 3, 'geeks': 5}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

