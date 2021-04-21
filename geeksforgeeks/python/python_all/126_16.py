Python | Positions of maximum element in list



Sometimes, while working with Python lists, we can have a problem in which we
intend to find the position of maximum element of list. This task is easy and
discussed many times. But sometimes, we can have multiple maximum elements and
hence multiple maximum positions. Let’s discuss a shorthand to achieve this
task in this case.

 **Method : Usingmax() + enumerate() \+ list comprehension**  
In this method, the combination of above functions is used to perform this
particular task. This is performed in two steps. In 1st, we acquire the
maximum element and then access the list using list comprehension and
corresponding element using enumerate and extract every element position equal
to maximum element processed in step 1.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Positions of maximum element in list

# Using list comprehension + max() + enumerate()

 

# initializing list

test_list = [8, 4, 6, 8, 2, 8]

 

# printing list

print("The original list : " + str(test_list))

 

# Positions of maximum element in list

# Using list comprehension + max() + enumerate()

temp = max(test_list)

res = [i for i, j in enumerate(test_list) if j ==
temp]

 

# Printing result

print("The Positions of maximum element : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
     
    The original list : [8, 4, 6, 8, 2, 8]
    The Positions of maximum element : [0, 3, 5]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

