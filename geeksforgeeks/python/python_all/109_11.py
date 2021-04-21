Python – Get sum of last K list items using slice



Accessing elements in a list has many types and variations. These are an
essential part of Python programming and one must have the knowledge to
perform the same. This article discusses ways to fetch the last K elements and
do its summation. Let’s discuss certain solution to perform this task.

 **Method #1 : Using list slicing + sum()**  
This problem can be performed in 1 line rather than using a loop using the
list slicing functionality provided by Python and then using sum(). Minus
operator specifies slicing to be done from rear end.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Inverse K slice Sum

# using list slicing + sum()

 

# initializing list 

test_list = [4, 5, 2, 6, 7, 8, 10] 

 

# printing original list 

print("The original list : " + str(test_list)) 

 

# initializing K 

K = 5

 

# Inverse K slice Sum

# using list slicing + sum()

res = sum(test_list[-K:])

 

# print result 

print("The last K elements sum of list is : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list : [4, 5, 2, 6, 7, 8, 10]
    The last K elements sum of list is : 33
    

**Method #2 : Usingislice() + reversed() + sum()**  
The inbuilt funtions can also be used to perform this particular task. The
islice function can be used to get the sliced list and reversed function is
used to get the elements from rear end and then sum() can be employed to
perform summation.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Inverse K slice Sum

# using islice() + reversed() + sum()

from itertools import islice 

 

# initializing list 

test_list = [4, 5, 2, 6, 7, 8, 10] 

 

# printing original list 

print("The original list : " + str(test_list)) 

 

# initializing K 

K = 5

 

# using islice() + reversed() + sum()

# Inverse K slice Sum

res = list(islice(reversed(test_list), 0, K)) 

res.reverse()

res = sum(res)

 

# print result 

print("The last K elements sum of list are : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list : [4, 5, 2, 6, 7, 8, 10]
    The last K elements sum of list is : 33
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

