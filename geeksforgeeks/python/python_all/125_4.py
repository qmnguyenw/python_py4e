Python | Custom sorting in list of tuples



Sometimes, while working with list of tuples, we can have a problem in which
we need to perform it’s sorting. Naive sorting is easier, but sometimes, we
have to perform custom sorting, i.e by decreasing order of first element and
increasing order of 2nd element. And these can also be in cases of different
types of tuples. Let’s discuss certain cases and solutions to perform this
kind of custom sorting.

 **Method #1 : Usingsorted() \+ lambda**  
This task can be performed using the combination of above functions. In this,
we just perform the normal sort, but in addition we feed a lambda function
which handles the case of custom sorting discussed above.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Custom sorting in list of tuples

# Using sorted() + lambda

 

# Initializing list

test_list = [(7, 8), (5, 6), (7, 5), (10,
4), (10, 1)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Custom sorting in list of tuples

# Using sorted() + lambda

res = sorted(test_list, key = lambda sub: (-sub[0],
sub[1]))

 

# printing result

print("The tuple after custom sorting is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [(7, 8), (5, 6), (7, 5), (10, 4), (10, 1)]
    The tuple after custom sorting is : [(10, 1), (10, 4), (7, 5), (7, 8), (5, 6)]
    

**Method #2 : Usingsorted() + lambda() + sum() ( With sum of tuple
condition)**  
In this method, similar solution sustains. But the case here is that we have
tuple as the 2nd element of tuple and its sum has to considered for sort
order. Other functions than summation can be extended in similar solution.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Custom sorting in list of tuples

# Using sorted() + lambda() + sum()

 

# Initializing list

test_list = [(7, (8, 4)), (5, (6, 1)), (7,
(5, 3)), (10, (5, 4)), (10, (1, 3))]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Custom sorting in list of tuples

# Using sorted() + lambda() + sum()

res = sorted(test_list, key = lambda sub: (-sub[0],
sum(sub[1])))

 

# printing result

print("The tuple after custom sorting is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [(7, (8, 4)), (5, (6, 1)), (7, (5, 3)), (10, (5, 4)), (10, (1, 3))]
    The tuple after custom sorting is : [(10, (1, 3)), (10, (5, 4)), (7, (5, 3)), (7, (8, 4)), (5, (6, 1))]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

