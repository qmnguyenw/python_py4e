Python | Records list XOR



Sometimes, while programming, we have a problem in which we might need to
perform certain bitwise operations among tuple list elements. This is an
essential utility as we come across bitwise operations many times. Let’s
discuss certain ways in which XOR can be performed.

 **Method #1 : Usingreduce() + lambda + “^” operator \+ loop**  
The above functions can be combined to perform this task. We can first flatten
the tuple list using loop and then employ reduce() to accumulate the result of
XOR logic specified by the lambda function. Works only with Python2.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate working of

# Records list XOR

# Using reduce() + lambda + "^" operator + loops

 

# initializing list 

test_list = [(4, 6), (2, ), (3, 8, 9)] 

 

# printing original list 

print("The original list is : " + str(test_list)) 

 

# Records list XOR

# Using reduce() + lambda + "^" operator + loops

temp = []

for sub in test_list:

 for ele in sub:

 temp.append(ele)

res = reduce(lambda x, y: x ^ y, temp) 

 

# printing result 

print("The Bitwise XOR of records list elements are : " + str(res))
  
  
---  
  
__

__

**Output :**

    
    
    The original list is : [(4, 6), (2, ), (3, 8, 9)]
    The Bitwise XOR of records list elements are : 2
    

**Method #2 : Usingreduce() + operator.ixor + chain()**  
This task can also be performed using this method. In this the task performed
by lambda function in above method is performed using ior function for
cumulative XOR operation, the flattening of elements to list is performed
using chain(). Works with Python2 only.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate working of

# Records list XOR

# Using reduce() + operator.ixor 

from operator import ixor 

from itertools import chain

 

# initializing list 

test_list = [(4, 6), (2, ), (3, 8, 9)] 

 

# printing original list 

print("The original list is : " + str(test_list)) 

 

# Records list XOR

# Using reduce() + operator.ixor 

temp = list(chain(*test_list))

res = reduce(ixor, temp) 

 

# printing result 

print("The Bitwise XOR of records list elements are : " + str(res))
  
  
---  
  
__

__

**Output :**

    
    
    The original list is : [(4, 6), (2, ), (3, 8, 9)]
    The Bitwise XOR of records list elements are : 2
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

