Python Nested Dictionary



 **Prerequisite –**Python dictionary

A Dictionary in Python works similar to the Dictionary in the real world. Keys
of a Dictionary must be unique and of immutable data type such as Strings,
Integers and tuples, but the key-values can be repeated and be of any type.

 **Nested Dictionary:** Nesting Dictionary means putting a dictionary inside
another dictionary. Nesting is of great use as the kind of information we can
model in programs is expanded greatly.

 __

 __  
 __

 __

 __  
 __  
 __

nested_dict= { 'dict1': {'key_A': 'value_A'},

 'dict2': {'key_B': 'value_B'}}  
  
---  
  
 __

 __

![](https://media.geeksforgeeks.org/wp-content/uploads/Dictionary_inmage.jpg)

 __

 __  
 __

 __

 __  
 __  
 __

# As shown in image

 

# Creating a Nested Dictionary 

Dict = {1: 'Geeks', 2: 'For', 3: {'A' :
'Welcome', 'B' : 'To', 'C' : 'Geeks'}}  
  
---  
  
 __

 __

#### Creating a Nested Dictionary

In Python, a Nested dictionary can be created by placing the comma-separated
dictionaries enclosed withing braces.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Empty nested dictionary

Dict = { 'Dict1': { }, 

 'Dict2': { }}

print("Nested dictionary 1-")

print(Dict)

 

# Nested dictionary having same keys

Dict = { 'Dict1': {'name': 'Ali', 'age': '19'},

 'Dict2': {'name': 'Bob', 'age': '25'}}

print("\nNested dictionary 2-")

print(Dict)

 

# Nested dictionary of mixed dictionary keys

Dict = { 'Dict1': {1: 'G', 2: 'F', 3: 'G'}, 

 'Dict2': {'Name': 'Geeks', 1: [1, 2]} }

print("\nNested dictionary 3-")

print(Dict)  
  
---  
  
 __

 __

 **Output:**

    
    
    Nested dictionary 1-
    {'Dict1': {}, 'Dict2': {}}
    
    Nested dictionary 2-
    {'Dict1': {'name': 'Ali', 'age': '19'}, 'Dict2': {'name': 'Bob', 'age': '25'}}
    
    Nested dictionary 3-
    {'Dict1': {1: 'G', 2: 'F', 3: 'G'}, 'Dict2': {1: [1, 2], 'Name': 'Geeks'}}
    

#### Adding elements to a Nested Dictionary

Addition of elements to a nested Dictionary can be done in multiple ways. One
way to add a dictionary in the Nested dictionary is to add values one be one,
Nested_dict[dict][key] = 'value'. Another way is to add the whole dictionary
in one go, Nested_dict[dict] = { 'key': 'value'}.

 __

 __  
 __

 __

 __  
 __  
 __

Dict = { }

print("Initial nested dictionary:-")

print(Dict)

 

Dict['Dict1'] = {}

 

# Adding elements one at a time 

Dict['Dict1']['name'] = 'Bob'

Dict['Dict1']['age'] = 21

print("\nAfter adding dictionary Dict1")

print(Dict)

 

# Adding whole dictionary

Dict['Dict2'] = {'name': 'Cara', 'age': 25}

print("\nAfter adding dictionary Dict1")

print(Dict)  
  
---  
  
 __

 __

 **Output:**

    
    
    Initial nested dictionary:-
    {}
    
    After adding dictionary Dict1
    {'Dict1': {'age': 21, 'name': 'Bob'}}
    
    After adding dictionary Dict1
    {'Dict1': {'age': 21, 'name': 'Bob'}, 'Dict2': {'age': 25, 'name': 'Cara'}}
    

#### Access elements of a Nested Dictionary

In order to access the value of any key in nested dictionary, use indexing
[] syntax.

 __

 __  
 __

 __

 __  
 __  
 __

# Nested dictionary having same keys

Dict = { 'Dict1': {'name': 'Ali', 'age': '19'},

 'Dict2': {'name': 'Bob', 'age': '25'}}

 

# Prints value corresponding to key 'name' in Dict1

print(Dict['Dict1']['name'])

 

# Prints value corresponding to key 'age' in Dict2

print(Dict['Dict2']['age'])  
  
---  
  
 __

 __

 **Output:**

    
    
    Ali
    25

#### Deleting dictionaries from a Nested Dictionary

Deletion of dictionaries from a nested dictionary can be done either by using
del keyword or by using pop() function.

 __

 __  
 __

 __

 __  
 __  
 __

Dict = {'Dict1': {'name': 'Ali', 'age': 19},

 'Dict2': {'name': 'Bob', 'age': 21}}

print("Initial nested dictionary:-")

print(Dict)

 

# Deleting dictionary using del keyword 

print("\nDeleting Dict2:-")

del Dict['Dict2']

print(Dict)

 

# Deleting dictionary using pop function

print("\nDeleting Dict1:-")

Dict.pop('Dict1') 

print (Dict)  
  
---  
  
 __

 __

 **Output:**

    
    
    Initial nested dictionary:-
    {'Dict2': {'name': 'Bob', 'age': 21}, 'Dict1': {'name': 'Ali', 'age': 19}}
    
    Deleting Dict2:-
    {'Dict1': {'name': 'Ali', 'age': 19}}
    
    Deleting Dict1:-
    {}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

