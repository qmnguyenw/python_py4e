Python – Filter and Double keys greater than K



Sometimes, while working with Python dictionaries, we can have the task of
extracting certain keys after manipulation and filtration, both at once. This
problem can be generalized for other values and operations as well. This has
applications in many domains such as day-day programming and web development.
Let’s discuss certain ways in which this task can be performed.

 **Method #1 : Using loop**  
This is one way to solve this problem. In this, we adopt brute force way to
extract only filtered elements and store after doubling them.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Filter and Double keys greater than K

# Using loop

 

# initializing dictionary

test_dict = {'Gfg' : 4, 'is' : 2, 'best': 3,
'for' : 6, 'geeks' : 1}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# initializing K

K = 2

 

# Filter and Double keys greater than K

# Using loop

res = dict()

for key, val in test_dict.items():

 if val > K:

 res[key] = val * 2

 

# printing result 

print("The filtred dictionary : " + str(res))   
  
---  
  
__

__

**Output :**

> The original dictionary : {‘geeks’: 1, ‘for’: 6, ‘Gfg’: 4, ‘is’: 2, ‘best’:
> 3}  
> The filtred dictionary : {‘for’: 12, ‘Gfg’: 8, ‘best’: 6}

  

  

**Method #2 : Using dictionary comprehension**  
This is yet another way to perform this task. In this, we perform task in
similar way as above method, but in a more compact way.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Filter and Double keys greater than K

# Using dictionary comprehension

 

# initializing dictionary

test_dict = {'Gfg' : 4, 'is' : 2, 'best': 3,
'for' : 6, 'geeks' : 1}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# initializing K

K = 2

 

# Filter and Double keys greater than K

# Using dictionary comprehension

res = {key : val * 2 for key, val in test_dict.items() if
val > K}

 

# printing result 

print("The filtred dictionary : " + str(res))   
  
---  
  
__

__

**Output :**

> The original dictionary : {‘geeks’: 1, ‘for’: 6, ‘Gfg’: 4, ‘is’: 2, ‘best’:
> 3}  
> The filtred dictionary : {‘for’: 12, ‘Gfg’: 8, ‘best’: 6}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

