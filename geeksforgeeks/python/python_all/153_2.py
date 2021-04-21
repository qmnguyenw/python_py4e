Python | Merging two list of dictionaries



Given two list of dictionaries, the task is to merge these two lists of
dictionaries based on some value.

 **Method #1:** Using defaultdict and extend to merge two list of
dictionaries based on _school_id_.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to merge two list of dictionaries

# based on some value.

 

from collections import defaultdict

 

# List initialization

Input1 = [{'roll_no': ['123445', '1212'], 'school_id':
1},

 {'roll_no': ['HA-4848231'], 'school_id': 2}]

 

Input2 = [{'roll_no': ['473427'], 'school_id': 2},

 {'roll_no': ['092112'], 'school_id': 5}]

 

 

# Using defaultdic

temp = defaultdict(list) 

 

# Using extend

for elem in Input1:

 temp[elem['school_id']].extend(elem['roll_no'])

 

for elem in Input2:

 temp[elem['school_id']].extend(elem['roll_no'])

 

Output = [{"roll_no":y, "school_id":x} for x, y in
temp.items()]

 

# printing

print(Output)  
  
---  
  
 __

 __

 **Output:**

> [{‘school_id’: 1, ‘roll_no’: [‘123445’, ‘1212’]}, {‘school_id’: 2,
> ‘roll_no’: [‘HA-4848231’, ‘473427’]}, {‘school_id’: 5, ‘roll_no’:
> [‘092112’]}]

  
**Method #2: Usingextend() only.**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to merge two list of dictionaries

# based on some value.

 

# List initialization

Input1 = [{'roll_no': ['123445', '1212'], 'school_id':
1},

 {'roll_no': ['HA-4848231'], 'school_id': 2}]

Input2 = [{'roll_no': ['473427'], 'school_id': 2},

 {'roll_no': ['092112'], 'school_id': 5}]

 

# Iterating and using extend to convert

for elm2 in Input2:

 

 for elm1 in Input1:

 if elm2['school_id'] == elm1['school_id']:

 elm1['roll_no'].extend(elm2['roll_no'])

 break

 else:

 Input1.append(elm2)

 

# printing 

print(Input1)  
  
---  
  
 __

 __

 **Output:**

> [{‘school_id’: 1, ‘roll_no’: [‘123445’, ‘1212’]}, {‘school_id’: 2,
> ‘roll_no’: [‘HA-4848231’, ‘473427’]}, {‘school_id’: 5, ‘roll_no’:
> [‘092112’]}]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

