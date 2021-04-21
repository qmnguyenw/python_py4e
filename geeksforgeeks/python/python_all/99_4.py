Python – Clearing a tuple



Sometimes, while working with Records data, we can have a problem in which we
may require to perform clearing of data records. Tuples, being immutable
cannot be modified and hence makes this job tough. Let’s discuss certain ways
in which this task can be performed.

 **Method #1 : Usinglist() + clear() + tuple()**  
The combination of above 3 finctions can be used to perform this task. In
this, we interconvert the tuple to list, clear it and again convert to tuple
using tuple().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Clearing a tuple

# using list() + tuple() + clear()

 

# initializing tuple

test_tup = (1, 5, 3, 6, 8)

 

# printing original tuple

print("The original tuple : " + str(test_tup))

 

# Clearing a tuple

# using list() + tuple() + clear()

temp = list(test_tup)

temp.clear()

test_tup = tuple(temp)

 

# print result

print("The tuple after clearing values : " + str(test_tup))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple : (1, 5, 3, 6, 8)
    The tuple after clearing values : ()
    

**Method #2 : Reinitialization using tuple()**  
Another straight forward way to perform this task is to reinitialize tuple
using tuple() which will return empty tuple.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Clearing a tuple

# using Reinitialization + tuple()

 

# initializing tuple

test_tup = (1, 5, 3, 6, 8)

 

# printing original tuple

print("The original tuple : " + str(test_tup))

 

# Clearing a tuple

# using Reinitialization + tuple()

test_tup = tuple()

 

# print result

print("The tuple after clearing values : " + str(test_tup))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple : (1, 5, 3, 6, 8)
    The tuple after clearing values : ()
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

