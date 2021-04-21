Python – Compare Dictionaries on certain Keys



Sometimes, while working with Python dictionaries, we can have a problem in
which we need to compare dictionaries for equality on bases in selected keys.
This kind of problem is common and has application in many domains. Lets
discuss certain ways in which this task can be performed.

 **Method #1 : Using loop**  
This is brute force way in which this task can be performed. In this, we
iterate for both the dictionary and manually test for keys equality using
equality operator from selected keys.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Compare Dictionaries on certain Keys

# Using loop

 

# initializing dictionaries

test_dict1 = {'gfg' : 1, 'is' : 2, 'best' : 3,
'for' : 4, 'geeks' : 5}

test_dict2 = {'gfg' : 2, 'is' : 3, 'best' : 3,
'for' : 7, 'geeks' : 5}

 

# printing original dictionaries

print("The original dictionary 1 : " + str(test_dict1))

print("The original dictionary 2 : " + str(test_dict2))

 

# initializing compare keys 

comp_keys = ['best', 'geeks']

 

# Compare Dictionaries on certain Keys

# Using loop

res = True

for key in comp_keys:

 if test_dict1.get(key) != test_dict2.get(key):

 res = False

 break

 

# printing result 

print("Are dictionary equal : " + str(res))   
  
---  
  
__

__

**Output :**

> The original dictionary 1 : {‘geeks’: 5, ‘gfg’: 1, ‘is’: 2, ‘for’: 4,
> ‘best’: 3}  
> The original dictionary 2 : {‘geeks’: 5, ‘gfg’: 2, ‘is’: 3, ‘for’: 7,
> ‘best’: 3}  
> Are dictionary equal : True

  

  

**Method #2 : Usingall()**  
This is one liner alternative to perform this task. In this the functionality
of comparison is done using all(), comparing all required keys.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Compare Dictionaries on certain Keys

# Using all()

 

# initializing dictionaries

test_dict1 = {'gfg' : 1, 'is' : 2, 'best' : 3,
'for' : 4, 'geeks' : 5}

test_dict2 = {'gfg' : 2, 'is' : 3, 'best' : 3,
'for' : 7, 'geeks' : 5}

 

# printing original dictionaries

print("The original dictionary 1 : " + str(test_dict1))

print("The original dictionary 2 : " + str(test_dict2))

 

# initializing compare keys 

comp_keys = ['best', 'geeks']

 

# Compare Dictionaries on certain Keys

# Using all()

res = all(test_dict1.get(key) == test_dict2.get(key) for key
in comp_keys)

 

# printing result 

print("Are dictionary equal : " + str(res))   
  
---  
  
__

__

**Output :**

> The original dictionary 1 : {‘geeks’: 5, ‘gfg’: 1, ‘is’: 2, ‘for’: 4,
> ‘best’: 3}  
> The original dictionary 2 : {‘geeks’: 5, ‘gfg’: 2, ‘is’: 3, ‘for’: 7,
> ‘best’: 3}  
> Are dictionary equal : True

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

