Difference between == and is operator in Python



The Equality operator (==) compares the values of both the operands and checks
for value equality. Whereas the ‘ **is’** **** operator checks whether both
the operands refer to the same object or not.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# python3 code to

# illustrate the

# difference between

# == and is operator

# [] is an empty list

list1 = []

list2 = []

list3=list1

if (list1 == list2):

 print("True")

else:

 print("False")

if (list1 is list2):

 print("True")

else:

 print("False")

if (list1 is list3):

 print("True")

else: 

 print("False")

list3 = list3 + list2

if (list1 is list3):

 print("True")

else: 

 print("False")  
  
---  
  
 __

 __

 **Output:**  

    
    
    True
    False
    True
    False
    

  * The output of the **first if** the condition is “True” as both list1 and list2 are empty lists.
  *  **Second** , **if** the condition shows “False” because two empty lists are at different memory locations. Hence list1 and list2 refer to different objects. We can check it with **id()** function in python which returns the “identity” of an object.
  * The output of the **third if** the condition is “True” as both list1 and list3 are pointing to the same object.
  * The output of the **fourth if** the condition is “False” because the concatenation of two lists always produces a new list.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

list1= []

list2 = []

print(id(list1))

print(id(list2))  
  
---  
  
 __

 __

 **Output:**  

    
    
    139877155242696
    139877155253640
    

This shows list1 and list2 refers to different objects.  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

