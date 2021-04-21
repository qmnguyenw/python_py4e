Python – Reinitialize Value lists to K in Dictionary



Sometimes, while working with Python dictionary values, we can have a problem
in which we need to reinitialize all the values lists of all keys in
dictionary to a constant K. This kind of problem can have application in
domains which use data, like Machine Learning and Data Science. Let’s discuss
certain way in which this task can be performed.

>  **Input** : test_dict = {‘Gfg’ : [[4, 5], [8, 9, 20], [1, 3, 4, ‘oops’]]}  
>  **Output** : {‘Gfg’: [[4, 4], [4, 4, 4], [4, 4, 4, 4]]}
>
>  **Input** : test_dict = {‘Gfg’ : “best”}  
>  **Output** : {‘Gfg’ : 4}

 **Method : Using recursion +type() + dictionary comprehension + items() \+
loop**  
The combination of above functionalities can help to solve this problem. In
this, we perform the assignment of values using dictionary comprehension and
types are tested using type. The items() is used to extract values from
dictionary and to perform to each nesting is handled by recursion.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Reinitialize Value lists to K in Dictionary

# Using recursion + type() + dictionary comprehension + items() + loop

 

# helpr function

def helpr_fnc(ele, K):

 if type(ele) is list:

 return [helpr_fnc(val, K) for val in ele]

 elif type(ele) is dict:

 return {key : helpr_fnc(val, K) for key, val in ele.items()}

 return K

 

# initializing dictionary

test_dict = {'gfg' : [4, 6, 7], 'is' : 8,
'best' : [[4, 5], [8, 9, 20]]}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# initializing K 

K = 4

 

# Reinitialize Value lists to K in Dictionary

# Using recursion + type() + dictionary comprehension + items() + loop

res = helpr_fnc(test_dict, K)

 

# printing result 

print("The Reinitialized dictionary : " + str(dict(res)))   
  
---  
  
__

__

**Output :**

  

  

> The original dictionary : {‘best’: [[4, 5], [8, 9, 20]], ‘is’: 8, ‘gfg’: [4,
> 6, 7]}  
> The Reinitialized dictionary : {‘best’: [[4, 4], [4, 4, 4]], ‘is’: 4, ‘gfg’:
> [4, 4, 4]}

