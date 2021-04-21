Python | Remove duplicate dictionaries from nested dictionary



Given a nested dictionary, the task is to remove duplicate dictionaries from
the dictionary. Given below are few methods to complete the given task.

 **Method #1: Using Naive Method**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# for removing duplicate values from dictionary

 

# initialising dictionary

ini_dict = {'a':{'b':1, 'c':2},
'b':{'b':1, 'c':2}, 

 'c':{'a':2, 'b':3}, 'd':{'a':2,
'b':7}}

 

# printing initial_dictionary

print ("initial dictionary", str(ini_dict))

 

# code to remove duplicates

result = {}

 

for key, value in ini_dict.items():

 if value not in result.values():

 result[key] = value

 

# printing result

print ("result", str(result))  
  
---  
  
 __

 __

 **Output:**

> initial dictionary {‘c’: {‘a’: 2, ‘b’: 3}, ‘d’: {‘a’: 2, ‘b’: 7}, ‘a’: {‘c’:
> 2, ‘b’: 1}, ‘b’: {‘c’: 2, ‘b’: 1}}  
> result {‘c’: {‘a’: 2, ‘b’: 3}, ‘d’: {‘a’: 2, ‘b’: 7}, ‘a’: {‘c’: 2, ‘b’: 1}}

  
**Method #2: Using _sorted_ and _set_**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# for removing duplicate values from dictionary

 

# initialising dictionary

ini_dict = {'a':{'b':1, 'c':2},
'b':{'b':1, 'c':2},

 'c':{'a':2, 'b':3}, 'd':{'a':2,
'b':7}}

 

# printing initial_dictionary

print ("initial dictionary", str(ini_dict))

 

# code to remove duplicates

keep = set({repr(sorted(value.items())):key

 for key, value in ini_dict.items()}.values())

 

for key in list(ini_dict):

 if key not in keep:

 del ini_dict[key]

 

# printing result

print ("result", str(ini_dict))  
  
---  
  
 __

 __

 **Output:**

> initial dictionary {‘a’: {‘b’: 1, ‘c’: 2}, ‘b’: {‘b’: 1, ‘c’: 2}, ‘c’: {‘a’:
> 2, ‘b’: 3}, ‘d’: {‘a’: 2, ‘b’: 7}}  
> result {‘b’: {‘b’: 1, ‘c’: 2}, ‘c’: {‘a’: 2, ‘b’: 3}, ‘d’: {‘a’: 2, ‘b’: 7}}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

