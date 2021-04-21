Python | Rear Addition of Record



Sometimes, while working with Python list, we can have a problem in which we
need to add a new tuple to existing list. Append at rear is usually easier
than addition at front. Let’s discuss certain ways in which this task can be
performed.

 **Method #1 : Usinginsert()**  
This is one of the way in which the element can be added to rear in one-liner.
It is used to add any element in rear of list. The behaviour is the same for
tuple as well.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Rear Addition of Record

# using insert()

 

# Initializing list 

test_list = [('is', 2), ('best', 3)]

 

# printing original list 

print("The original list is : " + str(test_list))

 

# Initializing tuple to add 

add_tuple = ('gfg', 1)

 

# Rear Addition of Record

# using insert()

test_list.insert(len(test_list), add_tuple)

 

# printing result

print("The tuple after adding is : " + str(test_list))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [('is', 2), ('best', 3)]
    The tuple after adding is : [('is', 2), ('best', 3), ('gfg', 1)]
    

**Method #2 : Usingdeque() + append()**  
The combination of above functions can be used to perform this particular
task. In this, we just need to convert the list into a deque so that we can
perform the append at right using append().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Rear Addition of Record

# using deque() + append()

from collections import deque

 

# Initializing list 

test_list = [('is', 2), ('best', 3)]

 

# printing original list 

print("The original list is : " + str(test_list))

 

# Initializing tuple to add 

add_tuple = ('gfg', 1)

 

# Rear Addition of Record

# using deque() + append()

res = deque(test_list)

res.append(add_tuple)

 

# printing result

print("The tuple after adding is : " + str(list(res)))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [('is', 2), ('best', 3)]
    The tuple after adding is : [('is', 2), ('best', 3), ('gfg', 1)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

