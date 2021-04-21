Python – AND operation between Tuples



Sometimes, while working with records, we might have a common problem of
performing AND operation contents of one tuple with corresponding index of
other tuple. This has application in almost all the domains in which we work
with tuple records especially Data Science. Let’s discuss certain ways in
which this task can be performed.

 **Method #1 : Usingmap() \+ lambda**  
Combination of above functionalities can solve the problem for us. In this, we
compute the AND using lambda functions and extend the logic to keys using
map().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Cross Tuple AND operation

# using map() + lambda

 

# initialize tuples 

test_tup1 = (10, 4, 5)

test_tup2 = (2, 5, 18)

 

# printing original tuples 

print("The original tuple 1 : " + str(test_tup1))

print("The original tuple 2 : " + str(test_tup2))

 

# Cross Tuple AND operation

# using map() + lambda

res = tuple(map(lambda i, j: i & j, test_tup1, test_tup2))

 

# printing result

print("Resultant tuple after AND operation : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple 1 : (10, 4, 5)
    The original tuple 2 : (2, 5, 18)
    Resultant tuple after AND operation : (2, 4, 0)
    

**Method #2 : Usingmap() + iand()**  
The combination of above functions can help us achieve this task. In this, we
first extend the logic to all using map() and then perform AND of each index
using iand().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Cross Tuple AND operation

# using map() + iand()

import operator

 

# initialize tuples 

test_tup1 = (10, 4, 5)

test_tup2 = (2, 5, 18)

 

# printing original tuples 

print("The original tuple 1 : " + str(test_tup1))

print("The original tuple 2 : " + str(test_tup2))

 

# Cross Tuple AND operation

# using map() + iand()

res = tuple(map(operator.iand, test_tup1, test_tup2))

 

# printing result

print("Resultant tuple after AND operation : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple 1 : (10, 4, 5)
    The original tuple 2 : (2, 5, 18)
    Resultant tuple after AND operation : (2, 4, 0)
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

