Python | How to get Subtraction of tuples



Sometimes, while working with records, we might have a common problem of
subtracting contents of one tuple with corresponding index of other tuple.
This has application in almost all the domains in which we work with tuple
records. Let’s discuss certain ways in which this task can be performed.

 **Method #1 : Using map() \+ lambda**  
Combination of above functionalities can solve the problem for us. In this, we
compute the subtraction using lambda functions and extend the logic to keys
using map().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Subtraction of tuples

# using map() + lambda

 

# initialize tuples 

test_tup1 = (10, 4, 5)

test_tup2 = (2, 5, 18)

 

# printing original tuples 

print("The original tuple 1 : " + str(test_tup1))

print("The original tuple 2 : " + str(test_tup2))

 

# Subtraction of tuples

# using map() + lambda

res = tuple(map(lambda i, j: i - j, test_tup1, test_tup2))

 

# printing result

print("Resultant tuple after subtraction : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple 1 : (10, 4, 5)
    The original tuple 2 : (2, 5, 18)
    Resultant tuple after subtraction : (8, -1, -13)
    

**Method #2 : Using map() + sub()**  
The combination of above functions can help us achieve this task. In this, we
first extend the logic to all using map() and then perform subtraction of
each index using sub().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Addition of tuples

# using map() + sub()

import operator

 

# initialize tuples 

test_tup1 = (10, 4, 5)

test_tup2 = (2, 5, 18)

 

# printing original tuples 

print("The original tuple 1 : " + str(test_tup1))

print("The original tuple 2 : " + str(test_tup2))

 

# Addition of tuples

# using map() + sub()

res = tuple(map(operator.sub, test_tup1, test_tup2))

 

# printing result

print("Resultant tuple after subtraction : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple 1 : (10, 4, 5)
    The original tuple 2 : (2, 5, 18)
    Resultant tuple after subtraction : (8, -1, -13)
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

