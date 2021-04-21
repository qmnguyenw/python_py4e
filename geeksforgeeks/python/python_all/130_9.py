Python | Group consecutive list elements with tolerance



Sometimes, we might need to group list according to the consecutive elements
in list. But a useful variation of this can also be a case in which we need to
consider a tolerance level, i.e allowing a skip value between number and not
being exactly consecutive but a “gap” is allowed between numbers. Let’s
discuss an approach in which this task can be performed.

 **Method : Using generator**  
The brute method to perform this task. Using loop and generator, one can
perform this task. The slicing is taken care by the yield operator and hence
this problem is solved by a small check of tolerance as well.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Group consecutive list elements with tolerance

# Using generator

 

# helper generator

def split_tol(test_list, tol):

 res = []

 last = test_list[0]

 for ele in test_list:

 if ele-last > tol:

 yield res

 res = []

 res.append(ele)

 last = ele

 yield res

 

# initializing list

test_list = [1, 2, 4, 5, 9, 11, 13, 24,
25, 26, 28]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Group consecutive list elements with tolerance

# Using generator

res = list(split_tol(test_list, 2))

 

# printing result 

print("The splitted list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 2, 4, 5, 9, 11, 13, 24, 25, 26, 28]
    The splitted list is : [[1, 2, 4, 5], [9, 11, 13], [24, 25, 26, 28]]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

