Python program to divide dictionary and its keys into K equal dictionaries



Given a dictionary, divide it into an equal dictionary list of size k, by
dividing each key’s value.

>  **Input** : test_dict = {“Gfg” : 9, “is” : 6, “best” : 12} , K = 3  
> **Output** : [{‘Gfg’: 3.0, ‘is’: 2.0, ‘best’: 4.0}, {‘Gfg’: 3.0, ‘is’: 2.0,
> ‘best’: 4.0}, {‘Gfg’: 3.0, ‘is’: 2.0, ‘best’: 4.0}]  
> **Explanation** : Values distributed equally among dictionaries.
>
>  **Input** : test_dict = {“Gfg” : 6, “is” : 4, “best” : 2} , K = 2  
> **Output** : [{‘Gfg’: 3.0, ‘is’: 2.0, ‘best’: 1.0}, {‘Gfg’: 3.0, ‘is’: 2.0,
> ‘best’: 1.0}]  
> **Explanation** : Values distributed equally among dictionaries.

 **Method #1: Using loop**

This is one of the ways in which this task can be performed. In this, we
compute each required key’s value and append each dictionary into the
dictionaries list.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Divide dictionary into K equal dictionaries

# Using loop

 

# initializing dictionary

test_dict = {"Gfg": 20, "is": 36, "best": 100}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing size

K = 4

 

# contructing new dict

temp = dict()

for key in test_dict:

 temp[key] = test_dict[key] / 4

 

# creating list

res = []

for idx in range(K):

 res.append(temp)

 

# printing result

print("Required dictionary list : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original dictionary is : {‘Gfg’: 20, ‘is’: 36, ‘best’: 100}  
> Required dictionary list : [{‘Gfg’: 5.0, ‘is’: 9.0, ‘best’: 25.0}, {‘Gfg’:
> 5.0, ‘is’: 9.0, ‘best’: 25.0}, {‘Gfg’: 5.0, ‘is’: 9.0, ‘best’: 25.0},
> {‘Gfg’: 5.0, ‘is’: 9.0, ‘best’: 25.0}]

 **Method #2 : Using dictionary comprehension + list comprehension**

This is yet another way in which this task can be performed. In this, we form
dictionary using dictionary comprehension and list using list comprehension as
a shorthand to solve this problem.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Divide dictionary into K equal dictionaries

# Using dictionary comprehension + list comprehension

 

 

# function to divide dictionary

# and keys into K equal dictionaries

def divideDictKeys(dictionary, K):

 

 # contructing new dict

 # using dictionary comprehension

 temp = {key: test_dict[key] / K for key in test_dict}

 

 # creating list

 # using list comprehension

 res = [temp for idx in range(K)]

 

 return str(res)

 

 

# driver code

 

# initializing dictionary

test_dict = {"Gfg": 20, "is": 36, "best": 100}

 

# initializing size

K = 4

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# printing result

print("Required dictionary list : " + divideDictKeys(test_dict, K))  
  
---  
  
 __

 __

 **Output:**

> The original dictionary is : {‘Gfg’: 20, ‘is’: 36, ‘best’: 100}  
> Required dictionary list : [{‘Gfg’: 5.0, ‘is’: 9.0, ‘best’: 25.0}, {‘Gfg’:
> 5.0, ‘is’: 9.0, ‘best’: 25.0}, {‘Gfg’: 5.0, ‘is’: 9.0, ‘best’: 25.0},
> {‘Gfg’: 5.0, ‘is’: 9.0, ‘best’: 25.0}]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

