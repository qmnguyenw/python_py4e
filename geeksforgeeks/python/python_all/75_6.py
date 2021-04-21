Python – Test Boolean Value of Dictionary



Sometimes, while working with data, we have a problem in which we need to
accept or reject a dictionary on the basis of its true value, i.e all the keys
are Boolean true or not. This kind of problem has possible applications in
data preprocessing domains. Let’s discuss certain ways in which this task can
be performed.

 **Method #1 : Using loop**  
This is brute force method to solve this problem. In this, we iterate for each
key and tag it as false if we find first occurrence of false value and break
from loop.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test Boolean Value of Dictionary

# Using loop

 

# initializing dictionary

test_dict = {'gfg' : True, 'is' : False, 'best' :
True}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Test Boolean Value of Dictionary

# Using loop

res = True

for ele in test_dict:

 if not test_dict[ele]:

 res = False

 break

 

# printing result 

print("Is Dictionary True ? : " + str(res))   
  
---  
  
__

__

**Output :**

> The original dictionary is : {‘is’: False, ‘best’: True, ‘gfg’: True}  
> Is Dictionary True ? : False

  

  

**Method #2 : Usingall() + values()**  
This is a shorthand approach to solve this problem. In this, all() is used to
check status of all values extracted using values().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test Boolean Value of Dictionary

# Using all() + values()

 

# initializing dictionary

test_dict = {'gfg' : True, 'is' : False, 'best' :
True}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Test Boolean Value of Dictionary

# Using all() + values()

res = all(test_dict.values())

 

# printing result 

print("Is Dictionary True ? : " + str(res))   
  
---  
  
__

__

**Output :**

> The original dictionary is : {‘is’: False, ‘best’: True, ‘gfg’: True}  
> Is Dictionary True ? : False

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

