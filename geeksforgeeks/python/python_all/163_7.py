Python | Check if two lists have any element in common



Sometimes we encounter the problem of checking if one list contains any
element of another list. This kind of problems is quite popular in competitive
programming. Let’s discuss various ways to achieve this particular task.

 **Method #1:** Using any()

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to check if two lists

# have any element in common

 

# Initialization of list

list1 = [1, 2, 3, 4, 55]

list2 = [2, 3, 90, 22]

 

# using any function

out = any(check in list1 for check in list2)

 

# Checking condition

if out:

 print("True") 

else :

 print("False")  
  
---  
  
 __

 __

 **Output:**

    
    
    True
    

  
**Method #2:** Using **_in_** operator.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to check if two lists

# have any element in common

 

# Initialization of list

list1 = [1, 3, 4, 55]

list2 = [90, 22]

 

flag = 0

 

# Using in to check element of

# second list into first list

for elem in list2:

 if elem in list1:

 flag = 1

 

# checking condition

if flag == 1:

 print("True") 

else :

 print("False")  
  
---  
  
 __

 __

 **Output:**

    
    
    False
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

