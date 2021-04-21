Python | Swap tuple elements in list of tuples



While doing competitive programming, one can come across a question in which
one requires to work with 2D plane and work with coordinates. One such
subproblem can be swapping x, y coordinate elements. Let’s discuss certain
ways in which this problem can be solved using tuple element swapping.

 **Method #1 : Using list comprehension**  
This is just a brute method to perform the longer method of loop for swapping
the elements. In this a new list of tuple is created rather than an inplace
swap.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Swap tuple elements in list of tuples

# Using list comprehension

 

# initializing list

test_list = [(3, 4), (6, 5), (7, 8)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Swap tuple elements in list of tuples

# Using list comprehension

res = [(sub[1], sub[0]) for sub in test_list]

 

# printing result

print("The swapped tuple list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [(3, 4), (6, 5), (7, 8)]
    The swapped tuple list is : [(4, 3), (5, 6), (8, 7)]
    

**Method #2 : Usingmap() \+ lambda**  
Yet another way to perform this task is using map and lambda. This is a bit
slower in execution but a more compact way to perform this task.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Swap tuple elements in list of tuples

# Using map() + lambda

 

# initializing list

test_list = [(3, 4), (6, 5), (7, 8)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Swap tuple elements in list of tuples

# Using map() + lambda

res = list(map(lambda sub: (sub[1], sub[0]),
test_list))

 

# printing result

print("The swapped tuple list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [(3, 4), (6, 5), (7, 8)]
    The swapped tuple list is : [(4, 3), (5, 6), (8, 7)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

