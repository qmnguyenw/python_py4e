Python | Index Maximum among Tuples



Sometimes, while working with records, we might have a common problem of
maximizing contents of one tuple with corresponding index of other tuple. This
has application in almost all the domains in which we work with tuple records.
Let’s discuss certain ways in which this task can be performed.

 **Method #1 : Usingmap() + lambda + max()**  
Combination of above functionalities can solve the problem for us. In this, we
compute the maximum using lambda functions and max() and extend the logic to
keys using map().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Index Maximum among Tuples

# using map() + lambda + max()

 

# initialize tuples 

test_tup1 = (10, 4, 5)

test_tup2 = (2, 5, 18)

 

# printing original tuples 

print("The original tuple 1 : " + str(test_tup1))

print("The original tuple 2 : " + str(test_tup2))

 

# Index Maximum among Tuples

# using map() + lambda + max()

res = tuple(map(lambda i, j: max(i, j), test_tup1,
test_tup2))

 

# printing result

print("Resultant tuple after maximization : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple 1 : (10, 4, 5)
    The original tuple 2 : (2, 5, 18)
    Resultant tuple after maximization : (10, 5, 18)
    

**Method #2 : Usingmap() + zip() + max()**  
The combination of above functions can also be used to achieve this particular
task. In this, we add inbuilt max() to perform maximization and zip the like
indices using zip() and extend logic to both tuples using map().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Index Maximum among Tuples

# using map() + zip() + max()

 

# initialize tuples 

test_tup1 = (10, 4, 5)

test_tup2 = (2, 5, 18)

 

# printing original tuples 

print("The original tuple 1 : " + str(test_tup1))

print("The original tuple 2 : " + str(test_tup2))

 

# Index Maximum among Tuples

# using map() + zip() + max()

res = tuple(map(max, zip(test_tup1, test_tup2)))

 

# printing result

print("Resultant tuple after maximization : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple 1 : (10, 4, 5)
    The original tuple 2 : (2, 5, 18)
    Resultant tuple after maximization : (10, 5, 18)
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

