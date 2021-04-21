Python | Zip Uneven Tuple



In python, zipping is a utility where we pair one record with the other.
Usually this task is successful only in the cases when the sizes of both the
records to be zipped is of the same size. But sometimes we require that
different sized records also to be zipped. Let’s discuss certain ways in which
this problem can be solved if it occurs.

 **Method #1 : Usingenumerate() \+ loop**  
This is the way in which we use the brute force method to achieve this
particular task. In this process we loop both the tuple and when one becomes
larger than other we cycle the elements to begin them from the beginning.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Zip Uneven Tuple

# using enumerate() + loop

 

# initializing tuples

test_tup1 = (7, 8, 4, 5, 9, 10)

test_tup2 = (1, 5, 6)

 

# printing original tuples

print ("The original tuple 1 is : " + str(test_tup1))

print ("The original tuple 2 is : " + str(test_tup2))

 

# using enumerate() + loop

# Zip Uneven Tuple

res = []

for i, j in enumerate(test_tup1):

 res.append((j, test_tup2[i % len(test_tup2)]))

 

# printing result 

print ("The zipped tuple is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple 1 is : (7, 8, 4, 5, 9, 10)
    The original tuple 2 is : (1, 5, 6)
    The zipped tuple is : [(7, 1), (8, 5), (4, 6), (5, 1), (9, 5), (10, 6)]
    

**Method #2 : Usingitertools.cycle()**  
This is yet another way to perform this particular task, in this we cycle the
smaller tuple so that it can begin zipping from beginning in case the smaller
tuple gets exhausted using a zip function.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Zip Uneven Tuple

# using itertools.cycle()

from itertools import cycle

 

# initializing tuples

test_tup1 = (7, 8, 4, 5, 9, 10)

test_tup2 = (1, 5, 6)

 

# printing original tuples

print ("The original tuple 1 is : " + str(test_tup1))

print ("The original tuple 2 is : " + str(test_tup2))

 

# using itertools.cycle()

# Zip Uneven Tuple

res = list(zip(test_tup1, cycle(test_tup2)) if len(test_tup1)
> len(test_tup2) else zip(cycle(test_tup1), test_tup2))

 

# printing result 

print ("The zipped tuple is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple 1 is : (7, 8, 4, 5, 9, 10)
    The original tuple 2 is : (1, 5, 6)
    The zipped tuple is : [(7, 1), (8, 5), (4, 6), (5, 1), (9, 5), (10, 6)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

