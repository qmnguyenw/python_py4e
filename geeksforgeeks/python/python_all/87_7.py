Python – Multiply all cross list element pairs



Sometimes, while working with Python list, we can have a problem in which we
need to perform multiplication of each element of list with other list. This
can have application in both web development and day-day programming. Lets
discuss certain ways in which this task can be performed.

 **Method #1 : Using list comprehension**  
This is the most straight forward method to perform this task. In this, we
iterate the both the list and perform multiplication of each element with
other and store result in new list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Multiply all cross list element pairs

# using list comprehension

 

# Initializing lists

test_list1 = [4, 5, 6]

test_list2 = [6, 4, 2]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# Multiply all cross list element pairs

# using list comprehension

res = [i * j for j in test_list1 for i in
test_list2]

 

# printing result 

print ("The multiplication list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 is : [4, 5, 6]
    The original list 2 is : [6, 4, 2]
    The multiplication list is : [24, 16, 8, 30, 20, 10, 36, 24, 12]
    

**Method #2 : Usingproduct()**  
This is another way in which this task can be performed. In this, we perform
the task of multiplication using product().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Multiply all cross list element pairs

# using product()

from itertools import product

 

# Initializing lists

test_list1 = [4, 5, 6]

test_list2 = [6, 4, 2]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# Multiply all cross list element pairs

# using product()

res = [a * b for a, b in product(test_list1, test_list2)]

 

# printing result 

print ("The multiplication list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 is : [4, 5, 6]
    The original list 2 is : [6, 4, 2]
    The multiplication list is : [24, 16, 8, 30, 20, 10, 36, 24, 12]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

