Python – Value length dictionary



Sometimes, while working with Python dictionary, we can have problem in which
we need to map the value of dictionary to its length. This kind of application
can come in many domains including web development and day-day programming.
Lets discuss certain ways in which this task can be performed.

 **Method #1 : Using loop +len()**  
This is one of the way in which this task can be performed. In this, we
extract the value of dictionary and map it with its length computed using
len().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Value length dictionary

# Using loop + len()

 

# initializing dictionary

test_dict = {1 : 'gfg', 2 : 'is', 3 : 'best'}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Value length dictionary

# Using loop + len()

res = {}

for val in test_dict.values():

 res[val] = len(val)

 

# printing result 

print("The value-size mapped dictionary is : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original dictionary is : {1: 'gfg', 2: 'is', 3: 'best'}
    The value-size mapped dictionary is : {'is': 2, 'best': 4, 'gfg': 3}
    

**Method #2 : Using dictionary comprehension**  
This task can also be performed using dictionary comprehension. In this, we
perform task similarly as above method, just in smaller form.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Value length dictionary

# Using dictionary comprehension

 

# initializing dictionary

test_dict = {1 : 'gfg', 2 : 'is', 3 : 'best'}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Value length dictionary

# Using dictionary comprehension

res = {val: len(val) for val in test_dict.values()}

 

# printing result 

print("The value-size mapped dictionary is : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original dictionary is : {1: 'gfg', 2: 'is', 3: 'best'}
    The value-size mapped dictionary is : {'is': 2, 'best': 4, 'gfg': 3}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

