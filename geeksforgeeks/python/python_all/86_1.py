Python – Assign values to initialized dictionary keys



Sometimes, while working with python dictionaries, we can have a problem in
which we need to initialize dictionary keys with values. We save a mesh of
keys to be initialized. This usually happens during web development while
working with JSON data. Lets discuss certain ways in which this task can be
performed.

 **Method #1 : Usingdict() + zip()**  
The combination of above methods can be used to perform this task. In this, we
allot the list values to already constructed mesh and zip() helps in mapping
values as per list index.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Assign values to initialized dictionary keys

# using dict() + zip()

 

# initializing dictionary 

test_dict = {'gfg' : '', 'is' : '', 'best' : ''} 

 

# Initializing list 

test_list = ['A', 'B', 'C']

 

# printing original dictionary 

print("The original dictionary is : " + str(test_dict)) 

 

# Assign values to initialized dictionary keys

# using dict() + zip()

res = dict(zip(test_dict, test_list))

 

# printing result 

print("The assigned value dictionary is : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original dictionary is : {'is': '', 'best': '', 'gfg': ''}
    The assigned value dictionary is : {'gfg': 'C', 'best': 'B', 'is': 'A'}
    

**Method #2 : Using loop +zip()**  
This is extended way in which this task can be performed. In this, we iterate
through the zipped list and assign value to dictionary.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Assign values to initialized dictionary keys

# using loop + zip()

 

# initializing dictionary 

test_dict = {'gfg' : '', 'is' : '', 'best' : ''} 

 

# Initializing list 

test_list = ['A', 'B', 'C']

 

# printing original dictionary 

print("The original dictionary is : " + str(test_dict)) 

 

# Assign values to initialized dictionary keys

# using loop + zip()

for key, val in zip(test_dict, test_list):

 test_dict[key] = val

 

# printing result 

print("The assigned value dictionary is : " + str(test_dict))   
  
---  
  
__

__

**Output :**

    
    
    The original dictionary is : {'is': '', 'best': '', 'gfg': ''}
    The assigned value dictionary is : {'gfg': 'C', 'best': 'B', 'is': 'A'}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

