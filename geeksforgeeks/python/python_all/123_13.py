Python | Segregate True and False value indices



Sometimes, while working with Python lists, we can have a problem in which we
have boolean list and require to have indices of True and False values
separately. This can have a possible use in Data Science domain. Let’s discuss
certain ways in which this task can be performed.

 **Method #1 : Using loop**  
This is the one way in which this task can be performed. We create different
lists and check for True or False values using conditional statements and
append it’s index accordingly in dedicated lists.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Segregate True and False value indices

# using loops

 

# initialize list

test_list = [False, True, False, False, True,
True]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Segregate True and False value indices

# using loops

res_true, res_false = [], []

for i in range(0, len(test_list)):

 if test_list[i]:

 res_true.append(i)

 else :

 res_false.append(i)

 

# printing result

print("True indices after grouping : " + str(res_true))

print("False indices after grouping : " + str(res_false))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [False, True, False, False, True, True]
    True indices after grouping : [1, 4, 5]
    False indices after grouping : [0, 2, 3]
    

**Method #2 : Using loop +enumerate()**  
This task can be solved in a brute manner by using above functionalities. In
this, we make a choice of append list and add elements accordingly in
dedicated lists.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Segregate True and False value indices

# using loop + enumerate()

 

# initialize list

test_list = [False, True, False, False, True,
True]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Segregate True and False value indices

# using loop + enumerate()

res_true, res_false = [], []

for i, ele in enumerate(test_list):

 temp = res_true if ele else res_false

 temp.append(i)

 

# printing result

print("True indices after grouping : " + str(res_true))

print("False indices after grouping : " + str(res_false))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [False, True, False, False, True, True]
    True indices after grouping : [1, 4, 5]
    False indices after grouping : [0, 2, 3]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

