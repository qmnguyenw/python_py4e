Python – Chunked interleave of Lists



Sometimes, while working with Lists, we can have a problem to perform merge
operation. The simpler version is easy to implement. But when it comes to
implement a variation of it, i.e the case in which we need to interleave in
chunks alternatively, it becomes a tougher task. Let’s discuss certain way in
which this task can be performed.

 **Method : Using loop +extend()**  
This task can be performed by using the above functionalities. In this, we
compute the iterations required and then run a loop as many times. We add
elements in list using extend() and variable number specified.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Chunked interleave of Lists

# using loop + extend()

 

# Initializing lists

test_list1 = [4, 5, 6, 8, 10, 11]

test_list2 = [6, 7, 8, 9, 8, 12]

 

# printing original lists 

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# Initializing step

step = 3

 

# Chunked interleave of Lists

# using loop + extend()

num = len(test_list1)

iters = int(num / step) + 1

res = []

for idx in range(iters):

 start = step * idx

 end = step * (idx + 1)

 res.extend(test_list1[start : end])

 res.extend(test_list2[start : end])

 

# printing result 

print ("List after chunked merge : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 is : [4, 5, 6, 8, 10, 11]
    The original list 2 is : [6, 7, 8, 9, 8, 12]
    List after chunked merge : [4, 5, 6, 6, 7, 8, 8, 10, 11, 9, 8, 12]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

