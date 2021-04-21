Python | Every Kth element in list



Sometimes, while working with Python lists, we can have a problem in which we
require to extract every Kth element of list and slice out a new list from
that. This type of problems are quite common as a variation of list slicing.
Let’s discuss a way in which this can be done.

 **Method : Using list slicing**  
This task can be performed using list slicing functionality. The trick here is
to use the skip functionality of list to get every Kth element of list. K, as
defined can be used as skip element.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Kth element list

# Using list slicing 

 

# initializing list

test_list = [6, 4, 8, 9, 10, 5, 8, 9,
10, 2, 34, 5]

 

# printing list

print("The original list : " + str(test_list))

 

# initializing K 

K = 3

 

# Kth element list

# Using list slicing 

res = test_list[::K]

 

# Printing result

print("Kth element list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
     
    The original list : [6, 4, 8, 9, 10, 5, 8, 9, 10, 2, 34, 5]
    Kth element list is : [6, 9, 8, 2]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

