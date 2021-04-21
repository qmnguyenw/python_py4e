Python – Update dictionary with other dictionary



Sometimes, while working with Python dictionaries, we can have problem in
which we need to perform the update of dictionary with other keys of
dictionary. This can have applications in domains in which we need to add
certain records to previously captured records. Let’s discuss certain ways in
which this task can be performed.

 **Method #1 : Using loop**  
This is a brute force way in which this task can be performed. In this, we
check for keys in other dictionary, and add the items in new dictionary.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Update dictionary with other dictionary

# Using loop

 

# initializing dictionaries

test_dict1 = {'gfg' : 1, 'best' : 2, 'for' : 4,
'geeks' : 6}

test_dict2 = {'for' : 3, 'geeks' : 5}

 

# printing original dictionaries

print("The original dictionary 1 is : " + str(test_dict1))

print("The original dictionary 2 is : " + str(test_dict2))

 

# Update dictionary with other dictionary

# Using loop

for key in test_dict1:

 if key in test_dict2:

 test_dict1[key] = test_dict2[key]

 

# printing result 

print("The updated dictionary is : " + str(test_dict1))   
  
---  
  
__

__

**Output :**

> The original dictionary 1 is : {‘best’: 2, ‘for’: 4, ‘gfg’: 1, ‘geeks’: 6}  
> The original dictionary 2 is : {‘for’: 3, ‘geeks’: 5}  
> The updated dictionary is : {‘best’: 2, ‘for’: 3, ‘gfg’: 1, ‘geeks’: 5}

  

  

**Method #2 : Using dictionary comprehension**  
This is yet another way in which this task can be performed. In this, we
iterate for dictionary and perform update in single line using comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Update dictionary with other dictionary

# Using dictionary comprehension

 

# initializing dictionaries

test_dict1 = {'gfg' : 1, 'best' : 2, 'for' : 4,
'geeks' : 6}

test_dict2 = {'for' : 3, 'geeks' : 5}

 

# printing original dictionaries

print("The original dictionary 1 is : " + str(test_dict1))

print("The original dictionary 2 is : " + str(test_dict2))

 

# Update dictionary with other dictionary

# Using dictionary comprehension

res = {key : test_dict2.get(key, val) for key, val in
test_dict1.items()}

 

# printing result 

print("The updated dictionary is : " + str(res))   
  
---  
  
__

__

**Output :**

> The original dictionary 1 is : {‘best’: 2, ‘for’: 4, ‘gfg’: 1, ‘geeks’: 6}  
> The original dictionary 2 is : {‘for’: 3, ‘geeks’: 5}  
> The updated dictionary is : {‘best’: 2, ‘for’: 3, ‘gfg’: 1, ‘geeks’: 5}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

