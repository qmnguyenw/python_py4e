Python | Find the closest Key in dictionary



The search of keys in dictionary in python has been discussed many times. But
sometimes, we may have a problem in which we require to fetch the key which is
the nearest one of the given keys. Let’s discuss certain ways in which this
task can be performed.

 **Method #1 : Using list comprehension +keys() \+ lambda**  
The combination of above functions can be used to perform the particular task
of finding the closest key in the dictionary. The keys function can be used to
access the keys from the dictionary, lambda function can be used to formulate
the logic and list comprehension to apply that all to whole list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Closest key in dictionary

# Using list comprehension + keys() + lambda

 

# initializing dictionary

test_dict = {13 : 'Hi', 15 : 'Hello', 16 :
'Gfg'}

 

# initializing nearest key

search_key = 15.6

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Using list comprehension + keys() + lambda

# Closest key in dictionary

res = test_dict.get(search_key) or test_dict[

 min(test_dict.keys(), key = lambda key:
abs(key-search_key))]

 

# printing result 

print("The value to the closest key : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary is : {16: 'Gfg', 13: 'Hi', 15: 'Hello'}
    The value to the closest key : Gfg
    

**Method #2 : Usingbisect_left() + OrderedDict()**  
This method generally uses the binary search method of finding the nearest
number. While being fast, it changes the ordering and also returns 2 potential
candidates for nearest values, current and the next key’s value in sequence.
And just returns position of key.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Closest key in dictionary

# Using bisect_left() + OrderedDict()

import collections

import bisect

 

# initializing dictionary

test_dict = collections.OrderedDict()

test_dict = {13 : 'Hi', 15 : 'Hello', 16 :
'Gfg'}

 

# initializing nearest key

search_key = 15.6

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Using bisect_left() + OrderedDict()

# Closest key in dictionary

res = bisect.bisect_left(list(test_dict.keys()), 15.6)

 

# printing result 

print("The position of closest key : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original dictionary is : {16: 'Gfg', 13: 'Hi', 15: 'Hello'}
    The position of closest key : 3
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

