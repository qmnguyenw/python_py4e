Python | Check if all elements in list follow a condition



Sometimes, while working with Python list, we can have a problem in which we
need to check if all the elements in list abide to a particular condition.
This can have application in filtering in web development domain. Let’s
discuss certain ways in which this task can be performed.

 **Method #1 : Usingall()**  
We can use all(), to perform this particular task. In this, we feed the
condition and the validation with all the elements is checked by all()
internally.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check if all elements in list follow a condition

# Using all()

 

# initializing list

test_list = [4, 5, 8, 9, 10]

 

# printing list

print("The original list : " + str(test_list))

 

# Check if all elements in list follow a condition

# Using all()

res = all(ele > 3 for ele in test_list)

 

# Printing result

print("Are all elements greater than 3 ? : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
     
    The original list : [4, 5, 8, 9, 10]
    Are all elements greater than 3 ? : True
    

**Method #2 : Usingitertools.takewhile()**  
This function can also be used to code solution of this problem. In this, we
just need to process the loop till a condition is met and increment the
counter. If it matches list length, then all elements meet that condition.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check if all elements in list follow a condition

# Using itertools.takewhile()

import itertools

 

# initializing list

test_list = [4, 5, 8, 9, 10]

 

# printing list

print("The original list : " + str(test_list))

 

# Check if all elements in list follow a condition

# Using itertools.takewhile()

count = 0

for ele in itertools.takewhile(lambda x: x > 3, test_list):

 count = count + 1

res = count == len(test_list)

 

# Printing result

print("Are all elements greater than 3 ? : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
     
    The original list : [4, 5, 8, 9, 10]
    Are all elements greater than 3 ? : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

