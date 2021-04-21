Python – Minimum identical consecutive Subarray



Sometimes, while working with Python lists or in competitive programming
setup, we can come across a subproblem in which we need to get an element that
has the minimum consecutive occurrence. The knowledge of solution to it can be
of great help and can be employed whenever required. Let’s discuss a certain
way in which this task can be performed.

 **Usinggroupby() + min() \+ lambda**

This task can be solved using a combination of above functions. In this, we
group each occurrence of numbers using groupby() and get the min of it using
min(). The lambda function provide utility logic to perform this task.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Minimum identical consecutive Subarray

# using groupby() + min() + lambda

from itertools import groupby

 

# initializing list

test_list = [1, 1, 1, 2, 2, 5, 5, 5,
5]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Minimum identical consecutive Subarray

# using groupby() + min() + lambda

temp = groupby(test_list)

res = min(temp, key = lambda sub: len(list(sub[1])))

 

# printing result 

print("Minimum Consecutive identical Occurring number is : " +
str(res[0]))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 1, 1, 2, 2, 5, 5, 5, 5]
    Minimum Consecutive identical Occurring number is : 2
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

