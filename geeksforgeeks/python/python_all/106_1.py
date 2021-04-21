Python | Records Intersection



Sometimes, while working with tuples, we can have a problem in which we need
similar features of two records. This type of application can come in Data
Science domain. Let’s discuss certain ways in which this problem can be
solved.

 **Method #1 : Usingset() + "&" operator**  
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

# Records Intersection

# Using set() + "&" operator

 

# initialize tuples

test_tup1 = (3, 4, 5, 6)

test_tup2 = (5, 7, 4, 10)

 

# printing original tuples

print("The original tuple 1 : " + str(test_tup1))

print("The original tuple 2 : " + str(test_tup2))

 

# Records Intersection

# Using set() + "&" operator

res = tuple(set(test_tup1) & set(test_tup2))

 

# printing result

print("The similar elements from tuples are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple 1 : (3, 4, 5, 6)
    The original tuple 2 : (5, 7, 4, 10)
    The similar elements from tuples are : (4, 5)
    

**Method #2 : Usingintersection() + set()**  
This is method similar to above method, the difference is that instead of &
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

# Records Intersection

# Using intersection() + set()

 

# initialize tuples

test_tup1 = (3, 4, 5, 6)

test_tup2 = (5, 7, 4, 10)

 

# printing original tuples

print("The original tuple 1 : " + str(test_tup1))

print("The original tuple 2 : " + str(test_tup2))

 

# Records Intersection

# Using intersection() + set()

res = tuple(set(test_tup1).intersection(set(test_tup2)))

 

# printing result

print("The similar elements from tuples are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple 1 : (3, 4, 5, 6)
    The original tuple 2 : (5, 7, 4, 10)
    The similar elements from tuples are : (4, 5)
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

