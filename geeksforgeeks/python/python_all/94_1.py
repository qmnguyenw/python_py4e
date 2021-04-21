Python – Unique values Multiplication



This article focuses on one of the operation of getting the unique list from a
list that contains a possible duplicates and performing its product. This
operations has large no. of applications and hence it’s knowledge is good to
have.

 **Method 1 : Naive method + loop**  
In naive method, we simply traverse the list and append the first occurrence
of the element in new list and ignore all the other occurrences of that
particular element. The task of product is performed using loop.

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# Unique values Multiplication

# using naive methods + loop

 

# getting Product 

def prod(val) : 

 res = 1

 for ele in val: 

 res *= ele 

 return res 

 

# initializing list

test_list = [1, 3, 5, 6, 3, 5, 6, 1]

print ("The original list is : " + str(test_list))

 

# using naive method + loop

# Unique values Multiplication

# from list 

res = []

for i in test_list:

 if i not in res:

 res.append(i)

res = prod(res)

 

# printing list after product

print ("The unique elements product : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 3, 5, 6, 3, 5, 6, 1]
    The unique elements product : 90
    

**Method 2 : Using set() + loop**  
This is the most popular way by which the duplicated are removed from the
list. After that the product of list can be performed using loop.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# Unique values Multiplication

# using set() + loop

 

# getting Product 

def prod(val) : 

 res = 1

 for ele in val: 

 res *= ele 

 return res 

 

# initializing list

test_list = [1, 5, 3, 6, 3, 5, 6, 1]

print ("The original list is : " + str(test_list))

 

# Unique values Multiplication

# using set() + loop 

res = prod(list(set(test_list)))

 

# Unique values Multiplication

# using set() + loop

# printing result

print ("The unique elements product : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 3, 5, 6, 3, 5, 6, 1]
    The unique elements product : 90
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

