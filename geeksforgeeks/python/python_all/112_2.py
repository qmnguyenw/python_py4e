Python – Incremental List Extension



Sometimes, while working with Python list, we can have a problem in which we
need to extend a list in a very customized way. We may have to repeat contents
of list and while doing that, each time new list must add a number to original
list. This incremental expansion has applications in many domains. Let’s
discuss a way in which this task can be performed.

 **Method : Using list comprehension**  
This task can be performed in a brute manner, but having a shorter
implementation using list comprehension always is better. In this, we perform
task in 2 steps, first we make a helper list to form a addition factor list
and then cumulate the result using original list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Incremental List Extension

# Using list comprehension

 

# initializing list

test_list = [7, 8, 9]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Extension factor

N = 4

 

# Addition factor 

M = 3

 

# Incremental List Extension

# Using list comprehension

temp = [1 * M**i for i in range(N)]

temp[0] = 0

res = list([ele + tele for tele in temp for ele in
test_list])

 

# printing result 

print("List after extension and addition : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [7, 8, 9]
    List after extension and addition : [7, 8, 9, 10, 11, 12, 16, 17, 18, 34, 35, 36]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

