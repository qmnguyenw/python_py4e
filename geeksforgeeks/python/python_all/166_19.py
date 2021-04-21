Python | Check if element is present in tuple of tuples



Sometimes the data that we use is in the form of tuples and often we need to
look into the nested tuples as well. The common problem that this can solve is
looking for a missing data or N.A values in data preprocessing. Let’s discuss
certain ways in which this can be performed.  

 **Method #1 : Usingany()**  
any function is used to perform this task. It just tests one by one if the
element is present as the tuple element. If the element is present, true is
returned else false is returned.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# test for values in tuple of tuple

# using any()

 

# initializing tuple of tuple 

test_tuple = (("geeksforgeeks", "gfg"), ("CS_Portal",
"best"))

 

# printing tuple

print ("The original tuple is " + str(test_tuple))

 

# using any()

# to test for value in tuple of tuple

if (any('geeksforgeeks' in i for i in test_tuple)) :

 print("geeksforgeeks is present")

else :

 print("geeksforgeeks is not present")  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple is (('geeksforgeeks', 'gfg'), ('CS_Portal', 'best'))
    geeksforgeeks is present
    

**Method #2 : Usingitertools.chain()**  
The chain function tests for all the intermediate tuples for the desired
values and then returns true if the required value is present in any of the
tuples searched.  

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# test for values in tuple of tuple

# using itertools.chain()

import itertools

 

# initializing tuple of tuple 

test_tuple = (("geeksforgeeks", "gfg"), ("CS_Portal",
"best"))

 

# printing tuple

print ("The original tuple is " + str(test_tuple))

 

# using itertools.chain()

# to test for value in tuple of tuple

if ('geeksforgeeks' in itertools.chain(*test_tuple)) :

 print("geeksforgeeks is present")

else :

 print("geeksforgeeks is not present")  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple is (('geeksforgeeks', 'gfg'), ('CS_Portal', 'best'))
    geeksforgeeks is present
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

