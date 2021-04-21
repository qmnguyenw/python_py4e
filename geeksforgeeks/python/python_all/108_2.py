Python | Pair Product combinations



Sometimes, while working with data, we can have a problem in which we need to
perform tuple multiplication among all the tuples in list. This can have
application in many domains. Let’s discuss certain ways in which this task can
be performed.

 **Method #1 : Usingcombinations() \+ list comprehension**  
This problem can be solved using combinations of above functions. In this, we
use combinations() to generate all possible combination among tuples and list
comprehension is used to feed product logic.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Pair Product combinations

# Using list comprehension + combinations

from itertools import combinations

 

# initialize list 

test_list = [(2, 4), (6, 7), (5, 1), (6,
10)]

 

# printing original list 

print("The original list : " + str(test_list))

 

# Pair Product combinations

# Using list comprehension + combinations

res = [(b1 * a1, b2 * a2) for (a1, a2), (b1, b2) in
combinations(test_list, 2)] 

 

# printing result

print("The Product pair combinations are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [(2, 4), (6, 7), (5, 1), (6, 10)]
    The Product pair combinations are : [(12, 28), (10, 4), (12, 40), (30, 7), (36, 70), (30, 10)]
    

**Method #2 : Using list comprehension +zip() \+ operator.mul +
combinations()**  
The combinations of above methods can also solve this problem. In this, we
perform the task of product using mul() and the like indexed elements are
linked using zip().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Pair Product combinations

# Using list comprehension + zip() + operator.mul + combinations()

from itertools import combinations

import operator

 

# initialize list 

test_list = [(2, 4), (6, 7), (5, 1), (6,
10)]

 

# printing original list 

print("The original list : " + str(test_list))

 

# Pair Product combinations

# Using list comprehension + zip() + operator.mul + combinations()

res = [(operator.mul(*a), operator.mul(*b))\

 for a, b in (zip(y, x) for x, y in
combinations(test_list, 2))]

 

# printing result

print("The Product pair combinations are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [(2, 4), (6, 7), (5, 1), (6, 10)]
    The Product pair combinations are : [(12, 28), (10, 4), (12, 40), (30, 7), (36, 70), (30, 10)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

