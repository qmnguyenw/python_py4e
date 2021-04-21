Python – Test if all elements in list are of same type



Sometimes, while working with Python, we can have a problem in which we need
to test if all the elements of argument are of same type or not. This can have
application in many domains such as data Science and day-day programming. Lets
discuss certain ways in which this task can be performed.

 **Method #1 : Using loop +isinstance()**  
The combination of above functionalities can be used to perform this task. In
this, we test for type using isinstance() and check for all elements if they
match same type as of 1st element.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Test if all elements in list are of same type

# using loop + isinstance()

 

# Initializing lists

test_list = [5, 6, 2, 5, 7, 9]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Test if all elements in list are of same type

# using loop + isinstance()

res = True

for ele in test_list:

 if not isinstance(ele, type(test_list[0])):

 res = False

 break

 

# printing result 

print ("Do all elements have same type : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [5, 6, 2, 5, 7, 9]
    Do all elements have same type : True
    

**Method #2 : Usingall() + isinstance()**  
This is yet another way to perform this task. In this, we instead of iterating
perform the task in one line using all and instance().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Test if all elements in list are of same type

# using all() + isinstance()

 

# Initializing lists

test_list = [5, 6, 2, 5, 7, 9]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Test if all elements in list are of same type

# using all() + isinstance()

res = all(isinstance(sub, type(test_list[0])) for sub
in test_list[1:])

 

# printing result 

print ("Do all elements have same type : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [5, 6, 2, 5, 7, 9]
    Do all elements have same type : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

