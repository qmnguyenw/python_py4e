Python | Repeat and Multiply list extension



Sometimes, while working with Python list, we can have a problem in which we
need to extend a list in a very customized way. We may have to repeat contents
of list and while doing that, each time new list must be a multiple of
original list. This incremental expansion has applications in many domains.
Let’s discuss a way in which this task can be performed.

 **Method : Using list comprehension**  
This task can be performed in a brute manner, but having a shorter
implementation using list comprehension always is better. In this, we perform
task in 2 steps, first we make a helper list to form a multiplication factor
list and then cumulate the result using original list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Repeat and Multiply list extension

# Using list comprehension

 

# initializing list

test_list = [4, 5, 6]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Extension factor

N = 4

 

# Multiply factor 

M = 3

 

# Repeat and Multiply list extension

# Using list comprehension

temp = [1 * M**i for i in range(N)]

res = list([ele * tele for tele in temp for ele in
test_list])

 

# printing result 

print("List after extension and multiplication : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [4, 5, 6]
    List after extension and multiplication : [4, 5, 6, 12, 15, 18, 36, 45, 54, 108, 135, 162]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

