How to Compare Two Dictionaries in Python?



In this article, we will discuss how to compare two dictionaries in Python. As
we all know what is a dictionary, but sometimes we may need to compare two
dictionaries. Let’s see different methods to do the same.

 **Method 1:** Using == operator.

## Python

 __

 __  
 __

 __

 __  
 __  
 __

dict1= {'Name': 'asif', 'Age': 5}

dict2 = {'Name': 'lalita', 'Age': 78}

 

if dict1 == dict2:

 print "dict1 is equal to dict2"

else:

 print "dict1 is not equal to dict2"  
  
---  
  
 __

 __

 **Output:**

    
    
    dict1 is not equal to dict2

 **Method 2:** Using DeepDiff module

This module is used to find the deep differences in dictionaries, iterables,
strings, and other objects. To install this module type the below command in
the terminal.

  

  

    
    
    pip install deepdiff

## Python

 __

 __  
 __

 __

 __  
 __  
 __

from deepdiff import DeepDiff

 

a = {'Name': 'asif', 'Age': 5}

b = {'Name': 'lalita', 'Age': 78}

 

diff = DeepDiff(a, b)

 

print(diff)  
  
---  
  
 __

 __

 **Output:**

> {‘values_changed’: {“root[‘Name’]”: {‘new_value’: ‘lalita’, ‘old_value’:
> ‘asif’}, “root[‘Age’]”: {‘new_value’: 78, ‘old_value’: 5}}}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

