Python – Value list Mean



Sometimes, while working with Python dictionary values, we can have problem in
which we need to find mean of all the values of all dictionary value lists.
This problem can have applications across many domains including web
development. Let’s discuss certain ways in which this problem can be solved.

>  **Input** : test_dict = {‘best’: [11, 21], ‘Gfg’: [7, 5]}  
>  **Output** : {‘best’: 16.0, ‘Gfg’: 6.0}
>
>  **Input** : test_dict = {‘Gfg’ : [9]}  
>  **Output** : {‘Gfg’: 9.0}

 **Method #1 : Using loop +sum() + len()**  
The combination of above functions can be used to solve this problem. In this,
we compute the sum of all values using sum() and all value list lengths using
len(). The iteration is done using loop.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Value list mean

# Using loop + sum() + len()

 

# initializing dictionary

test_dict = {'Gfg' : [6, 7, 5, 4], 'is' :
[10, 11, 2, 1], 'best' : [12, 1, 2]} 

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Value list mean

# Using loop + sum() + len()

res = dict()

for key in test_dict:

 res[key] = sum(test_dict[key]) / len(test_dict[key])

 

# printing result 

print("The dictionary average is : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

> The original dictionary is : {‘is’: [10, 11, 2, 1], ‘best’: [12, 1, 2],
> ‘Gfg’: [6, 7, 5, 4]}  
> The dictionary average is : {‘is’: 6.0, ‘best’: 5.0, ‘Gfg’: 5.5}

