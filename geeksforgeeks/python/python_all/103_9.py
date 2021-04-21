Python | List Inversions



Sometimes, while programming, we have a problem in which we might need to
perform certain bitwise operations among list elements. This is an essential
utility as we come across bitwise operations many times. Let’s discuss certain
ways in which this task can be performed.

 **Method #1 : Usingmap() + lambda + "~" operator**  
The above functions can be combined to perform this task. We can employ map()
to accumulate the result of Inversion logic specified by the lambda function.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# List Inversions

# Using map() + lambda + "~" operator

 

# initializing list

test_list = [7, 8, 9, 1, 10, 7]

 

# printing original list

print("The original list is : " + str(test_list))

 

# List Inversions

# Using map() + lambda + "~" operator

res = list(map(lambda x: ~x, test_list)) 

 

# printing result 

print("The Bitwise Inversions of list elements are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [7, 8, 9, 1, 10, 7]
    The Bitwise Inversions of list elements are : [-8, -9, -10, -2, -11, -8]
    

**Method #2 : Usingmap() + operator.invert**  
This task can also be performed using this method. In this the task performed
by lambda function in above method is performed using ior function for
cumulative Inversion operation.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate working of

# List Inversions

# Using map() + operator.invert

from operator import invert

 

# initializing list

test_list = [7, 8, 9, 1, 10, 7]

 

# printing original list

print("The original list is : " + str(test_list))

 

# List Inversions

# Using map() + operator.invert

res = list(map(invert, test_list))

 

# printing result 

print("The Bitwise Inversions of list elements are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [7, 8, 9, 1, 10, 7]
    The Bitwise Inversions of list elements are : [-8, -9, -10, -2, -11, -8]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

