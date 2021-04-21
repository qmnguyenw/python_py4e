Python – Characters Index occurrences in String



Sometimes, while working with Python Strings, we can have a problem in which
we need to check for all the characters indices. The position where they
occur. This kind of application can come in many domains. Lets discuss certain
ways in which this task can be performed.

 **Method #1 : Usingset() + regex + list comprehension + replace()**  
The combination of above functions can be used to perform this task. In this,
set() is used to get elements whose frequency has to be computed. The task of
assembling to dictionary accordingly is performed using regex function and
list comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Characters Index occurrences in String

# Using regex + set() + list comprehension + replace()

import re 

 

# initializing string

test_str = "Gfg is best for geeks"

 

# printing original string

print("The original string is : " + test_str)

 

# Characters Index occurrences in String

# Using regex + set() + list comprehension + replace()

temp = set(test_str.replace(' ', ''))

res = {ele: [sub.start() for sub in re.finditer(ele, test_str)]
for ele in temp}

 

# printing result 

print("Characters frequency index dictionary : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : Gfg is best for geeks
    Characters frequency index dictionary : {'g': [2, 16], 'k': [19], 't': [10], 'G': [0], 'b': [7], 'i': [4], 'r': [14], 'f': [1, 12], 's': [5, 9, 20], 'o': [13], 'e': [8, 17, 18]}
    

**Method #2 : Using loop +enumerate()**  
This is yet another way in which this task can be performed. In this we create
a dictionary and then iterate the string to map the characters with their
respective characters.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Characters Index occurrences in String

# Using loop + enumerate()

import re 

 

# initializing string

test_str = "Gfg is best for geeks"

 

# printing original string

print("The original string is : " + test_str)

 

# Characters Index occurrences in String

# Using loop + enumerate()

res = {ele : [] for ele in test_str} 

for idx, ele in enumerate(test_str):

 res[ele].append(idx)

 

# printing result 

print("Characters frequency index dictionary : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : Gfg is best for geeks
    Characters frequency index dictionary : {'g': [2, 16], 'k': [19], 't': [10], 'G': [0], 'b': [7], 'i': [4], 'r': [14], 'f': [1, 12], 's': [5, 9, 20], 'o': [13], 'e': [8, 17, 18]}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

