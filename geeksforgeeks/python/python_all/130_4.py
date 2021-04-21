Python | Consecutive Maximum Occurrence in list



Sometimes, while working with Python lists or in competitive programming
setup, we can come across a subproblem in which we need to get an element
which has the maximum consecutive occurrence. The knowledge of solution of it
can be of great help and can be employed whenever required. Let’s discuss
certain ways in which this task can be performed.

 **Method #1 : Usinggroupby() + max() \+ lambda**  
This task can be solved using combination of above functions. In this, we
group each occurrence of numbers using groupby() and get the max of it using
max(). The lambda function provide utility logic to perform this task.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Consecutive Maximum Occurrence in list

# using groupby() + max() + lambda

from itertools import groupby

 

# initializing list

test_list = [1, 1, 1, 2, 2, 4, 2, 2,
5, 5, 5, 5]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Consecutive Maximum Occurrence in list

# using groupby() + max() + lambda

temp = groupby(test_list)

res = max(temp, key = lambda sub: len(list(sub[1])))

 

# printing result 

print("Maximum Consecutive Occurring number is : " +
str(res[0]))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 1, 1, 2, 2, 4, 2, 2, 5, 5, 5, 5]
    Maximum Consecutive Occurring number is : 5
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

