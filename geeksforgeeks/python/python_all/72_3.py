Python – Alternate Default Key Value



Sometimes, while working with Python Dictionaries, we can have problem in
which we need to assign a particular value to a particular key, but in
absence, require the similar’s key’s value but from different dictionary. This
problem can have applications in domain of web development. Let’s discuss
certain ways in which this task can be performed.

>  **Input** : test_dict = {‘gfg’ : {‘a’ : 1, ‘b’ : 2, ‘c’ : 3}, ‘best’ : {‘a’
> : 3, ‘c’ : 4, ‘b’ : 17}}  
>  **Output** : 17
>
>  **Input** : test_dict = {‘gfg’ : {‘b’ : 1}, ‘best’ : {‘a’ : 3}}  
>  **Output** : 1

 **Method #1 : Using loop**  
This is brute force way in which this task can be performed. In this, we test
for a particular dictionary for value, if not present we check the alternate
key and assign value.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Alternate Default Key Value

# Using loop

 

# initializing dictionary

test_dict = {'gfg' : {'a' : 1, 'b' : 2, 'c' :
3}, 'best' : {'a' : 3, 'c' : 4}}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# alternate key 

alt_key = 'gfg'

 

# Alternate Default Key Value

# Using loop

if 'b' in test_dict['best']:

 res = test_dict['best']['b']

else :

 res = test_dict[alt_key]['b']

 

# printing result 

print("The required value : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

> The original dictionary is : {‘gfg’: {‘a’: 1, ‘b’: 2, ‘c’: 3}, ‘best’: {‘a’:
> 3, ‘c’: 4}}  
> The required value : 2

