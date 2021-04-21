Python – Minimum element indices



Sometimes, while working with Python lists, we can have a problem in which we
intend to find the position of minimum element of list. This task is easy and
discussed many times. But sometimes, we can have multiple minimum elements and
hence multiple minimum positions. Let’s discuss a shorthand to achieve this
task in this case.

 **Method : Usingmin() + enumerate() \+ list comprehension**  
In this method, the combination of above functions is used to perform this
particular task. This is performed in two steps. In 1st, we acquire the
minimum element and then access the list using list comprehension and
corresponding element using enumerate and extract every element position equal
to minimum element processed in step 1.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Minimum element indices

# Using list comprehension + min() + enumerate()

 

# initializing list

test_list = [2, 4, 6, 8, 2, 2]

 

# printing list

print("The original list : " + str(test_list))

 

# Minimum element indices

# Using list comprehension + min() + enumerate()

temp = min(test_list)

res = [i for i, j in enumerate(test_list) if j ==
temp]

 

# Printing result

print("The Positions of minimum element : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [2, 4, 6, 8, 2, 2]
    The Positions of minimum element : [0, 4, 5]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

