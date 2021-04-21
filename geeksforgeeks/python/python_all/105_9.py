Python – Index match element Product



Sometimes, while working with Python list we can have a problem in which we
have to compare two lists for index similarity and hence can have a task of
mutiplication equal index pairs. Let’s discuss certain way in which this task
can be performed.

 **Method #1 : Using loop +zip()**  
This task can be performed by passing the zip(), which performs task of
mapping both list with each other, to the function which computes the product
according to equal indices.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Index match element Product

# using loop + zip()

 

def prod(val) : 

 res = 1

 for ele in list(val): 

 res *= ele 

 return res

 

# initialize lists

test_list1 = [5, 6, 10, 4, 7, 1, 19]

test_list2 = [6, 6, 10, 3, 7, 10, 19]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# Index match element Product

# using loop + zip()

res = prod(x for x, y in zip(test_list1, test_list2) if x
== y)

 

# printing result

print("Multiplication of Identical elements : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 is : [5, 6, 10, 4, 7, 1, 19]
    The original list 2 is : [6, 6, 10, 3, 7, 10, 19]
    Multiplication of Identical elements : 7980
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

