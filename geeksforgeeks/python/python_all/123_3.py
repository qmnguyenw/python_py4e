Python | Ways to concatenate tuples



Many times, while working with records, we can have a problem in which we need
to add two records and store them together. This requires concatenation. As
tuples are immutable, this task becomes little complex. Let’s discuss certain
ways in which this task can be performed.

 **Method #1 : Using+ operator**  
This is the most Pythonic and recommended method to perform this particular
task. In this, we add two tuples and return the concatenated tuple. No
previous tuple is changed in this process.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Ways to concatenate tuples

# using + operator

 

# initialize tuples

test_tup1 = (1, 3, 5)

test_tup2 = (4, 6)

 

# printing original tuples

print("The original tuple 1 : " + str(test_tup1))

print("The original tuple 2 : " + str(test_tup2))

 

# Ways to concatenate tuples

# using + operator

res = test_tup1 + test_tup2

 

# printing result

print("The tuple after concatenation is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple 1 : (1, 3, 5)
    The original tuple 2 : (4, 6)
    The tuple after concatenation is : (1, 3, 5, 4, 6)
    

**Method #2 : Usingsum()**  
This is yet another way in which this task can be performed. In this, we add
the tuples to one other using sum function.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Ways to concatenate tuples

# using sum()

 

# initialize tuples

test_tup1 = (1, 3, 5)

test_tup2 = (4, 6)

 

# printing original tuples

print("The original tuple 1 : " + str(test_tup1))

print("The original tuple 2 : " + str(test_tup2))

 

# Ways to concatenate tuples

# using sum()

res = sum((test_tup1, test_tup2), ())

 

# printing result

print("The tuple after concatenation is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple 1 : (1, 3, 5)
    The original tuple 2 : (4, 6)
    The tuple after concatenation is : (1, 3, 5, 4, 6)
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

