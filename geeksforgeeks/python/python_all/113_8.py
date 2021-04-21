Python | Nth tuple index Subtraction by K



Many times, while working with records, we can have a problem in which we need
to change the value of tuple elements. This is a common problem while working
with tuples. Let’s discuss certain ways in which K can be subtracted to Nth
element of tuple in list.

 **Method #1 : Using loop**  
Using loops this task can be performed. In this, we just iterate the list to
change the Nth element by predefined value K in code.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Nth tuple element Subtraction by K

# Using loop

 

# Initializing list

test_list = [(4, 5, 6), (7, 4, 2), (9,
10, 11)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Initializing N 

N = 1

 

# Initializing K 

K = 3

 

# Nth tuple element Subtraction by K

# Using loop

res = []

for i in range(0, len(test_list)):

 res.append((test_list[i][0], test_list[i][N] - K,
test_list[i][2]))

 

# printing result

print("The tuple after removing K from Nth element : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [(4, 5, 6), (7, 4, 2), (9, 10, 11)]
    The tuple after removing K from Nth element : [(4, 2, 6), (7, 1, 2), (9, 7, 11)]
    

**Method #2 : Using list comprehension**  
This method is having the same approach as the above method, just reduces
lines of code using list comprehension functionality to make code compact by
size.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Nth tuple element Subtraction by K

# Using list comprehension

 

# Initializing list

test_list = [(4, 5, 6), (7, 4, 2), (9,
10, 11)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Initializing N 

N = 1

 

# Initializing K 

K = 3

 

# Nth tuple element Subtraction by K

# Using list comprehension

res = [(a, b - K, c) for a, b, c in test_list]

 

# printing result

print("The tuple after removing K from Nth element : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [(4, 5, 6), (7, 4, 2), (9, 10, 11)]
    The tuple after removing K from Nth element : [(4, 2, 6), (7, 1, 2), (9, 7, 11)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

