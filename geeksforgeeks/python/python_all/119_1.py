Python | Check if tuple has any None value



Sometimes, while working with Python, we can have a problem in which we have a
record and we need to check if it contains all valid values i.e has any None
value. This kind of problem is common in data preprocessing steps. Let’s
discuss certain ways in which this task can be performed.

 **Method #1 : Usingany() + map() + lambda**  
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

# Check if tuple has any None value

# using any() + map() + lambda

 

# initialize tuple

test_tup = (10, 4, 5, 6, None)

 

# printing original tuple

print("The original tuple : " + str(test_tup))

 

# Check if tuple has any None value

# using any() + map() + lambda

res = any(map(lambda ele: ele is None, test_tup))

 

# printing result

print("Does tuple contain any None value ? : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple : (10, 4, 5, 6, None)
    Does tuple contain any None value ? : True
    

**Method #2 : Using not +all()**  
This checks for truthness of all elements of tuple using all() and with not,
returns True if there is no None element.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Check if tuple has any None value

# using not + all()

 

# initialize tuple

test_tup = (10, 4, 5, 6, None)

 

# printing original tuple

print("The original tuple : " + str(test_tup))

 

# Check if tuple has any None value

# using not + all()

res = not all(test_tup)

 

# printing result

print("Does tuple contain any None value ? : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple : (10, 4, 5, 6, None)
    Does tuple contain any None value ? : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

