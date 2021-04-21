Python – Maximum Value in Nested Dictionary



Sometimes, while working with python dictionary, we can have problem in which
each key in itself is a record with several keys and we desire to substitute
the value as maximum value of keys of dictionary. This kind of problem can
have application in many domains that involves data. Lets discuss certain ways
in which this task can be performed.

 **Method #1 : Using loop**  
This is brute way in which this task can be performed. In this, we iterate for
each key’s keys to get maximum value and set in resultant dictionary.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Maximum Value in Nested Dictionary

# Using loop

 

# initializing dictionary

test_dict = {'gfg' : {'a' : 15, 'b' : 14},

 'is' : {'d' : 2, 'e' : 10, 'f' : 3},

 'best' : {'g' : 19}}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Maximum Value in Nested Dictionary

# Using loop

res = {}

for key, val in test_dict.items():

 max_val = 0

 for ele in val.values():

 if ele > max_val:

 max_val = ele

 res[key] = max_val

 

# printing result 

print("The modified dictionary : " + str(res))   
  
---  
  
__

__

**Output :**

> The original dictionary is : {‘is’: {‘f’: 3, ‘e’: 10, ‘d’: 2}, ‘gfg’: {‘a’:
> 15, ‘b’: 14}, ‘best’: {‘g’: 19}}  
> The modified dictionary : {‘best’: 19, ‘is’: 10, ‘gfg’: 15}

  

  

**Method #2 : Usingmax() \+ dictionary comprehension**  
This is yet another way in which this task can be performed. In this, we
perform the task of extracting maximum using max() and dictionary
comprehension is used to iterate and construct new dictionary.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Maximum Value in Nested Dictionary

# Using max() + dictionary comprehension

 

# initializing dictionary

test_dict = {'gfg' : {'a' : 15, 'b' : 14},

 'is' : {'d' : 2, 'e' : 10, 'f' : 3},

 'best' : {'g' : 19}}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Maximum Value in Nested Dictionary

# Using max() + dictionary comprehension

res = {key: max(val.values()) for key, val in
test_dict.items()}

 

# printing result 

print("The modified dictionary : " + str(res))   
  
---  
  
__

__

**Output :**

> The original dictionary is : {‘is’: {‘f’: 3, ‘e’: 10, ‘d’: 2}, ‘gfg’: {‘a’:
> 15, ‘b’: 14}, ‘best’: {‘g’: 19}}  
> The modified dictionary : {‘best’: 19, ‘is’: 10, ‘gfg’: 15}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

