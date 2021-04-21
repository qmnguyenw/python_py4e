Python – Frequency of unequal items in Dictionary



Sometimes, while working with Python, we can come across a problem in which we
need to check for the unequal items count among two dictionaries. This has an
application in cases of web development and other domains as well. Let’s
discuss certain ways in which this task can be performed.

 **Method #1 : Using dictionary comprehension**  
This particular task can be performed in one line using dictionary
comprehension which offers a way of compacting lengthy brute logic and just
checks for unequal items and increments count.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Dissimilar items frequency in Dictionary

# Using dictionary comprehension

 

# initializing dictionaries

test_dict1 = {'gfg' : 1, 'is' : 2, 'best' : 3}

test_dict2 = {'gfg' : 1, 'is' : 2, 'good' : 3}

 

# printing original dictionaries

print("The original dictionary 1 is : " + str(test_dict1))

print("The original dictionary 2 is : " + str(test_dict2))

 

# Dissimilar items frequency in Dictionary

# Using dictionary comprehension

res = {key: test_dict1[key] for key in test_dict1 if key
not in test_dict2}

 

# printing result

print("The number of uncommon items are : " + str(len(res)))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary 1 is : {'best': 3, 'is': 2, 'gfg': 1}
    The original dictionary 2 is : {'good': 3, 'is': 2, 'gfg': 1}
    The number of uncommon items are : 1
    

**Method #2 : Using set() \+ XOR operator + items()**  
The combination of above methods can be used to perform this particular task.
In this, the set function removes duplicates and XOR operator computes the
matched items. Result can be computed by subtracting original dict. length by
new dict. length.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Dissimilar items frequency in Dictionary

# Using set() + XOR operator + items()

 

# initializing dictionaries

test_dict1 = {'gfg' : 1, 'is' : 2, 'best' : 3}

test_dict2 = {'gfg' : 1, 'is' : 2, 'good' : 3}

 

# printing original dictionaries

print("The original dictionary 1 is : " + str(test_dict1))

print("The original dictionary 2 is : " + str(test_dict2))

 

# Dissimilar items frequency in Dictionary

# Using set() + XOR operator + items()

res = set(test_dict1.items()) ^ set(test_dict2.items())

 

# printing result

print("The number of uncommon items are : " +
str(len(test_dict1) - len(res)))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary 1 is : {'best': 3, 'is': 2, 'gfg': 1}
    The original dictionary 2 is : {'good': 3, 'is': 2, 'gfg': 1}
    The number of uncommon items are : 1
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

