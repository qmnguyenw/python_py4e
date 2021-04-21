Python | Get last N elements from given list



Accessing elements in a list has many types and variations. These are an
essential part of Python programming and one must have the knowledge to
perform the same. This article discusses ways to fetch the last N elements of
list. Let’s discuss certain solution to perform this task.

 **Method #1 : Using list slicing**

This problem can be performed in 1 line rather than using a loop using the
list slicing functionality provided by Python. Minus operator specifies
slicing to be done from rear end.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Get last N elements from list

# using list slicing

 

# initializing list

test_list = [4, 5, 2, 6, 7, 8, 10]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing N

N = 5

 

# using list slicing

# Get last N elements from list

res = test_list[-N:]

 

# print result

print("The last N elements of list are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [4, 5, 2, 6, 7, 8, 10]
    The last N elements of list are : [2, 6, 7, 8, 10]
    

  

  

**Method #2 : Usingislice() + reversed()**

The inbuilt funtions can also be used to perform this particular task. The
islice function can be used to get the sliced list and reversed function is
used to get the elements from rear end.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Get last N elements from list

# using islice() + reversed()

from itertools import islice

 

# initializing list

test_list = [4, 5, 2, 6, 7, 8, 10]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing N

N = 5

 

# using islice() + reversed()

# Get last N elements from list

res = list(islice(reversed(test_list), 0, N))

res.reverse()

 

# print result

print("The last N elements of list are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [4, 5, 2, 6, 7, 8, 10]
    The last N elements of list are : [2, 6, 7, 8, 10]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

