Python | Triplet iteration in List



List iteration is common in programming, but sometimes one requires to print
the elements in consecutive triplets. This particular problem is quite common
and having a solution to it always turns out to be handy. Lets discuss certain
way in which this problem can be solved.

 **Method #1 : Using list comprehension**  
List comprehension can be used to print the triplets by accessing current,
next and next to next element in the list and then printing the same. Care has
to be taken while pairing the last elements with the first ones to form a
cyclic triplet pairs.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Triplet iteration in List

# using list comprehension

from itertools import compress

 

# initializing list 

test_list = [0, 1, 2, 3, 4, 5]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# using list comprehension

# Triplet iteration in List

res = [((i), (i + 1) % len(test_list), (i + 2) %
len(test_list)) 

 for i in range(len(test_list))]

 

# printing result

print ("The triplet list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [0, 1, 2, 3, 4, 5]
    The triplet list is : [(0, 1, 2), (1, 2, 3), (2, 3, 4), (3, 4, 5), (4, 5, 0), (5, 0, 1)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

