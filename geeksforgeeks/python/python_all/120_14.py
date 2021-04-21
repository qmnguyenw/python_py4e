Python | Find Dissimilar Elements in Tuples



Sometimes, while working with tuples, we can have a problem in which we need
dissimilar features of two records. This type of application can come in Data
Science domain. Let’s discuss certain ways in which this problem can be
solved.

 **Method #1 : Usingset() + "^" operator**

This task can be performed using symmetric difference functionality offered by
XOR operator over sets. The conversion to set is done by set().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Dissimilar elements in tuples

# Using set() + "^" operator

 

# initialize tuples

test_tup1 = (3, 4, 5, 6)

test_tup2 = (5, 7, 4, 10)

 

# printing original tuples

print("The original tuple 1 : " + str(test_tup1))

print("The original tuple 2 : " + str(test_tup2))

 

# Dissimilar elements in tuples

# Using set() + "^" operator

res = tuple(set(test_tup1) ^ set(test_tup2))

 

# printing result

print("The Dissimilar elements from tuples are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple 1 : (3, 4, 5, 6)
    The original tuple 2 : (5, 7, 4, 10)
    The Dissimilar elements from tuples are : (3, 6, 7, 10)
    

  

  

**Method #2 : Usingsymmetric_difference() + set()**

This is method similar to above method, the difference is that instead of XOR
operator, we use inbuilt function to perform the task of filtering dissimilar
elements.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Dissimilar elements in tuples

# Using symmetric_difference() + set()

 

# initialize tuples

test_tup1 = (3, 4, 5, 6)

test_tup2 = (5, 7, 4, 10)

 

# printing original tuples

print("The original tuple 1 : " + str(test_tup1))

print("The original tuple 2 : " + str(test_tup2))

 

# Dissimilar elements in tuples

# Using symmetric_difference() + set()

res =
tuple(set(test_tup1).symmetric_difference(set(test_tup2)))

 

# printing result

print("The Dissimilar elements from tuples are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple 1 : (3, 4, 5, 6)
    The original tuple 2 : (5, 7, 4, 10)
    The Dissimilar elements from tuples are : (3, 6, 7, 10)
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

