Python | Convert Character Matrix to single String



Sometimes, while working with Python strings, we can have an option in which
we need to perform the task of converting character matrix to a single string.
This can have applications in domains in which we need to work with data. Lets
discuss certain ways in which we can perform this task.

 **Method #1 : Usingjoin() \+ list comprehension**  
The combination of above functionalities can be used to perform this task. In
this, we just iterate for all lists and join them using join().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Character Matrix to single String

# Using join() + list comprehension

 

# initializing list

test_list = [['g', 'f', 'g'], ['i', 's'], ['b',
'e', 's', 't']]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Convert Character Matrix to single String

# Using join() + list comprehension

res = ''.join(ele for sub in test_list for ele in sub)

 

# printing result 

print("The String after join : " + res)   
  
---  
  
__

__

**Output :**

    
    
    The original list is : [['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't']]
    The String after join : gfgisbest
    

**Method #2 : Usingjoin() + chain()**  
The combination of above functionalities can be used to perform this task. In
this, we perform the task performed by list comprehension by chain().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Character Matrix to single String

# Using join() + chain()

from itertools import chain

 

# initializing list

test_list = [['g', 'f', 'g'], ['i', 's'], ['b',
'e', 's', 't']]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Convert Character Matrix to single String

# Using join() + chain()

res = "".join(chain(*test_list))

 

# printing result 

print("The String after join : " + res)   
  
---  
  
__

__

**Output :**

    
    
    The original list is : [['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't']]
    The String after join : gfgisbest
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

