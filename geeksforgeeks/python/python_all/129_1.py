Python | Test for nested list



Sometimes, while working with Python list, we might have a problem in which we
need to find that a list is a Matrix or a list contains list as it’s element.
This problem can come in Data Science domain as it involves use of Matrices
more than often. Let’s discuss certain way in which this task can be
performed.

 **Method : Usingany() + isinstance()**  
The combination of above functions can be used to perform this task. The
any() is used to check for each of the occurrence and isinstance() is used
to check for list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test for nested list

# using any() + isinstance()

 

# initialize list

test_list = [[5, 6], 6, [7], 8, 10]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Test for nested list

# using any() + isinstance()

res = any(isinstance(sub, list) for sub in test_list)

 

# printing result

print("Does list contain nested list ? : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [[5, 6], 6, [7], 8, 10]
    Does list contain nested list ? : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

