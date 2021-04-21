Python – List product excluding duplicates



This article focuses on one of the operation of getting the unique list from a
list that contains a possible duplicated and finding its product. This
operations has large no. of applications and hence it’s knowledge is good to
have.

 **Method 1 : Naive method**  
In naive method, we simply traverse the list and append the first occurrence
of the element in new list and ignore all the other occurrences of that
particular element. The task of performing product is done using loop.

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# Duplication Removal List Product

# using naive methods 

 

# getting Product 

def prod(val) : 

 res = 1

 for ele in val: 

 res *= ele 

 return res 

 

# initializing list

test_list = [1, 3, 5, 6, 3, 5, 6, 1]

print ("The original list is : " + str(test_list))

 

# using naive method

# Duplication Removal List Product

res = []

for i in test_list:

 if i not in res:

 res.append(i)

res = prod(res)

 

# printing list after removal 

print ("Duplication removal list product : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 3, 5, 6, 3, 5, 6, 1]
    Duplication removal list product : 90
    

**Method 2 : Using list comprehension**  
This method has working similar to the above method, but this is just a one-
liner shorthand of longer method done with the help of list comprehension.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# Duplication Removal List Product

# using list comprehension

 

# getting Product 

def prod(val) : 

 res = 1

 for ele in val: 

 res *= ele 

 return res 

 

# initializing list

test_list = [1, 3, 5, 6, 3, 5, 6, 1]

print ("The original list is : " + str(test_list))

 

# using list comprehension

# Duplication Removal List Product

res = []

[res.append(x) for x in test_list if x not in res]

res = prod(res)

 

# printing list after removal 

print ("Duplication removal list product : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 3, 5, 6, 3, 5, 6, 1]
    Duplication removal list product : 90
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

