Python – Initialize dictionary keys with Matrix



Sometimes, while working with Python Data, we can have a problem in which we
need to construct an empty mesh of dictionaries for further population of
data. This problem can have applications in many domains which include data
manipulation. Let’s discuss certain ways in which this task can be performed.

 **Method #1 : Using list comprehension**  
This is one of the way in which this task can be performed. In this, we
initialize the dictionary keys with empty mesh with N by iterating using list
comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Initialize dictionary keys with Matrix

# Using list comprehension

 

# initializing N

num = 4

 

# Initialize dictionary keys with Matrix

# Using list comprehension

res = {'gfg': [[] for _ in range(num)], 'best': [[]
for _ in range(num)]}

 

# printing result 

print("The Initialized dictionary : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The Initialized dictionary : {'gfg': [[], [], [], []], 'best': [[], [], [], []]}
    

**Method #2 : Usingdeepcopy()**  
This task can also be performed using deepcopy(). In this, we perform the task
of performing copy of each dictionary key as non referenced key.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Initialize dictionary keys with Matrix

# Using deepcopy()

from copy import deepcopy

 

# initializing N

num = 4

 

# Initialize dictionary keys with Matrix

# Using deepcopy()

temp = [[] for idx in range(num)]

res = {'gfg': deepcopy(temp), 'best': deepcopy(temp)}

 

# printing result 

print("The Initialized dictionary : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The Initialized dictionary : {'gfg': [[], [], [], []], 'best': [[], [], [], []]}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

