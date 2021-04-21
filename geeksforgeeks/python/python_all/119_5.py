Python | Check if one tuple is subset of other



Sometimes, while working with Python, we can work with different data and we
might need to solve problem of checking if one subset is part of other. Let’s
discuss certain ways in which this task can be performed.

 **Method #1 : Using issubset()**  
We can solve this problem using type conversion of tuple into a set and then
check if one tuple is subset of other using issubset().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check if one tuple is subset of other

# using issubset()

 

# initialize tuples

test_tup1 = (10, 4, 5, 6)

test_tup2 = (5, 10)

 

# printing original tuples

print("The original tuple 1 : " + str(test_tup1))

print("The original tuple 2 : " + str(test_tup2))

 

# Check if one tuple is subset of other

# using issubset()

res = set(test_tup2).issubset(test_tup1)

 

# printing result

print("Is 2nd tuple subset of 1st ? : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple 1 : (10, 4, 5, 6)
    The original tuple 2 : (5, 10)
    Is 2nd tuple subset of 1st ? : True
    

**Method #2 : Usingall() \+ generator expression**  
The combination of above functionalities can also perform this task. In this,
we check for each element of one tuple with another using expression and
all().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check if one tuple is subset of other

# using all() + generator expression

 

# initialize tuples

test_tup1 = (10, 4, 5, 6)

test_tup2 = (5, 10)

 

# printing original tuples

print("The original tuple 1 : " + str(test_tup1))

print("The original tuple 2 : " + str(test_tup2))

 

# Check if one tuple is subset of other

# using all() + generator expression

res = all(ele in test_tup1 for ele in test_tup2)

 

# printing result

print("Is 2nd tuple subset of 1st ? : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple 1 : (10, 4, 5, 6)
    The original tuple 2 : (5, 10)
    Is 2nd tuple subset of 1st ? : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

