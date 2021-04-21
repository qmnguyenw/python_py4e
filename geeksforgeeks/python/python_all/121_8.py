Python | Flatten Tuples List to String



Sometimes, while working with data, we can have a problem in which we need to
perform interconversion of data. In this, we can have a problem of converting
tuples list to a single String. Let’s discuss certain ways in which this task
can be performed.

 **Method #1 : Using list comprehension +join()**  
The combination of above functionalities can be used to perform this task. In
this, we join all the individual string elements using join() and extraction
of each element is done using list comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Flatten Tuples List to String

# using join() + list comprehension

 

# initialize list of tuple

test_list = [('1', '4', '6'), ('5', '8'), ('2',
'9'), ('1', '10')]

 

# printing original tuples list

print("The original list : " + str(test_list))

 

# Flatten Tuples List to String

# using join() + list comprehension

res = ' '.join([idx for tup in test_list for idx in
tup])

 

# printing result

print("Tuple list converted to String is : " + res)  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [('1', '4', '6'), ('5', '8'), ('2', '9'), ('1', '10')]
    Tuple list converted to String is : 1 4 6 5 8 2 9 1 10
    

**Method #2 : Usingchain() + join()**  
This is yet another method to perform this particular task. In this, we
perform the task of extracting each of element of tuple list using chain()
rather than list comprehension.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Flatten Tuples List to String

# using chain() + join()

from itertools import chain

 

# initialize list of tuple

test_list = [('1', '4', '6'), ('5', '8'), ('2',
'9'), ('1', '10')]

 

# printing original tuples list

print("The original list : " + str(test_list))

 

# Flatten Tuples List to String

# using chain() + join()

res = ' '.join(chain(*test_list))

 

# printing result

print("Tuple list converted to String is : " + res)  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [('1', '4', '6'), ('5', '8'), ('2', '9'), ('1', '10')]
    Tuple list converted to String is : 1 4 6 5 8 2 9 1 10
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

