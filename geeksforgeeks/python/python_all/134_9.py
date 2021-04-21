Python | Get Unique values from list of dictionary



Sometimes, while working with Python dictionaries, we can have a problem in
which we need to find the unique values over all the dictionaries in a list.
This kind of utility can occur in case while working with similar data and we
wish to extract the unique ones. Let’s discuss certain ways in which this task
can be performed.

 **Method #1 : Usingset() + values() \+ dictionary comprehension**  
The combination of these methods can together help us achieve the task of
getting the unique values. The values function helps us get the values of
dictionary, set helps us to get the unique of them, and dictionary
comprehension to iterate through the list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Get Unique values from list of dictionary

# Using set() + values() + dictionary comprehension

 

# Initialize list 

test_list = [{'gfg' : 1, 'is' : 2}, {'best' : 1,
'for' : 3}, {'CS' : 2}]

 

# printing original list

print("The original list : " + str(test_list))

 

# Using set() + values() + dictionary comprehension

# Get Unique values from list of dictionary

res = list(set(val for dic in test_list for val in
dic.values()))

 

# printing result 

print("The unique values in list are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list : [{‘gfg’: 1, ‘is’: 2}, {‘best’: 1, ‘for’: 3}, {‘CS’: 2}]  
> The unique values in list are : [1, 2, 3]

  

  

**Method #2 : Usingset() + values() \+ from_iterable()**  
The combination of above functions can be used to perform this particular
task. It is just as the above method, but the iteration part is done by the
from_iterable function.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Get Unique values from list of dictionary

# Using set() + values() + from_iterable()

from itertools import chain

 

# Initialize list 

test_list = [{'gfg' : 1, 'is' : 2}, {'best' : 1,
'for' : 3}, {'CS' : 2}]

 

# printing original list

print("The original list : " + str(test_list))

 

# Using set() + values() + from_iterable()

# Get Unique values from list of dictionary

res = list(set(chain.from_iterable(sub.values() for sub in
test_list)))

 

# printing result 

print("The unique values in list are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list : [{‘gfg’: 1, ‘is’: 2}, {‘best’: 1, ‘for’: 3}, {‘CS’: 2}]  
> The unique values in list are : [1, 2, 3]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

