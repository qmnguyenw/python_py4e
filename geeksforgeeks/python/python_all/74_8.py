Python – Extract Equal Pair Dictionary



Sometimes, while working with Python dictionary, we can have problem in which
we need to create a new dictionary of the existing dictionary having tuple as
key. We desire to create singlton key dictionary with keys only where both
elements of pair are equal. This can have application in many domains. Let’s
discuss certain ways in which this task can be performed.

 **Method #1 : Using loop**  
This is brute way in which this task can be performed. In this, we iterate for
each element of tuple dictionary and compare for equality to create new
dictionary.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract Equal Pair Dictionary 

# Using loop

 

# initializing dictionary

test_dict = { (1, 1) : 4, (2, 3) : 6, (3,
3) : 7, (5, 2) : 10, (2, 2) : 11}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Extract Equal Pair Dictionary 

# Using loops

res = dict()

for key, val in test_dict.items():

 if key[0] == key[1]:

 res[key[0]] = val

 

# printing result 

print("The dictionary after equality testing : " + str(res))   
  
---  
  
__

__

**Output :**

> The original dictionary is : {(5, 2): 10, (2, 2): 11, (2, 3): 6, (1, 1): 4,
> (3, 3): 7}  
> The dictionary after equality testing : {1: 4, 2: 11, 3: 7}

  

  

**Method #2 : Using dictionary comprehension**  
This is yet another way in which this task can be performed. In this we use
dictionary comprehension instead of loop to provide shorthand.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract Equal Pair Dictionary 

# Using dictionary comprehension

 

# initializing dictionary

test_dict = { (1, 1) : 4, (2, 3) : 6, (3,
3) : 7, (5, 2) : 10, (2, 2) : 11}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Extract Equal Pair Dictionary 

# Using dictionary comprehension

res = {idx[0] : j for idx, j in test_dict.items() if
idx[0] == idx[1]}

 

# printing result 

print("The dictionary after equality testing : " + str(res))   
  
---  
  
__

__

**Output :**

> The original dictionary is : {(5, 2): 10, (2, 2): 11, (2, 3): 6, (1, 1): 4,
> (3, 3): 7}  
> The dictionary after equality testing : {1: 4, 2: 11, 3: 7}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

