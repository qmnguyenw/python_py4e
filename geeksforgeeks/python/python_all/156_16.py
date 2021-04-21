Python | Append at front and remove from rear



Being familiar with the concept of queue, which follows FIFO rule, i.e first
in first out, that suggests a front removal and rear insertion. This has been
discussed many times. But sometimes we need to perform the exact opposite of
this and we need to perform the append at front and remove element from the
rear. Let’s discuss certain ways in which this can be done.

 **Method #1 : Using+ operator and list slicing**  
These operators can be used to perform this particular task. The append
operation can be done with the help of + operator and the removal of rear can
be done using the conventional list slicing.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# append from front and remove from rear

# using + operator and list slicing

 

# initializing list

test_list = [4, 5, 7, 3, 10]

 

# printing original list 

print("The original list : " + str(test_list))

 

# using + operator and list slicing

# append from front and remove from rear

res = [13] + test_list[:-1]

 

# printing result

print("The list after append and removal : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [4, 5, 7, 3, 10]
    The list after append and removal : [13, 4, 5, 7, 3]
    

**Method #2 : Usingcollections.deque()**  
The doubly ended queue can be used to perform this particular task in which is
supported by python using the collection library, the _appendleft_ and _pop_
methods of queue function can be used to perform this job.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# append from front and remove from rear

# using collections.deque

from collections import deque

 

# initializing list

test_list = [4, 5, 7, 3, 10]

 

# printing original list 

print("The original list : " + str(test_list))

 

# using collections.deque

# append from front and remove from rear

res = deque(test_list)

res.appendleft(13)

res.pop()

res = list(res)

 

# printing result

print("The list after append and removal : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [4, 5, 7, 3, 10]
    The list after append and removal : [13, 4, 5, 7, 3]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

