Python | Tuple multiplication



Sometimes, while working with records, we can have a problem in which we may
need to perform multiplication of tuples. This problem can occur in day-day
programming. Let’s discuss certain ways in which this task can be performed.

 **Method #1 : Using zip() + generator expression**  
The combination of above functions can be used to perform this task. In this,
we perform the task of multiplication using generator expression and mapping
index of each tuple is done by zip().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Tuple multiplication

# using zip() + generator expression

 

# initialize tuples

test_tup1 = (10, 4, 5, 6)

test_tup2 = (5, 6, 7, 5)

 

# printing original tuples

print("The original tuple 1 : " + str(test_tup1))

print("The original tuple 2 : " + str(test_tup2))

 

# Tuple multiplication

# using zip() + generator expression

res = tuple(ele1 * ele2 for ele1, ele2 in zip(test_tup1,
test_tup2))

 

# printing result

print("The multiplied tuple : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple 1 : (10, 4, 5, 6)
    The original tuple 2 : (5, 6, 7, 5)
    The multiplied tuple : (50, 24, 35, 30)
    

**Method #2 : Using map() + mul**  
The combination of above functionalities can also perform this task. In this,
we perform the task of extending logic of multiplication using mul and mapping
is done by map().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Tuple multiplication

# using map() + mul

from operator import mul

 

# initialize tuples

test_tup1 = (10, 4, 5, 6)

test_tup2 = (5, 6, 7, 5)

 

# printing original tuples

print("The original tuple 1 : " + str(test_tup1))

print("The original tuple 2 : " + str(test_tup2))

 

# Tuple multiplication

# using map() + mul

res = tuple(map(mul, test_tup1, test_tup2))

 

# printing result

print("The multiplied tuple : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple 1 : (10, 4, 5, 6)
    The original tuple 2 : (5, 6, 7, 5)
    The multiplied tuple : (50, 24, 35, 30)
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

