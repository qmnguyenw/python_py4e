Python – Maximum record value key in dictionary



Sometimes, while working with dictionary records, we can have problem in which
we need to find the key with maximum value of particular key of nested records
in list. This can have application in domains such as web development and
Machine Learning. Lets discuss certain ways in which this task can be
performed.

 **Method #1 : Using loop**  
This is brute force way in which this task can be performed. In this, we
iterate through each key for keys and assign to max, the maximum of required
key in nested record.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Maximum record value key in dictionary

# Using loop

 

# initializing dictionary

test_dict = {'gfg' : {'Manjeet' : 5, 'Himani' : 10},

 'is' : {'Manjeet' : 8, 'Himani' : 9},

 'best' : {'Manjeet' : 10, 'Himani' : 15}}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing search key

key = 'Himani'

 

# Maximum record value key in dictionary

# Using loop

res = None

res_max = 0

for sub in test_dict:

 if test_dict[sub][key] > res_max:

 res_max = test_dict[sub][key]

 res = sub

 

# printing result 

print("The required key is : " + str(res))   
  
---  
  
__

__

**Output :**

> The original dictionary is : {‘best’: {‘Himani’: 15, ‘Manjeet’: 10}, ‘gfg’:
> {‘Himani’: 10, ‘Manjeet’: 5}, ‘is’: {‘Himani’: 9, ‘Manjeet’: 8}}  
> The required key is : best

  

  

**Method #2 : Usingmax() \+ lambda function**  
This is one liner approach to solve this problem. In this, we perform the task
of iteration using max key argument, passing a lambda function which binds the
required logic.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Maximum record value key in dictionary

# Using max() + lambda function

 

# initializing dictionary

test_dict = {'gfg' : {'Manjeet' : 5, 'Himani' : 10},

 'is' : {'Manjeet' : 8, 'Himani' : 9},

 'best' : {'Manjeet' : 10, 'Himani' : 15}}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing search key

key = 'Himani'

 

# Maximum record value key in dictionary

# Using max() + lambda function

res = max(test_dict, key = lambda sub: test_dict[sub][key])

 

# printing result 

print("The required key is : " + str(res))   
  
---  
  
__

__

**Output :**

> The original dictionary is : {‘best’: {‘Himani’: 15, ‘Manjeet’: 10}, ‘gfg’:
> {‘Himani’: 10, ‘Manjeet’: 5}, ‘is’: {‘Himani’: 9, ‘Manjeet’: 8}}  
> The required key is : best

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

