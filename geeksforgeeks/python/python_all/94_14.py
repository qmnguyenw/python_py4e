Python – Summation of Unique elements



This article focuses on one of the operation of getting the unique list from a
list that contains a possible duplicates and performing its summation. This
operations has large no. of applications and hence it’s knowledge is good to
have.

 **Method 1 : Naive method + sum()**  
In naive method, we simply traverse the list and append the first occurrence
of the element in new list and ignore all the other occurrences of that
particular element. The task of summation is performed using sum().

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# Summation of Unique elements

# using naive methods + sum()

 

# initializing list

test_list = [1, 3, 5, 6, 3, 5, 6, 1]

print ("The original list is : " + str(test_list))

 

# using naive method + sum()

# Summation of Unique elements

# from list 

res = []

for i in test_list:

 if i not in res:

 res.append(i)

res = sum(res)

 

# printing list after removal 

print ("The unique elements summation : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 3, 5, 6, 3, 5, 6, 1]
    The unique elements summation : 15
    

**Method 2 : Usingset() + sum()**  
This is the most popular way by which the duplicated are removed from the
list. After that the summation of list can be performed using sum().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# Summation of Unique elements

# using set() + sum()

 

# initializing list

test_list = [1, 5, 3, 6, 3, 5, 6, 1]

print ("The original list is : " + str(test_list))

 

# using set() + sum()

# Summation of Unique elements

# from list 

res = sum(list(set(test_list)))

 

# Summation of Unique elements

# using set() + sum()

print ("The unique elements summation : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 3, 5, 6, 3, 5, 6, 1]
    The unique elements summation : 15
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

