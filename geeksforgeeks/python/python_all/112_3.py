Python – Modulo of tuple elements



Sometimes, while working with records, we can have a problem in which we may
need to perform modulo of tuples. This problem can occur in day-day
programming. Let’s discuss certain ways in which this task can be performed.

 **Method #1 : Usingzip() \+ generator expression**  
The combination of above functions can be used to perform this task. In this,
we perform the task of modulo using generator expression and mapping index of
each tuple is done by zip().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Tuple modulo

# using zip() + generator expression

 

# initialize tuples

test_tup1 = (10, 4, 5, 6)

test_tup2 = (5, 6, 7, 5)

 

# printing original tuples

print("The original tuple 1 : " + str(test_tup1))

print("The original tuple 2 : " + str(test_tup2))

 

# Tuple modulo

# using zip() + generator expression

res = tuple(ele1 % ele2 for ele1, ele2 in zip(test_tup1,
test_tup2))

 

# printing result

print("The modulus tuple : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple 1 : (10, 4, 5, 6)
    The original tuple 2 : (5, 6, 7, 5)
    The modulus tuple : (0, 4, 5, 1)
    

**Method #2 : Using map() \+ mod**  
The combination of above functionalities can also perform this task. In this,
we perform the task of extending logic of modulus using mod and mapping is
done by map().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Tuple modulo

# using map() + mod

from operator import mod

 

# initialize tuples

test_tup1 = (10, 4, 5, 6)

test_tup2 = (5, 6, 7, 5)

 

# printing original tuples

print("The original tuple 1 : " + str(test_tup1))

print("The original tuple 2 : " + str(test_tup2))

 

# Tuple modulo

# using map() + mod

res = tuple(map(mod, test_tup1, test_tup2))

 

# printing result

print("The modulus tuple : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple 1 : (10, 4, 5, 6)
    The original tuple 2 : (5, 6, 7, 5)
    The modulus tuple : (0, 4, 5, 1)
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

