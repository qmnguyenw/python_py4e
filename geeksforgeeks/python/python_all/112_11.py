Python – Test if Tuple contains K



Sometimes, while working with Python, we can have a problem in which we have a
record and we need to check if it contains K. This kind of problem is common
in data preprocessing steps. Let’s discuss certain ways in which this task can
be performed.

 **Method #1 : Using any() + map() \+ lambda**  
Combination of above functions can be used to perform this task. In this, we
check for any element using any() and extension of logic is done by map() and
lambda.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test if Tuple contains K

# using any() + map() + lambda

 

# initialize tuple

test_tup = (10, 4, 5, 6, 8)

 

# printing original tuple

print("The original tuple : " + str(test_tup))

 

# initialize K 

K = 6

 

# Test if Tuple contains K

# using any() + map() + lambda

res = any(map(lambda ele: ele is K, test_tup))

 

# printing result

print("Does tuple contain any K value ? : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple : (10, 4, 5, 6, 8)
    Does tuple contain any K value ? : True
    

**Method #2 : Using loop**  
This task can be performed using loop as well using brute force constructs. We
just iterate through the tuple and when we encounter K, we set flag to True
and break.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test if Tuple contains K

# Using loop

 

# initialize tuple

test_tup = (10, 4, 5, 6, 8)

 

# printing original tuple

print("The original tuple : " + str(test_tup))

 

# initialize K 

K = 6

 

# Test if Tuple contains K

# Using loop

res = False

for ele in test_tup:

 if ele == K:

 res = True

 break

 

# printing result

print("Does tuple contain any K value ? : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple : (10, 4, 5, 6, 8)
    Does tuple contain any K value ? : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

