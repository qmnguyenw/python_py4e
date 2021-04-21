Python – Mapping key values to Dictionary



Sometimes, while working with Python records, we can have a problem in which
we need to extract key’s value as the dictionary values required. This can
have application in domains in which we require to reduce the data storage and
in web development domain. Lets discuss certain ways in which this task can be
performed.

 **Method #1 : Using dictionary comprehension**  
This is one of the way in which we can solve this problem. In this, we iterate
the list keys and construct dictionary of required key-value pairs using
dictionary comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Mapping key values to Dictionary

# Using dictionary comprehension

 

# initializing list

test_list = [{'name' : 'Manjeet', 'age' : 23}, 

 {'name' : 'Akshat', 'age' : 22},

 {'name' : 'Nikhil', 'age' : 21}]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Mapping key values to Dictionary

# Using dictionary comprehension

res = {sub['name'] : sub['age'] for sub in test_list}

 

# printing result 

print("The flattened dictionary is : " + str(dict(res)))   
  
---  
  
__

__

**Output :**

> The original list is : [{‘age’: 23, ‘name’: ‘Manjeet’}, {‘age’: 22, ‘name’:
> ‘Akshat’}, {‘age’: 21, ‘name’: ‘Nikhil’}]  
> The flattened dictionary is : {‘Manjeet’: 23, ‘Akshat’: 22, ‘Nikhil’: 21}

  

  

**Method #2 : Usingdict() + values()**  
The combination of above functions can also be used to solve this problem. In
this, we perform conversion to dictionary using dict() and extract dictionary
values using values().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Mapping key values to Dictionary

# Using dict() + values()

 

# initializing list

test_list = [{'name' : 'Manjeet', 'age' : 23}, 

 {'name' : 'Akshat', 'age' : 22},

 {'name' : 'Nikhil', 'age' : 21}]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Mapping key values to Dictionary

# Using dict() + values()

res = dict(sub.values() for sub in test_list)

 

# printing result 

print("The flattened dictionary is : " + str(dict(res)))   
  
---  
  
__

__

**Output :**

> The original list is : [{‘age’: 23, ‘name’: ‘Manjeet’}, {‘age’: 22, ‘name’:
> ‘Akshat’}, {‘age’: 21, ‘name’: ‘Nikhil’}]  
> The flattened dictionary is : {‘Manjeet’: 23, ‘Akshat’: 22, ‘Nikhil’: 21}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

