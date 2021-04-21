Python | Add list at beginning of list



Sometimes, while working with Python list, we have a problem in which we need
to add a complete list to other. The rear end addition of list has been
discussed before. But sometimes, we need to perform an append at beginning of
list. Let’s discuss certain ways in which this task can be performed.

 **Method #1 : Using "+" operator**  
The “+” operator can be used to perform this particular task. In this, we just
perform the addition of one list before other and construct a new list or
perform the addition to same list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Adding list at beginning of list

# using "+" operator

 

# initialize list

test_list = [1, 4, 5, 7, 6]

 

# initialize add list

add_list = [3, 4, 2, 10]

 

# printing original list

print("The original list is : " + str(test_list))

 

# printing add list 

print("The add list is : " + str(add_list))

 

# Adding list at beginning of list

# using "+" operator

test_list = add_list + test_list

 

# printing result

print("The original updated list is : " + str(test_list))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 4, 5, 7, 6]
    The add list is : [3, 4, 2, 10]
    The original updated list is : [3, 4, 2, 10, 1, 4, 5, 7, 6]
    

**Method #2 : Usingdeque.extendleft() + reversed()**  
This task can also be performed using combination of above methods. In this,
we just convert the list into a dequeue, to allow a front append, and then one
by one addition is done by extendleft(), the add list is reversed so that
addition take place in correct order using reversed().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Adding list at beginning of list

# using deque.extendleft() + reversed()

from collections import deque

 

# initialize list

test_list = [1, 4, 5, 7, 6]

 

# initialize add list

add_list = [3, 4, 2, 10]

 

# printing original list

print("The original list is : " + str(test_list))

 

# printing add list 

print("The add list is : " + str(add_list))

 

# Adding list at beginning of list

# using deque.extendleft() + reversed()

res = deque(test_list)

res.extendleft(reversed(add_list))

 

# printing result

print("The original updated list is : " + str(list(res)))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 4, 5, 7, 6]
    The add list is : [3, 4, 2, 10]
    The original updated list is : [3, 4, 2, 10, 1, 4, 5, 7, 6]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

