Python | Cummulative Columns summation of Records



Sometimes, while working with records, we can have a problem in which we need
to sum all the columns of a container of lists which are tuples. This kind of
application is common in web development domain. Let’s discuss certain ways in
which this task can be performed.

 **Method #1 : Usingsum() \+ list comprehension + zip()**  
This task can be performed using combination of above functions. In this, we
cummulate the like index elements, i.e columns using zip(), and then iterate
through them using list comprehension and perform summation using sum().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Cummulative Columns summation of Records

# using list comprehension + sum() + zip()

 

# initialize list

test_list = [(1, 2, 3), (6, 7, 6), (1, 6,
8)]

 

# printing original list

print("The original list : " + str(test_list))

 

# Cummulative Columns summation of Records

# using list comprehension + sum() + zip()

res = [sum(ele) for ele in zip(*test_list)]

 

# printing result

print("The Cummulative column sum is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [(1, 2, 3), (6, 7, 6), (1, 6, 8)]
    The Cummulative column sum is : [8, 15, 17]
    

**Method #2 : Usingzip() + map() + sum()**  
This method is similar to the above method. In this, the task performed by
list comprehension is performed by map(), which extends the summation of
columns to zipped elements.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Cummulative Columns summation of Records

# using zip() + map() + sum()

 

# initialize list

test_list = [(1, 2, 3), (6, 7, 6), (1, 6,
8)]

 

# printing original list

print("The original list : " + str(test_list))

 

# Cummulative Columns summation of Records

# using zip() + map() + sum()

res = list(map(sum, zip(*test_list)))

 

# printing result

print("The Cummulative column sum is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [(1, 2, 3), (6, 7, 6), (1, 6, 8)]
    The Cummulative column sum is : [8, 15, 17]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

