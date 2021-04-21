Python – Convert Nested dictionary to Mapped Tuple



Sometimes, while working with Python dictionaries, we can have a problem in
which we need to convert nested dictionaries to mapped tuple. This kind of
problem can occur in web development and day-day programming. Let’s discuss
certain ways in which this task can be performed.

>  **Input** : test_dict = {‘gfg’ : {‘x’ : 5, ‘y’ : 6, ‘z’: 3}, ‘best’ : {‘x’
> : 8, ‘y’ : 3, ‘z’: 5}}  
>  **Output** : [(‘x’, (5, 8)), (‘y’, (6, 3)), (‘z’, (3, 5))]
>
>  **Input** : test_dict = {‘gfg’ : {‘x’ : 5, ‘y’ : 6, ‘z’: 3}}  
>  **Output** : [(‘x’, (5, )), (‘y’, (6, )), (‘z’, (3, ))]

 **Method #1 : Using list comprehension + generator expression**  
The combination of above functions can be used to solve this problem. In this,
we perform the tasks of creating the tuple using list comprehension and
generator expression helps in grouping, by extracting values using values().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Nested dictionary to Mapped Tuple

# Using list comprehension + generator expression

 

# initializing dictionary

test_dict = {'gfg' : {'x' : 5, 'y' : 6}, 'is' :
{'x' : 1, 'y' : 4},

 'best' : {'x' : 8, 'y' : 3}}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Convert Nested dictionary to Mapped Tuple

# Using list comprehension + generator expression

res = [(key, tuple(sub[key] for sub in test_dict.values())) 

 for key in test_dict['gfg']]

 

# printing result 

print("The grouped dictionary : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

> The original dictionary is : {‘gfg’: {‘x’: 5, ‘y’: 6}, ‘is’: {‘x’: 1, ‘y’:
> 4}, ‘best’: {‘x’: 8, ‘y’: 3}}  
> The grouped dictionary : [(‘x’, (5, 1, 8)), (‘y’, (6, 4, 3))]

