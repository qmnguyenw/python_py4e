Python | Bitwise OR among List elements



Sometimes, while programming, we have a problem in which we might need to
perform certain bitwise operations among list elements. This is an essential
utility as we come across bitwise operations many times. Let’s discuss certain
ways in which this task can be performed.

 **Method #1 : Usingreduce() + lambda + "|" operator**  
The above functions can be combined to perform this task. We can employ
reduce() to accumulate the result of OR logic specified by the lambda
function. Works only with Python2.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate working of

# Bitwise OR among List elements

# Using reduce() + lambda + "|" operator

 

# initializing list

test_list = [7, 8, 9, 1, 10, 7]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Bitwise OR among List elements

# Using reduce() + lambda + "|" operator

res = reduce(lambda x, y: x | y, test_list)

 

# printing result 

print("The Bitwise OR of list elements are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [7, 8, 9, 1, 10, 7]
    The Bitwise OR of list elements are : 15
    

**Method #2 : Usingreduce() + operator.ior**  
This task can also be performed using this method. In this the task performed
by lambda function in above method is performed using ior function for
cumulative OR operation. Works with Python2 only.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate working of

# Bitwise OR among List elements

# Using reduce() + operator.ior

from operator import ior

 

# initializing list

test_list = [7, 8, 9, 1, 10, 7]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Bitwise OR among List elements

# Using reduce() + operator.ior

res = reduce(ior, test_list)

 

# printing result 

print("The Bitwise OR of list elements are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [7, 8, 9, 1, 10, 7]
    The Bitwise OR of list elements are : 15
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

