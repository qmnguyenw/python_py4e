Python – Successive element pairing



Sometimes, while working with Python list, we can have a problem in which we
need to construct tuples, with the succeeding element, whenever that element
matches a particular condition. This can have potential application in day-day
programming. Let’s discuss a way in which this task can be performed.

 **Method : Usingzip() \+ list comprehension**  
This task can be performed using the combination of above functionalities. In
this, the zip() performs the task of construction of tuples and the catering
of condition matching and iteration is handled by list comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Successive element pairing

# using zip() + list comprehension

 

# initialize list

test_list = [1, 4, 'gfg', 7, 8, 'gfg', 9,
'gfg', 10]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initialize ele 

ele = 'gfg'

 

# Successive element pairing

# using zip() + list comprehension

res = [(x, y) for x, y in zip(test_list, test_list[1 : ])
if x == ele]

 

# printing result

print("Tuple list with desired Successive elements " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 4, 'gfg', 7, 8, 'gfg', 9, 'gfg', 10]
    Tuple list with desired Successive elements [('gfg', 7), ('gfg', 9), ('gfg', 10)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

