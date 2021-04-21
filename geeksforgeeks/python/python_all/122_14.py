Python | Removing duplicates from tuple



Many times, while working with Python tuples, we can have a problem of
removing duplicates. This is a very common problem and can occur in any form
of programming set up, be it regular programming or web development. Let’s
discuss certain ways in which this task can be performed.

 **Method #1 : Usingset() + tuple()**  
This is the most straight forward way to remove duplicates. In this, we
convert the tuple to a set, removing duplicates and then converting it back
again using tuple().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Removing duplicates from tuple 

# using tuple() + set()

 

# initialize tuple

test_tup = (1, 3, 5, 2, 3, 5, 1, 1,
3)

 

# printing original tuple 

print("The original tuple is : " + str(test_tup))

 

# Removing duplicates from tuple 

# using tuple() + set()

res = tuple(set(test_tup))

 

# printing result

print("The tuple after removing duplicates : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple is : (1, 3, 5, 2, 3, 5, 1, 1, 3)
    The tuple after removing duplicates : (1, 2, 3, 5)
    

**Method #2 : UsingOrderedDict() + fromkeys()**  
The combination of above functions can also be used to perform this particular
task. In this, we convert the tuples to dictionary removing duplicates and
then accessing it’s keys.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Removing duplicates from tuple 

# using OrderedDict() + fromkeys()

from collections import OrderedDict

 

# initialize tuple

test_tup = (1, 3, 5, 2, 3, 5, 1, 1,
3)

 

# printing original tuple 

print("The original tuple is : " + str(test_tup))

 

# Removing duplicates from tuple 

# using OrderedDict() + fromkeys()

res = tuple(OrderedDict.fromkeys(test_tup).keys())

 

# printing result

print("The tuple after removing duplicates : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple is : (1, 3, 5, 2, 3, 5, 1, 1, 3)
    The tuple after removing duplicates : (1, 2, 3, 5)
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

