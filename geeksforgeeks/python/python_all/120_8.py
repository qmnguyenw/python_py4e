Python | Count the elements till first tuple



Sometimes, while working with records, we can have a problem in which an
element of a record is another tuple records and we might have to count the
element count that occur before the record. This is a problem which does not
occur commonly, but having a solution to it is useful. Let’s discuss certain
ways in which this task can be performed.

 **Method #1 : Using loop +isintance() + enumerate()**  
This problem can be solved using the above functionalities. In this, we just
loop through the elements using enumerate() to get the index count of it and
check the type using isinstance().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Elements till first tuple

# using isinstance() + enumerate() + loop

 

# initialize tuple

test_tup = (1, 5, 7, (4, 6), 10)

 

# printing original tuple

print("The original tuple : " + str(test_tup))

 

# Elements till first tuple

# using isinstance() + enumerate() + loop

for count, ele in enumerate(test_tup):

 if isinstance(ele, tuple):

 break

 

# printing result

print("Elements till the first tuple : " + str(count))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple : (1, 5, 7, (4, 6), 10)
    Elements till the first tuple : 3
    

**Method #2 : Usingtakewhile() + sum() + isinstance() \+ lambda**  
The combination of above functions can also be used to solve this problem. In
this, we use takewhile(), to iterate till a tuple and sum() to check the
counter.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Elements till first tuple

# using takewhile() + sum() + isinstance() + lambda

from itertools import takewhile

 

# initialize tuple

test_tup = (1, 5, 7, (4, 6), 10)

 

# printing original tuple

print("The original tuple : " + str(test_tup))

 

# Elements till first tuple

# using takewhile() + sum() + isinstance() + lambda

res = sum(1 for sub in takewhile(lambda ele: not
isinstance(ele, tuple), test_tup))

 

# printing result

print("Elements till the first tuple : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple : (1, 5, 7, (4, 6), 10)
    Elements till the first tuple : 3
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

