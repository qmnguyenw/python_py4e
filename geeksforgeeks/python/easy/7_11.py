Python – Convert key-values list to flat dictionary



Sometimes, while working with Python dictionaries, we can have a problem in
which we need to flatten dictionary of key-value pair pairing the equal index
elements together. This can have utilities in web development and Data Science
domain. Lets discuss certain way in which this task can be performed.

 **Method :zip() + dict()**  
The combination of above functions can be used to achieve the required task.
In this, we perform the pairing using zip() and dict() is used to convert
tuple data returned by zip() to dictionary format.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert key-values list to flat dictionary

# Using dict() + zip()

from itertools import product

 

# initializing dictionary

test_dict = {'month' : [1, 2, 3],

 'name' : ['Jan', 'Feb', 'March']}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Convert key-values list to flat dictionary

# Using dict() + zip()

res = dict(zip(test_dict['month'], test_dict['name']))

 

# printing result 

print("Flattened dictionary : " + str(res))   
  
---  
  
__

__

**Output :**

> The original dictionary is : {‘name’: [‘Jan’, ‘Feb’, ‘March’], ‘month’: [1,
> 2, 3]}  
> Flattened dictionary : {1: ‘Jan’, 2: ‘Feb’, 3: ‘March’}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

