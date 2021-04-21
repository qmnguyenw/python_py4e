Python | Split list in uneven groups



Sometimes, while working with python, we can have a problem of splitting a
list. This problem is quite common and has many variations. Having solutions
to popular variations proves to be good in long run. Let’s discuss certain way
to split list in uneven groups as defined by other list.

 **Method : Usingitertools.islice() \+ list comprehension**  
The combination of above functionalities can be used to perform this task. In
this, islice() is used to perform the core task of slicing the list and list
comprehension is used to perform the task of binding together logic and
iterations. The container is converted to iterator for faster iteration.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Split list in uneven groups

# using itertools.islice() + list comprehension

from itertools import islice

 

# initialize list

test_list = [1, 4, 5, 7, 6, 5, 4, 2,
10]

 

# initialize split list

split_list = [3, 4, 2]

 

# printing original list

print("The original list is : " + str(test_list))

 

# printing split list 

print("The split list is : " + str(split_list))

 

# Split list in uneven groups

# using itertools.islice() + list comprehension

temp = iter(test_list)

res = [list(islice(temp, 0, ele)) for ele in split_list]

 

# printing result

print("The resultant split list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 4, 5, 7, 6, 5, 4, 2, 10]
    The split list is : [3, 4, 2]
    The resultant split list is : [[1, 4, 5], [7, 6, 5, 4], [2, 10]]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

