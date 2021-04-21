Tuple Division in Python



Sometimes, while working with records, we can have a problem in which we may
need to perform mathematical division operation across tuples. This problem
can occur in day-day programming. Let’s discuss certain ways in which this
task can be performed.

 **Method #1 : Usingzip() \+ generator expression**  
The combination of above functions can be used to perform this task. In this,
we perform the task of division using generator expression and mapping index
of each tuple is done by zip().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Tuple division

# using zip() + generator expression 

 

# initialize tuples 

test_tup1 = (10, 4, 6, 9) 

test_tup2 = (5, 2, 3, 3) 

 

# printing original tuples 

print("The original tuple 1 : " + str(test_tup1)) 

print("The original tuple 2 : " + str(test_tup2)) 

 

# Tuple division 

# using zip() + generator expression 

res = tuple(ele1 // ele2 for ele1, ele2 in
zip(test_tup1, test_tup2)) 

 

# printing result 

print("The divided tuple : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original tuple 1 : (10, 4, 6, 9)
    The original tuple 2 : (5, 2, 3, 3)
    The divided tuple : (2, 2, 2, 3)
    

**Method #2 : Usingmap() \+ floordiv**  
The combination of above functionalities can also perform this task. In this,
we perform the task of extending logic of division using floordiv and mapping
is done by map().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Tuple division 

# using map() + floordiv 

from operator import floordiv

 

# initialize tuples 

test_tup1 = (10, 4, 6, 9) 

test_tup2 = (5, 2, 3, 3) 

 

# printing original tuples 

print("The original tuple 1 : " + str(test_tup1)) 

print("The original tuple 2 : " + str(test_tup2)) 

 

# Tuple division

# using map() + floordiv 

res = tuple(map(floordiv, test_tup1, test_tup2)) 

 

# printing result 

print("The divided tuple : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple 1 : (10, 4, 6, 9)
    The original tuple 2 : (5, 2, 3, 3)
    The divided tuple : (2, 2, 2, 3)
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

