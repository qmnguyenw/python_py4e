Python – Bitwise AND of List



Sometimes, while programming, we have a problem in which we might need to
perform certain bitwise operations among list elements. This is an essential
utility as we come across bitwise operations many times. Let’s discuss certain
ways in which this task can be performed.  
 **Method #1 : Using reduce() + lambda + “ &” operator**  
The above functions can be combined to perform this task. We can employ
reduce() to accumulate the result of AND logic specified by the lambda
function. Works only with Python2.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate working of

# Bitwise AND of List

# Using reduce() + lambda + "&" operator

# initializing list

test_list = [4, 6, 2, 3, 8, 9]

# printing original list

print("The original list is : " + str(test_list))

# Bitwise AND of List

# Using reduce() + lambda + "&" operator

res = reduce(lambda x, y: x & y, test_list)

# printing result

print("The Bitwise AND of list elements are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [4, 6, 2, 3, 8, 9]
    The Bitwise AND of list elements are : 0
    
    

  
**Method #2 : Using reduce() + operator.iand**  
This task can also be performed using this method. In this the task performed
by lambda function in above method is performed using iand function for
cumulative AND operation. Works with Python2 only.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate working of

# Bitwise AND of List

# Using functools.reduce() + operator.iand

from operator import iand

from functools import reduce

# initializing list

test_list = [4, 6, 2, 3, 8, 9]

# printing original list

print("The original list is : " + str(test_list))

# Bitwise AND of List

# Using functools.reduce() + operator.iand

res = reduce(iand, test_list)

# printing result

print("The Bitwise AND of list elements are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [4, 6, 2, 3, 8, 9]
    The Bitwise AND of list elements are : 0
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

