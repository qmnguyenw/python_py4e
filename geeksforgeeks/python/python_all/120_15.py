Python | Extract unique tuples from list, Order Irrespective



Sometimes, while working with data, we can have a problem in which we need to
check for similar records and eradicate them. When elements are ordered, this
case has been discussed before. But sometimes, we might have to ignore the
order and has to be removed in case similar elements occur. Let’s discuss
certain ways in which this task can be performed.

 **Method #1 : Using list comprehension +set()**  
The combination of above functionalities can be clubbed to perform this
particular task. In this, we check for each pair and add to a set for
reference to check if it has existed before and add if it’s a new one.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract unique tuples from list(Order Irrespective)

# using list comprehension + set()

 

# initialize tuples list 

test_list = [(1, 3), (4, 5), (3, 1), (1,
10), (5, 4)]

 

# printing original list 

print("The original list : " + str(test_list))

 

# Extract unique tuples from list(Order Irrespective)

# using list comprehension + set()

res = set() 

temp = [res.add((a, b)) for (a, b) in test_list 

 if (a, b) and (b, a) not in res]

 

# printing result

print("The list after duplicated removal : " + str(list(res)))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [(1, 3), (4, 5), (3, 1), (1, 10), (5, 4)]
    The list after duplicated removal : [(4, 5), (1, 3), (1, 10)]
    

**Method #2 : Usingfrozenset()**  
Another method to perform this particular task is to use frozenset(). This
function eliminates internally the similar elements irrespective of order.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract unique tuples from list(Order Irrespective)

# using frozenset()

 

# initialize tuples list 

test_list = [(1, 3), (4, 5), (3, 1), (1,
10), (5, 4)]

 

# printing original list 

print("The original list : " + str(test_list))

 

# Extract unique tuples from list(Order Irrespective)

# using frozenset()

res = set(tuple(frozenset(sub)) for sub in
set(test_list))

 

# printing result

print("The list after duplicated removal : " + str(list(res)))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [(1, 3), (4, 5), (3, 1), (1, 10), (5, 4)]
    The list after duplicated removal : [(4, 5), (1, 3), (1, 10)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

