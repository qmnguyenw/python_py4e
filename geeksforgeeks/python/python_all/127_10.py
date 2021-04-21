Python | Search in Nth Column of Matrix



Sometimes, while working with Python Matrix, we can have a problem in which we
need to check if an element is present or not. This problem is simpler, but a
variation to it can be to perform a check in particular column of Matrix.
Let’s discuss a shorthand by which this task can be performed.

 **Method : Usingany() \+ list comprehension**  
This task can be performed using combination of above functions in which we
imply list comprehension for iteration and support tasks and any() can be
used to check for any occurrence of the desired character.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Search in Nth Column of Matrix

# Using any() + list comprehension

 

# initializing list 

test_list = [[1, 4, 5], [6, 7, 8], [8, 3,
0]]

 

# printing list 

print("The original list : " + str(test_list))

 

# initializing N 

N = 1

 

# initializing num

ele = 3

 

# Search in Nth Column of Matrix

# Using any() + list comprehension

res = any(sub[N] == ele for sub in test_list)

 

# Printing result

print("Does element exists in particular column : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
     
    The original list : [[1, 4, 5], [6, 7, 8], [8, 3, 0]]
    Does element exists in particular column : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

