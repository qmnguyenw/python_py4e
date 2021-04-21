Python – Filter odd elements from value lists in dictionary



Sometimes, while working with Python dictionaries we can have problem in which
we need to perform the removal of odd elements from values list of
dictionaries. This can have application in many domains including web
development. Lets discuss certain ways in which this task can be performed.

 **Method #1 : Using list comprehension + dictionary comprehension**  
This is brute force one liner in which this task can be performed. In this, we
remake new dictionary using dictionary comprehension in which filtering data
and iteration in value list is performed using list comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove odd elements from value lists in dictionary

# Using list comprehension + dictionary comprehension

 

# initializing Dictionary

test_dict = {'gfg' : [1, 3, 4, 10], 'is' :
[1, 2, 8], 'best' : [4, 3, 7]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Remove odd elements from value lists in dictionary

# Using list comprehension + dictionary comprehension

res = {key: [idx for idx in val if idx % 2] 

 for key, val in test_dict.items()}

 

# printing result 

print("The filtered values are : " + str(res))   
  
---  
  
__

__

**Output :**

> The original dictionary is : {‘gfg’: [1, 3, 4, 10], ‘best’: [4, 3, 7], ‘is’:
> [1, 2, 8]}  
> The filtered values are : {‘gfg’: [1, 3], ‘is’: [1], ‘best’: [3, 7]}

  

  

**Method #2 : Using dictionary comprehension +filter() + lambda**  
This is yet another way to solve this problem. In this, the task performed by
list comprehension is done using filter() + lambda.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove odd elements from value lists in dictionary

# Using filter() + lambda + dictionary comprehension

 

# initializing Dictionary

test_dict = {'gfg' : [1, 3, 4, 10], 'is' :
[1, 2, 8], 'best' : [4, 3, 7]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Remove odd elements from value lists in dictionary

# Using filter() + lambda + dictionary comprehension

res = {key: list(filter(lambda ele: (ele % 2), val)) 

 for key, val in test_dict.items()}

 

# printing result 

print("The filtered values are : " + str(res))   
  
---  
  
__

__

**Output :**

> The original dictionary is : {‘gfg’: [1, 3, 4, 10], ‘best’: [4, 3, 7], ‘is’:
> [1, 2, 8]}  
> The filtered values are : {‘gfg’: [1, 3], ‘is’: [1], ‘best’: [3, 7]}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

