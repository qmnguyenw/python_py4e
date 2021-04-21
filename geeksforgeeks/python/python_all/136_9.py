Python | List value merge in dictionary



Sometimes, while working with dictionaries, we can have a problem in which we
have many dictionaries and we are required to merge like keys. This problem
seems common, but complex is if the values of keys are list and we need to add
elements to list of like keys. Let’s discuss way in which this problem can be
solved.

 **Method : Using list comprehension +items()**  
This problem can be solved using list comprehension that can be used to merge
the list content and also the items method which can be employed to get the
dictionary keys and values.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# List value merge in dictionary

# Using items() + list comprehension

 

# initializing dictionaries

test_dict1 = {'Gfg' : [1, 2, 3], 'for' : [2,
4], 'CS' : [7, 8]}

test_dict2 = {'Gfg' : [10, 11], 'for' : [5], 'CS'
: [0, 18]}

 

# printing original dictionaries

print("The original dictionary 1 is : " + str(test_dict1))

print("The original dictionary 2 is : " + str(test_dict2))

 

# Using items() + list comprehension

# List value merge in dictionary

res = {key: value + test_dict2[key] for key, value in
test_dict1.items()}

 

# printing result 

print("The merged dictionary is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original dictionary 1 is : {‘for’: [2, 4], ‘CS’: [7, 8], ‘Gfg’: [1, 2,
> 3]}  
> The original dictionary 2 is : {‘for’: [5], ‘CS’: [0, 18], ‘Gfg’: [10, 11]}  
> The merged dictionary is : {‘for’: [2, 4, 5], ‘CS’: [7, 8, 0, 18], ‘Gfg’:
> [1, 2, 3, 10, 11]}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

