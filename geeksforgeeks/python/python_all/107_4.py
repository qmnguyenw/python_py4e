Python – List XOR



Sometimes, while programming, we have a problem in which we might need to
perform certain bitwise operations among list elements. This is an essential
utility as we come across bitwise operations many times. Let’s discuss certain
ways in which XOR can be performed.

 **Method #1 : Usingreduce() + lambda + “^” operator**  
The above functions can be combined to perform this task. We can employ
reduce() to accumulate the result of XOR logic specified by the lambda
function. Works only with Python2.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate working of

# List XOR

# Using reduce() + lambda + "^" operator

 

# initializing list

test_list = [4, 6, 2, 3, 8, 9]

 

# printing original list

print("The original list is : " + str(test_list))

 

# List XOR

# Using reduce() + lambda + "^" operator

res = reduce(lambda x, y: x ^ y, test_list)

 

# printing result 

print("The Bitwise XOR of list elements are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [4, 6, 2, 3, 8, 9]
    The Bitwise XOR of list elements are : 2
    

**Method #2 : Usingreduce() + operator.ixor**  
This task can also be performed using this method. In this the task performed
by lambda function in above method is performed using ior function for
cumulative XOR operation. Works with Python2 only.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate working of

# List XOR

# Using reduce() + operator.ixor

from operator import ixor

 

# initializing list

test_list = [4, 6, 2, 3, 8, 9]

 

# printing original list

print("The original list is : " + str(test_list))

 

# List XOR

# Using reduce() + operator.ixor

res = reduce(ixor, test_list)

 

# printing result 

print("The Bitwise XOR of list elements are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [4, 6, 2, 3, 8, 9]
    The Bitwise XOR of list elements are : 2
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

