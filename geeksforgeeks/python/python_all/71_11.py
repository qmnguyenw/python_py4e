Python – Combine dictionary with priority



Sometimes, while working with dictionary data, we can have problem in which we
need to combine two dictionaries. This is very common problem. But a variation
of this can be combining dictionaries, and giving precedence to a particular
dictionary if both the keys clash in dictionaries. Let’s discuss certain ways
in which this task can be performed.

>  **Input** : test_dict1 = {‘Gfg’ : 6, ‘is’ : 15, ‘best’ : 13}  
> test_dict2 = {‘Gfg’ : 8, ‘is’ : 10}  
>  **Output** : {‘Gfg’: 8, ‘best’: 13, ‘is’: 10}
>
>  **Input** : test_dict1 = {‘Gfg’ : 6}  
> test_dict2 = {‘Gfg’ : 8}  
>  **Output** : {‘Gfg’: 8}

 **Method #1 : Usingcopy() \+ loop**  
The combination of above functionalities can be used to solve this problem.
This is brute way in which this problem can be solved. In this, we perform
copy() to deep copy dictionary values and then override the values using
priority dictionary.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Combine dictionary with priority

# Using loop + copy()

 

# initializing dictionaries

test_dict1 = {'Gfg' : 1, 'is' : 2, 'best' : 3}

test_dict2 = {'Gfg' : 4, 'is' : 10, 'for' : 7,
'geeks' : 12}

 

# printing original dictionaries

print("The original dictionary is 1 : " + str(test_dict1))

print("The original dictionary is 2 : " + str(test_dict2))

 

# declaring priority order

prio_dict = {1 : test_dict2, 2: test_dict1}

 

# Combine dictionary with priority

# Using loop + copy()

res = prio_dict[2].copy()

for key, val in prio_dict[1].items():

 res[key] = val

 

# printing result 

print("The dictionary after combination : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

> The original dictionary is 1 : {‘is’: 2, ‘best’: 3, ‘Gfg’: 1}  
> The original dictionary is 2 : {‘for’: 7, ‘is’: 10, ‘geeks’: 12, ‘Gfg’: 4}  
> The dictionary after combination : {‘for’: 7, ‘is’: 10, ‘best’: 3, ‘geeks’:
> 12, ‘Gfg’: 4}

