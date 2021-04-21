Python | Test if any list element returns true for condition



Sometimes, while coding in Python, we can have a problem in which we need to
filter a list on basis of condition met by any of the element. This can have
it’s application in web development domain. Let’s discuss a shorthand in which
this task can be performed.

 **Method : Usingany() \+ list comprehension**  
The simplest way and shorthand to solve this problem is to combine the
functionalities of inbuilt any() and list comprehension for rendering
condition logic and list iteration. The any() returns true if any of the
list element matches the condition.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test if any list element returns true for condition

# Using any() + list comprehension

 

# initializing list

test_list = [6, 4, 8, 9, 10]

 

# printing list

print("The original list : " + str(test_list))

 

# Test if any list element returns true for condition

# Using any() + list comprehension

res = any(x % 5 for x in test_list)

 

# Printing result

print("Does list contain any element divisible by 5? : " +
str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
     
    The original list : [6, 4, 8, 9, 10]
    Does list contain any element divisible by 5? : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

