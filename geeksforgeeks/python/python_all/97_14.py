Python – Tuple elements inversions



Sometimes, while programming, we have a problem in which we might need to
perform certain bitwise operations among tuple elements. This is an essential
utility as we come across bitwise operations many times. Let’s discuss certain
ways in which this task can be performed.

 **Method #1 : Usingmap() + list() + tuple() + lambda + "~" operator**  
The above functions can be combined to perform this task. We can employ map()
to accumulate the result of Inversion logic specified by the lambda function.
The list() and tuple() functions are used to perform interconversions.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Tuple elements inversions

# Using map() + list() + tuple() + lambda + "~" operator 

 

# initializing tup 

test_tup = (7, 8, 9, 1, 10, 7) 

 

# printing original tuple

print("The original tuple is : " + str(test_tup)) 

 

# Tuple elements inversions

# Using map() + list() + tuple() + lambda + "~" operator 

res = tuple(list(map(lambda x: ~x, list(test_tup)))) 

 

# printing result 

print("The Bitwise Inversions of tuple elements are : " + str(res))
  
  
---  
  
__

__

**Output :**

    
    
    The original tuple is : (7, 8, 9, 1, 10, 7)
    The Bitwise Inversions of tuple elements are : (-8, -9, -10, -2, -11, -8)
    

**Method #2 : Usingmap() + tuple() + list() + operator.invert**  
This task can also be performed using this method. In this the task performed
by lambda function in above method is performed using ior function for
cumulative Inversion operation. The list() and tuple() functions are used to
perform interconversions.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate working of

# Tuple elements inversions

# Using map() + list() + tuple() + operator.invert 

from operator import invert 

 

# initializing tup 

test_tup = (7, 8, 9, 1, 10, 7) 

 

# printing original tuple

print("The original tuple is : " + str(test_tup)) 

 

# Tuple elements inversions

# Using map() + list() + tuple() + operator.invert 

res = tuple(list(map(invert, list(test_tup)))) 

 

# printing result 

print("The Bitwise Inversions of tuple elements are : " + str(res))
  
  
---  
  
__

__

**Output :**

    
    
    The original tuple is : (7, 8, 9, 1, 10, 7)
    The Bitwise Inversions of tuple elements are : (-8, -9, -10, -2, -11, -8)
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

