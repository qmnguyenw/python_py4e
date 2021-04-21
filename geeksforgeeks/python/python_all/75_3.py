Python – Key Lists Summations



Sometimes, while working with Python Dictionaries, we can have problem in
which we need to perform the replace of key with values with sum of all keys
in values. This can have application in many domains that include data
computations, such as Machine Learning. Let’s discuss certain ways in which
this task can be performed.

 **Method #1 : Usingsum() \+ loop**  
This is one of the ways in which this task can be performed. In this, we
perform the summation using sum, and iteration to each key is done in brute
way using loop.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Key Values Summations

# Using sum() + loop

 

# initializing dictionary

test_dict = {'gfg' : [4, 6, 8], 'is' : [9, 8,
2], 'best' : [10, 3, 2]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Key Values Summations

# Using sum() + loop

for key, value in test_dict.items():

 test_dict[key] = sum(value)

 

# printing result 

print("The summation keys are : " + str(test_dict))   
  
---  
  
__

__

**Output :**

> The original dictionary is : {‘gfg’: [4, 6, 8], ‘is’: [9, 8, 2], ‘best’:
> [10, 3, 2]}  
> The summation keys are : {‘gfg’: 18, ‘is’: 19, ‘best’: 15}

  

  

**Method #2 : Using dictionary comprehension +sum()**  
This is yet another way in which this task can be performed. This is similar
to above method, just a shorthand version.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Key Values Summations

# Using dictionary comprehension + sum()

 

# initializing dictionary

test_dict = {'gfg' : [4, 6, 8], 'is' : [9, 8,
2], 'best' : [10, 3, 2]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Key Values Summations

# Using dictionary comprehension + sum()

res = {key : sum(val) for key, val in test_dict.items()}

 

# printing result 

print("The summation keys are : " + str(res))   
  
---  
  
__

__

**Output :**

> The original dictionary is : {‘gfg’: [4, 6, 8], ‘is’: [9, 8, 2], ‘best’:
> [10, 3, 2]}  
> The summation keys are : {‘gfg’: 18, ‘is’: 19, ‘best’: 15}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

